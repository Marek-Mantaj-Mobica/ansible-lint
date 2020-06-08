import unittest
from ansiblelint import RulesCollection
from ansiblelint.runner import Runner
from ansiblelint.rules.UseCommandInsteadOfShellRule import UseCommandInsteadOfShellRule


class TestUseCommandInsteadOfShell(unittest.TestCase):
    collection = RulesCollection()

    def setUp(self):
        self.collection.register(UseCommandInsteadOfShellRule())

    def test_file_positive(self):
        success = 'test/command-instead-of-shell-success.yml'
        good_runner = Runner(self.collection, success, [], [], [])
        self.assertEqual([], good_runner.run())

    def test_file_negative(self):
        failure = 'test/command-instead-of-shell-failure.yml'
        bad_runner = Runner(self.collection, failure, [], [], [])
        errs = bad_runner.run()
        self.assertEqual(2, len(errs))
