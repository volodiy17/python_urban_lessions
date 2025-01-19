import logging
import unittest

from rt_with_exceptions import Runner

logging.basicConfig(
    level=logging.INFO,
    filename='runner_tests.log',
    filemode='w',
    encoding='utf-8',
    format='%(levelname)s: %(message)s'
)


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        try:
            runner = Runner("Walker", speed=-5)
            for _ in range(10):
                runner.walk()
            self.assertEqual(runner.distance, 50, "Distance after walking 10 times should be 50.")
            logging.info('"test_walk" выполнен успешно')
        except ValueError as e:
            logging.warning("Неверная скорость для Runner: %s", e)

    def test_run(self):
        try:
            runner = Runner(12345)
            for _ in range(10):
                runner.run()
            self.assertEqual(runner.distance, 100, "Distance after running 10 times should be 100.")
            logging.info('"test_run" выполнен успешно')
        except TypeError as e:
            logging.warning("Неверный тип данных для объекта Runner: %s", e)

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
