import unittest, os

class Example(unittest.TestCase):
    @classmethod
    def setUp(self):
        self.branch = os.getenv("GIT_BRANCH")

    def test_branch(self):
        self.assertEqual(self.branch, "pipelines")