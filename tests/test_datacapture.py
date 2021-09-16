import unittest
from datacapture import DataCapture

class AddTest(unittest.TestCase):

    def test_add(self):
        data_to_capture = 999;
        data_capture = DataCapture()
        
        observed = data_capture.add(data_to_capture)
        self.assertIn(data_to_capture, observed)
    
    def test_add_int_at_corresponding_index(self):
        data_to_capture = 1000;
        data_capture = DataCapture()
        
        observed = data_capture.add(data_to_capture)
        self.assertEqual(data_to_capture, observed[data_to_capture])
    
    def test_add_int_more_than_once(self):
        data_to_repeat = 3;
        expected_summed_value_of_repeated_int = 3 + 3 + 3;
        data_capture = DataCapture()      
        
        data_capture.add(data_to_repeat)
        data_capture.add(4)
        data_capture.add(7)
        data_capture.add(data_to_repeat)  
        observed = data_capture.add(data_to_repeat)

        self.assertEqual(observed[data_to_repeat], expected_summed_value_of_repeated_int)

class BuildStatsTest(unittest.TestCase):

    def test_build_stats_matches_added(self):
        data_capture = DataCapture()
        data_capture.add(1)
        data_capture.add(1000)
        
        data_capture.build_stats()

        # this will not be observed will be self.
        # self.assertEqual(observed, [1, 1000])
        self.assertEqual(data_capture.raw_data_ascending_condensed, [1, 1000])

    
    def test_build_stats_records_lookup_indicies(self):
        data_one = 1;
        data_three = 3;
        data_five = 5;
        data_capture = DataCapture()
        data_capture.add(data_one)
        data_capture.add(data_three)
        data_capture.add(data_five)
        
        observed_stats = data_capture.build_stats()

        # how to not bleed into stats?  can't mock init or new, let it call through? 
        # __init__ and __new__ not supported by Mock/MagicMock
        # https://docs.python.org/dev/library/unittest.mock.html#mocking-magic-methods
        # assert assert_called_once_with('foo')
        self.assertEqual(observed_stats.min_max_population_array[data_one], (0,0))
        self.assertEqual(observed_stats.min_max_population_array[data_three], (1,1))
        self.assertEqual(observed_stats.min_max_population_array[data_five], (2,2))

class FullChallengeTest(unittest.TestCase):

    def test_full_challenge(self):
        capture = DataCapture()
 
        # [KZB] the add function impl worst case is O(1) according to https://www.python.org/dev/peps/pep-3128/#motivation  (set item)
        capture.add(3)
        capture.add(9)
        capture.add(3)
        capture.add(4)
        capture.add(6)
        
        # [KZB] 
        # the build_stats function impl worst case is O(n)
        stats = capture.build_stats()
        
        # [KZB] the less function impl worst case is O(1) according to https://www.python.org/dev/peps/pep-3128/#motivation  (get item)
        less_result = stats.less(4) # should return 2 (only two values 3, 3 are less than 4)
        self.assertEqual(less_result, 2)
        
        # [KZB] incomplete can use same "lookup tuples" as less to achieve worst case O(1) according to https://www.python.org/dev/peps/pep-3128/#motivation  (get item)
        # stats.between(3, 6) # should return 4 (3, 3, 4 and 6 are between 3 and 6)
        
        # [KZB] incomplete can use same "lookup tuples" as less to achieve worst case O(1) according to https://www.python.org/dev/peps/pep-3128/#motivation  (get item)
        # stats.greater(4) # should return 2 (6 and 9 are the only two values greater than 4)

# unittest.main(exit=False)