class ExtendList(list):
  
  def __init__(self, _list):
    self._list = [] + _list
    
  def __getitem__(self, index):
    return self._list[index]
  
  def __get__(self, instance, owner):
    return self._list
  
  @staticmethod
  def value_of(self, extend_list):
    return extend_list._list.copy()
    
  
  def append(self, value):
    self._list.append(value)
    
  
  def extend(self, iterable):
    self._list.extend(iterable)
    
  
  def insert(self, i, x):
    self._list.insert(i, x)
    
  
  def remove(self, x):
    self._list.remove(x)
  
  
  def pop(self, i=None):
    if(i == None): i = self.size()-1
    return self._list.pop(i)
  
  
  def clear(self):
    self._list.clear()
  
  
  def index(self, x, start, end):
    return self._list.index(x, start, end)
    
  
  def count(self, x):
    return self._list.count(x)
  
  
  def copy(self):
    return ExtendList(self._list)
    
  
  def map(self, func):
    returned_extend_list = ExtendList([])
    for i in range(self.size()):
      returned_extend_list.append(func(self[i]))
    return returned_extend_list
    
  
  def filter(self, func):
    returned_extend_list = ExtendList([])
    for i in range(self.size()):
      if func(self[i]): returned_extend_list.append(self[i]) 
    return returned_extend_list
    
  
  def foreach(self, func):
    for i in range(self.size()):
      func(self[i])
    return self
  
  
  def reduce(self, func):
    accumulator = self[0]
    for i in range(self[i].size()-1):
      accumulator = func(accumu_lator, self[i+1])
    return accumulator
  
  
  def reverse(self):
    returned_extend_list = ExtendList([])
    length = self.size()
    for i in range(length):
      returned_extend_list.append(self[length-1-i])
    return returned_extend_list
    
  
  def d_reverse(self):
    length = self.size()
    for i in range(int(length/2)):
      self._list[i], self._list[length-i-1] = self._list[length-i-1], self._list[i] 
    return self
      
  
  def join(self):
    result = ''
    length = self.size()
    for i in range(length):
      result += str(self[i])
    return result
  
  def sort(self, func=None):
    returned_extend_list = self.copy()
    if(func == None): 
      returned_extend_list._list.sort()
      return returned_extend_list
      
  
  def size(self):
    return len(self._list)
  
  # to output \n
  
  def println(self):
    print()
    return self
  
# Below, test code
  
def add(x):
  return lambda y: x + y

def print_func(x):
  print(x, end='')

if __name__ == "__main__":
  test = ExtendList([1,2,3,4,3,2,1,3])
  test.sort().foreach(print_func).println()
  test.map(lambda x: x + 2).filter(lambda x: x > 3).foreach(print_func).println()
  test2 = ExtendList(["i", "n", "t"])
  print(test2.reverse().join())
  import doctest
  doctest.testmod()
 
  
