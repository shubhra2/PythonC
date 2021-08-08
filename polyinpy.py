class Cat:
  def __init__(self, name, age):
    self.__name = name
    self.__age  = age
  
  def get_name(self):
    print('Name of cat is {}'.format(self.__name))
  
  def get_age(self):
    print('Age of {} is {}'.format(self.__name, self.__age))

  def speak(self):
    print('Maow...')

  def type(self):
    print('Cat')
class Dog:
  def __init__(self, name, age):
    self.__name = name
    self.__age  = age

  def get_name(self):
    print("Name of Dog is {}".format(self.__name))

  def get_age(self):
    print("Age of {} if {}".format(self.__name, self.__age))

  def speak(self):
    print("Bhow Bhow...")

  def type(self):
    print('Dog')
def get_info(obj):
  print('Type of obj is : {}'.format(type(obj)))
  obj.get_name()
  obj.get_age()
  obj.speak()
  obj.type()

c = Cat('Kitty', 2)
d = Dog('Sheru', 3)

print('Information of Cat :')
get_info(c)
print('Information of Dog')
get_info(d)