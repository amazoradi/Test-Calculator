import unittest
import sys
sys.path.append('../')
from calculator import Calculator

def setUpModule():
  print('set up module')

def tearDownModule():
  print('tear down module')

class TestCalculator(unittest.TestCase):

  @classmethod
  def setUpClass(self):
    print('Set up class')
    self.calc = Calculator()

  @classmethod
  def tearDownClass(self):
    print('Tear down class')
  


  def test_add(self):
    self.assertEqual(self.calc.add(2, 7), 9)
    self.assertEqual(self.calc.add(-1, 1), 0)
    print(self.calc.add(2, 7), "= 2+7")
    print(self.calc.add(-2, 7), "= -2+7")
  
  def test_subtract(self):
    self.assertEqual(self.calc.subtract(10,2), 8)
    print("10-2 =",self.calc.subtract(10,2))
    self.assertEqual(self.calc.subtract(-10, 2), -12)
    self.assertEqual(self.calc.subtract(-10, -2), -8)

  def test_multiply(self):
    self.assertEqual(self.calc.multiply(10,2), 20)
    print("10*2 =",self.calc.multiply(10,2))
    self.assertEqual(self.calc.multiply(-10, 2), -20)
    self.assertEqual(self.calc.multiply(-10, -2), 20)

  def test_divide(self):
    self.assertEqual(self.calc.divide(10,2), 5)
    print("10/2 =",self.calc.divide(10,2))
    self.assertEqual(self.calc.divide(-10, 2), -5)
    self.assertEqual(self.calc.divide(-10, -2), 5)
    self.assertEqual(self.calc.divide(-10, 4), -2.5)
  

if __name__ == '__main__':
    unittest.main()