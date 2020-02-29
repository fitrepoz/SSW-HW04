import unittest

from HW04 import view_repos

class TestHW(unittest.TestCase):

    def test_github_api(self):
        self.assertEqual(view_repos('fitrepoz'),['Repo:810A Number of commits: 1',
        'Repo:http---code.google.com-p-sharpdx- Number of commits: 2', 
        'Repo:projectxenie Number of commits: 3', 
        'Repo:sastokes.github.io Number of commits: 4', 
        'Repo:sharpdx Number of commits: 2', 
        'Repo:SSW-567 Number of commits: 10', 
        'Repo:SSW810GHrepo Number of commits: 5', 
        'Repo:SSWTeamD Number of commits: 2'])


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)