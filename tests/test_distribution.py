"""Distribution regressions; these do not evaluate model teaching quality."""
import importlib.util
from pathlib import Path
import re
import shutil
import subprocess
import tempfile
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('bundle', ROOT / 'scripts/build-bundle.py')
bundle = importlib.util.module_from_spec(spec)
spec.loader.exec_module(bundle)


class BundleTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.skill = Path(self.tmp.name) / 'kaogong'
        shutil.copytree(ROOT / 'skills/kaogong', self.skill)
        self.patcher = patch.object(bundle, 'SKILL_DIR', self.skill)
        self.patcher.start()
        self.addCleanup(self.patcher.stop)

    def test_full_includes_every_reference_once(self):
        for ref in (self.skill / 'references').glob('*.md'):
            with ref.open('a') as f:
                f.write(f'\nUNIQUE_REFERENCE_{ref.stem}\n')
        output = bundle.build_full()
        for ref in (self.skill / 'references').glob('*.md'):
            self.assertEqual(output.count(f'UNIQUE_REFERENCE_{ref.stem}\n'), 1)
        self.assertNotRegex(output, r'\]\((?:references/|\.\./)[^)]+\)')

    def test_new_reference_cannot_silently_disappear(self):
        (self.skill / 'references/new-topic.md').write_text('# New topic\n')
        with self.assertRaisesRegex(ValueError, 'unregistered'):
            bundle.build_full()

    def test_missing_reference_fails(self):
        (self.skill / 'references/gongwen.md').unlink()
        with self.assertRaisesRegex(ValueError, 'missing'):
            bundle.build_full()

    def test_unrouted_reference_fails(self):
        p = self.skill / 'SKILL.md'
        p.write_text(p.read_text().replace('](references/gongwen.md)', '](#removed)'))
        with self.assertRaisesRegex(ValueError, 'entrypoint'):
            bundle.build_full()

    def test_compact_retains_modes_without_file_routing(self):
        output = bundle.build_compact()
        source = (self.skill / 'SKILL.md').read_text()
        modes = re.findall(r'^### .+', source, re.M)
        for mode in modes:
            self.assertIn(mode, output)
        self.assertNotIn('## 知识库路由', output)
        self.assertNotIn('](references/', output)
        self.assertLessEqual(len(output), bundle.CUSTOM_GPT_LIMIT)


class InstallerTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        self.repo = self.root / 'repo'
        (self.repo / 'scripts').mkdir(parents=True)
        shutil.copy2(ROOT / 'scripts/install.sh', self.repo / 'scripts/install.sh')
        shutil.copytree(ROOT / 'skills', self.repo / 'skills')

    def install(self, dest):
        return subprocess.run(['bash', str(self.repo / 'scripts/install.sh'), str(dest)],
                              capture_output=True, text=True)

    def test_install_and_update_preserve_custom_files_in_backup(self):
        dest = self.root / 'client with spaces'
        self.assertEqual(self.install(dest).returncode, 0)
        (dest / 'kaogong/custom.md').write_text('keep my notes')
        self.assertEqual(self.install(dest).returncode, 0)
        backups = list(Path(str(dest) + '.kaogong-backups').glob('backup.*/kaogong/custom.md'))
        self.assertEqual(len(backups), 1)
        self.assertEqual(backups[0].read_text(), 'keep my notes')
        self.assertTrue((dest / 'kaogong/references/gongwen.md').is_file())
        self.assertFalse(list(dest.glob('.kaogong-stage.*')))

    def test_source_cannot_be_overwritten(self):
        source = self.repo / 'skills/kaogong/SKILL.md'
        before = source.read_bytes()
        self.assertNotEqual(self.install(self.repo / 'skills').returncode, 0)
        self.assertEqual(source.read_bytes(), before)
        self.assertNotEqual(self.install(source.parent / 'nested').returncode, 0)

    def test_existing_symlink_is_backed_up_without_modifying_target(self):
        dest = self.root / 'client'
        dest.mkdir()
        target = self.root / 'custom-skill'
        target.mkdir()
        (target / 'notes.txt').write_text('keep')
        (dest / 'kaogong').symlink_to(target, target_is_directory=True)
        self.assertEqual(self.install(dest).returncode, 0)
        self.assertEqual((target / 'notes.txt').read_text(), 'keep')
        self.assertFalse((dest / 'kaogong').is_symlink())
        backups = Path(str(dest) + '.kaogong-backups')
        self.assertTrue(next(backups.glob('backup.*/kaogong')).is_symlink())


if __name__ == '__main__':
    unittest.main()
