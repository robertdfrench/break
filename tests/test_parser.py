import unittest
import breakable


class TestParser(unittest.TestCase):
    def test_list_tasks(self):
        args = breakable._get_args(["-l"])
        self.assertTrue(args.list_tasks)

    def test_breakfile_default(self):
        args = breakable._get_args([])
        self.assertEqual(args.breakfile, "Breakfile.py")

    def test_set_breakfile(self):
        args = breakable._get_args(["-f", "Dummy.py"])
        self.assertEqual(args.breakfile, "Dummy.py")

    def test_set_task(self):
        args = breakable._get_args(["-t", "crapola"])
        self.assertEqual(args.task, "crapola")

    def test_default_task_is_none(self):
        args = breakable._get_args([])
        self.assertIsNone(args.task)
