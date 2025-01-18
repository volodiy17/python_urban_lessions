import unittest

from runner_and_tournament import Tournament, Runner


class TournamentTest(unittest.TestCase):
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

    def test_usain_and_nick(self):
        tournament = Tournament(90, self.runner_usain, self.runner_nick)
        result = tournament.start()
        self.__class__.all_results["test_usain_and_nick"] = result
        self.assertEqual(result.get(2), "Nick")

    def test_andrey_and_nick(self):
        tournament = Tournament(90, self.runner_andrey, self.runner_nick)
        result = tournament.start()
        self.__class__.all_results["test_andrey_and_nick"] = result
        self.assertEqual(result.get(2), "Nick")

    def test_usain_andrey_and_nick(self):
        tournament = Tournament(90, self.runner_usain, self.runner_andrey, self.runner_nick)
        result = tournament.start()
        self.__class__.all_results["test_usain_andrey_and_nick"] = result
        self.assertEqual(result.get(3), "Nick")


if __name__ == "__main__":
    unittest.main()
