import unittest
from datacapture import DataCapture

class AddTest(unittest.TestCase):

    def test_add(self):
        data_capture = DataCapture()
        data_capture.add();
        self.assertTrue(False)    


unittest.main(exit=False)