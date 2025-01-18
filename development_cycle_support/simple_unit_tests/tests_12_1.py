import unittest

from runner import Runner


class RunnerTest(unittest.TestCase):

    def test_walk(self):
        runner = Runner("Walker")
        for _ in range(10):
            runner.walk()
        self.assertEqual(runner.distance, 50, "Distance after walking 10 times should be 50.")

    def test_run(self):
        runner = Runner("Runner")
        for _ in range(10):
            runner.run()
        self.assertEqual(runner.distance, 100, "Distance after running 10 times should be 100.")

    def test_challenge(self):
        runner1 = Runner("Runner1")
        runner2 = Runner("Runner2")

        for _ in range(10):
            runner1.run()
            runner2.walk()

        self.assertNotEqual(runner1.distance, runner2.distance,
                            "Distances should not be equal when one runs and the other walks.")


if __name__ == "__main__":
    unittest.main()
