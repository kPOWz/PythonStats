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
        observered_before = data_capture.add(5)
        self.assertEquals(observered_before[data_one], data_one)
        self.assertEquals(observered_before[data_three], data_three)
        self.assertEquals(observered_before[data_five], data_five)
        
        data_capture.build_stats()
        observed_after = data_capture.raw_data;

        self.assertEquals(observed_after[data_one], 0)
        self.assertEquals(observed_after[data_three], 1)
        self.assertEquals(observed_after[data_five], 2)

unittest.main(exit=False)