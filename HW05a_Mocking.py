import unittest 
from HW04 import view_repos
from unittest import mock

class TestCase(unittest.TestCase):

    @mock.patch('HW04.view_repos')

    def test_hw04(self, mockAPI):
        mockAPI('fitrepoz').return_value = {'810A': 1, 'http---code.google.com-p-sharpdx-': 2, 'projectxenie': 3, 'sastokes.github.io': 4, 'sharpdx': 2, 'SSW-567': 30, 'SSW-HW02': 2, 'SSW-HW04': 13, 'SSW810GHrepo': 5, 'SSWTeamD': 2}
        self.assertEqual(mockAPI("fitrepoz").return_value, {'810A': 1, 'http---code.google.com-p-sharpdx-': 2, 'projectxenie': 3, 'sastokes.github.io': 4, 'sharpdx': 2, 'SSW-567': 30, 'SSW-HW02': 2, 'SSW-HW04': 13, 'SSW810GHrepo': 5, 'SSWTeamD': 2})

if __name__ == "__main__":
    unittest.main()
