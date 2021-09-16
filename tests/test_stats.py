import unittest
from stats import Stats

class StatsTest(unittest.TestCase):

    def test_less(self):
        expected_count_integers_less_than_four = len([3])
        stats = Stats([None, None, None,(0,0),(1,1),None, (2,2), None, None, (3,3)], 5)
        
        observed = stats.less(4)

        self.assertEqual(observed, expected_count_integers_less_than_four)

    # !!! --- over-time --- !!!
    def test_less_duplicates(self):
        expected_count_integers_less_than_four = len([3,3])
        stats = Stats([None, None, None,(0,1),(2,2),None, (3,3), None, None, (4,4)], 5)
        
        observed = stats.less(4)

        self.assertEqual(observed, expected_count_integers_less_than_four)
    
    def test_greater(self):
        greater_array = [6, 6, 9];
        expected_count_integers_more_than_four = len(greater_array)
        given_lookup_array = [None, None, None,(0,1),(2,2),None, (3,4), None, None, (5,5)];
        given_condensed_array_length = len([3,3,4] + greater_array);
        stats = Stats(given_lookup_array, given_condensed_array_length)
        
        observed = stats.greater(4)

        self.assertEqual(observed, expected_count_integers_more_than_four)
    
    def test_between(self):
        between_array = [2,3,3,4,6]
        expected_count_integers_between = len(between_array)
        given_lookup_array = [None, None, (0,0), (1,2), (3,3), None, (4,4), None, None, (5,6)]
        # given_condensed_array = between_array + [9,9];
        stats = Stats(given_lookup_array, 6)
        
        observed = stats.between(2,6)

        self.assertEqual(observed, expected_count_integers_between)