import unittest
#from functionz import add, subtract, multiply, divide, containMethod1, containMethod2
from functionz import *
#from math import *



class Testfunctionz(unittest.TestCase):
    def test_add(self):
        #test real numbers
        self.assertAlmostEqual(add(5,3), 8)
        self.assertAlmostEqual(add(6.102,1.101), 7.203)
        self.assertEqual(add(1,3),4)
        self.assertEqual(add(0,4),4)
        self.assertEqual(add(5,0), 5)
        self.assertAlmostEqual(add(-1,-2), -3)
        self.assertAlmostEqual(add(-5,5), 0)
        self.assertAlmostEqual(add(-200,1000), 800)
        #test imaginary numbers
        #self.assertAlmostEqual(add(0,sqrt(-1), sqrt(-1)))
        #self.assertAlmostEqual(add(3,5j), 3+5j)
        #test string
        self.assertRaises(TypeError, divide, "4", "3")
        #self.assertRaises(TypeError, add, "Wow", "Hey")
        #self.assertRaises(TypeError, add, 4,3)
        #self.assertRaises(TypeError, add, False, False)

    def test_divide(self):
        self.assertEqual(divide(5, 1), 5)
        with self.assertRaises(ValueError):
            divide(10,0)


if __name__=='__main__':
    unittest.main()
