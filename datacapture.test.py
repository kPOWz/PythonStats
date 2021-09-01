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
        self.assertEquals(data_to_capture, observed[data_to_capture])
    
    def test_add_int_more_than_once(self):
        data_to_repeat = 3;
        expected_summed_value_of_repeated_int = 3 + 3 + 3;
        data_capture = DataCapture()      
        
        data_capture.add(data_to_repeat)
        data_capture.add(4)
        data_capture.add(7)
        data_capture.add(data_to_repeat)  
        observed = data_capture.add(data_to_repeat)

        self.assertEquals(observed[data_to_repeat], expected_summed_value_of_repeated_int)

class BuildStatsTest(unittest.TestCase):

    def test_build_stats_matches_added(self):
        data_capture = DataCapture()
        data_capture.add(1)
        data_capture.add(1000)
        
        observed = data_capture.build_stats()
        self.assertEquals(observed, [1, 1000])
    
    def test_build_stats_records_lookup_indicies(self):
        data_one = 1;
        data_three = 3;
        data_five = 5;
        data_capture = DataCapture()
        data_capture.add(data_one)
        data_capture.add(data_three)
        data_capture.add(data_five)
        
        data_capture.build_stats()
        observed = data_capture.raw_data;

        self.assertEquals(observed[data_one], (0,0))
        self.assertEquals(observed[data_three], (1,1))
        self.assertEquals(observed[data_five], (2,2))

class LessTest(unittest.TestCase):

    def test_less(self):
        expected_count_integers_less_than_four = len([3])
        data_capture = DataCapture()
        data_capture.add(9)
        data_capture.add(3)
        data_capture.add(4)
        data_capture.add(6)
        data_capture.build_stats()
        
        observed = data_capture.less(4)

        self.assertEquals(observed, expected_count_integers_less_than_four)

    # !!! --- over-time --- !!!
    def test_less_duplicates(self):
        expected_count_integers_less_than_four = len([3,3])
        data_capture = DataCapture()
        data_capture.add(3)
        data_capture.add(9)
        data_capture.add(3)
        data_capture.add(4)
        data_capture.add(6)
        data_capture.build_stats()
        
        observed = data_capture.less(4)

        self.assertEqual(observed, expected_count_integers_less_than_four)

unittest.main(exit=False)