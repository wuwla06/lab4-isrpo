import unittest

def perimeter(a,b):
    return (a+b)*2

def square(a,b):
    return a*b

class RectangleTestCase(unittest.TestCase):
    def testZeroMul(self):
        res = square(10, 0)
        self.assertEqual(res, 0)

    def testSquareMul(self):
        res = square(10, 10)
        self.assertEqual(res, 100)

    def testPerimeter(self):
        res = perimeter(10, 1)
        self.assertEqual(res, 22)

if __name__ == "__main__":
    unittest.main()
