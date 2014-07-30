import handbookof.electronics.resistors as hr
import unittest as ut

class TestDim(ut.TestCase):
##    def setUp(self):
##        pass

    def test_01color(self):
        c1 = hr.resistor_colors(470)
        self.assertEqual(c1, ('Yellow','Violet','Brown'))

    def test_02nearest(self):
        v = 5200
        r20 = hr.nearest_value(v,20)
        r10 = hr.nearest_value(v,10)
        r05 = hr.nearest_value(v,05)
        self.assertEqual(r20,4700)
        self.assertEqual(r10,5600)
        self.assertEqual(r05,5100)
        
    
if __name__ == '__main__':
    ut.main()

