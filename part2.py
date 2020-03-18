'''
#option 1 for unittesting framework
import unittest



class TestStringMethods(unittest.TestCase):

    def test_sheet(self):
        self.assertEqual(dataset.iloc[0,0],dataset.iloc[0,0])

if __name__ == '__main__':
    unittest.main()
'''

#below is using pytest

from part3colorbands import CalculateOhmValue


def test_answer():
    #check if out of spec returns what it needs to
    #can be changed for other value checks
    assert CalculateOhmValue(4,4,4,20) == "This wire is out of spec, replace wires"    
