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
        with self.assertRaises(ValueError):
            add(0,sqrt(-1), sqrt(-1))
        self.assertAlmostEqual(add(3,5j), 3+5j)
        #test string
        self.assertEqual(add("Hey","There"), "HeyThere")
        #test boolean
        self.assertRaises(TypeError, add, False, False)

    def test_subtract(self):
        self.assertEqual(subtract(111,11), 100)
        self.assertEqual(subtract(100,-1), 101)
        self.assertEqual(subtract(-1, 100), -101)
        self.assertAlmostEqual(subtract(0,15), -15)
        self.assertAlmostEqual(subtract(15, 0), 15)
        #self.assertAlmostEqual((3,12j),3-12j)
        #self.assertAlmostEqual((12j,-3), -3+12j)     

        with self.assertRaises(TypeError):
            #test string
            subtract("Bye", "Now"), "NowBye"
            #test boolean
            subtract(False, True), -True

    def test_multiple(self):
        self.assertEqual(multiply(100, 50), 5000)
        self.assertEqual(multiply(-3,21), -63)
        self.assertEqual(multiply(-1, -75), 75)

        with self.assertRaises(TypeError):
            #test string
            multiply("Where", "Now"), "NowWhere"
            #test boolean
            multiply(False, True), False
            #test combination
            multiply("Hey ", 4), "Hey Hey Hey Hey "
        

    def test_divide(self):
        self.assertEqual(divide(5,1), 5)
        self.assertEqual(divide(2, 5), 0.40)
        with self.assertRaises(ValueError):
            divide(10,0)
        self.assertRaises(TypeError, divide, "4", "3")
        self.assertRaises(TypeError, divide, False, False)


if __name__=='__main__':
    unittest.main()
