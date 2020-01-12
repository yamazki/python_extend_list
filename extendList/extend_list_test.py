import unittest
from extend_list import ExtendList

class TestExtendList(unittest.TestCase):
  """test class of extend_list.py
  """
  
  def test_value_of(self):
    extend_list = ExtendList([0,1,2,3,4,5,6])
    expected = [0,1,2,3,4,5,6]
    actual = extend_list.list_value()
    
    self.assertEqual(expected, actual)

  def test_clear(self):
    extend_list = ExtendList([0,1,2,3,4,5,6])
    extend_list.clear()
    expected = []
    actual = extend_list.list_value()
    self.assertEqual(expected, actual)
    
  
  
if __name__ == "__main__":
  unittest.main()
