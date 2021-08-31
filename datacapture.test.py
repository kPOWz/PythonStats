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


unittest.main(exit=False)