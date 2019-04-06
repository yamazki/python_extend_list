class extend_list(list):
  _list = []

  def __init__(self, _list):
    self._list = [] + _list
    
  def __getitem__(self, index):
    return self._list[index]
  
  def __get__(self, instance, owner):
    return self._list
    
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
  
  
  # def sort(self, key=None, reverse=False):
  #   return extend_list([self._list.sort(key, reverse)])
    
  def copy(self):
    return extend_list([self._list.copy()])
    
  def map(self, func):
    new_list = extend_list([])
    for i in range(self.size()):
      new_list.append(func(self[i]))
    return new_list
    
  def filter(self, func):
    new_list = extend_list([])
    for i in range(self.size()):
      if func(self[i]): new_list.append(self[i]) 
    return new_list
    
  def foreach(self, func):
    for i in range(self.size()):
      func(self[i])
  
  def reduce(self, func):
    accumulator = self[0]
    for i in range(self[i].size()-1):
      accumulator = func(accumu_lator, self[i+1])
    return accumulator
  
  def reverse(self):
    new_list = extend_list([])
    length = self.size()
    for i in range(length):
      new_list.append(self[length-1-i])
    return new_list
    
  def dreverse(self):
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
  
  def sort(self, func):
    n =1
    
  def size(self):
    return len(self._list)
  
# Below, test code
  
def add(x):
  return lambda y: x + y

def print_func(x):
  print(x, end='')

if __name__ == "__main__":
  test = extend_list([1,2,3,4])
  test.append(4)
  print(test.pop())
  test.map(lambda x: x + 2).filter(lambda x: x > 3).foreach(print_func)
  test2 = extend_list(["i", "n", "t"])
  print(test2.reverse().join())
 
  
