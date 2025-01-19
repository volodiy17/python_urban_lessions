import unittest

from tests_12_3 import TournamentTest, RunnerTest

suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(RunnerTest))
suite.addTest(unittest.makeSuite(TournamentTest))

if __name__ == "__main__":
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)
