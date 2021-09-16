import unittest
from stats import Stats

class LessTest(unittest.TestCase):

    def test_less(self):
        expected_count_integers_less_than_four = len([3])
        stats = Stats([None, None, None,(0,0),(1,1),None, (2,2), None, None, (3,3)], [3,4,6,6,9])
        
        observed = stats.less(4)

        self.assertEqual(observed, expected_count_integers_less_than_four)

    # !!! --- over-time --- !!!
    def test_less_duplicates(self):
        expected_count_integers_less_than_four = len([3,3])
        stats = Stats([None, None, None,(0,1),(2,2),None, (3,3), None, None, (4,4)], [3,3,4,6,9])
        
        observed = stats.less(4)

        self.assertEqual(observed, expected_count_integers_less_than_four)
    
    def test_greater(self):
        expected_count_integers_more_than_four = len([6, 6, 9])

        stats = Stats([None, None, None,(0,1),(2,2),None, (3,4), None, None, (5,5)], [3,3,4,6,6,9])
        
        observed = stats.greater(4)

        self.assertEqual(observed, expected_count_integers_more_than_four)