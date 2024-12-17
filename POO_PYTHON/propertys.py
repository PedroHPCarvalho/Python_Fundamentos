class Foo: 
  def __init__(self,x=None):
    self.__x = x

  @property
  def x(self):
    return self.__x or 0
  
  @x.setter
  def x(self, value):
    self.__x += value
 
  @x.deleter
  def x(self):
    self.__x = -1


  
foo_obj = Foo(10)
print(foo_obj.x)

del foo_obj.x
print(foo_obj.x)

foo_obj.x = 10
print(foo_obj.x)
