import unittest
from extend_list import ExtendList

class TestExtendList(unittest.TestCase):
  """test class of extend_list.py
  """

  def test_clear():
    extend_list = ExtendList([0,1,2,3,4,5,6])
    extend_list.clear(extend_list)
    print(extend_list._list)
    expected = []
    actual = extend_list.value_of(extend_list)
    self.assertEqual(expected, actual)
    
if __name__ == "__main__":
  unittest.main()
