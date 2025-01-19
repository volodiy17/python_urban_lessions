import unittest

from runner_and_tournament import Tournament, Runner


def check_frozen(func):
    def wrapper(self, *args, **kwargs):
        if self.is_frozen:
            self.skipTest("Тесты в этом кейсе заморожены")
        return func(self, *args, **kwargs)

    return wrapper


class TournamentTest(unittest.TestCase):
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.runner_usain = Runner(name="Usain", speed=10)
        self.runner_andrey = Runner(name="Andrey", speed=9)
        self.runner_nick = Runner(name="Nick", speed=3)

    @classmethod
    def tearDownClass(cls):
        for test_name, result in cls.all_results.items():
            print(f"{result}")

    @check_frozen
    def test_usain_and_nick(self):
        tournament = Tournament(90, self.runner_usain, self.runner_nick)
        result = tournament.start()
        self.__class__.all_results["test_usain_and_nick"] = result
        self.assertEqual(result.get(2), "Nick")

    @check_frozen
    def test_andrey_and_nick(self):
        tournament = Tournament(90, self.runner_andrey, self.runner_nick)
        result = tournament.start()
        self.__class__.all_results["test_andrey_and_nick"] = result
        self.assertEqual(result.get(2), "Nick")

    @check_frozen
    def test_usain_andrey_and_nick(self):
        tournament = Tournament(90, self.runner_usain, self.runner_andrey, self.runner_nick)
        result = tournament.start()
        self.__class__.all_results["test_usain_andrey_and_nick"] = result
        self.assertEqual(result.get(3), "Nick")


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @check_frozen
    def test_walk(self):
        runner = Runner("Walker")
        for _ in range(10):
            runner.walk()
        self.assertEqual(runner.distance, 50, "Distance after walking 10 times should be 50.")

    @check_frozen
    def test_run(self):
        runner = Runner("Runner")
        for _ in range(10):
            runner.run()
        self.assertEqual(runner.distance, 100, "Distance after running 10 times should be 100.")

    @check_frozen
    def test_challenge(self):
        runner1 = Runner("Runner1")
        runner2 = Runner("Runner2")

        for _ in range(10):
            runner1.run()
            runner2.walk()

        self.assertNotEqual(runner1.distance, runner2.distance,
                            "Distances should not be equal when one runs and the other walks.")
