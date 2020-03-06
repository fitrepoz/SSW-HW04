import unittest
from HW04 import view_repos


class TestCase(unittest.TestCase):

    def test_hw04(self):
        self.assertEqual(view_repos("fitrepoz"), {'810A': 1, 'http---code.google.com-p-sharpdx-': 2, 'projectxenie': 3, 'sastokes.github.io': 4, 'sharpdx': 2, 'SSW-567': 30, 'SSW-HW02': 3, 'SSW-HW04': 13, 'SSW810GHrepo': 5, 'SSWTeamD': 2})

if __name__ == "__main__":
    unittest.main()
