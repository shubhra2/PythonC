class A:
  def __init__(self, a1, a2):
    self._a1 = a1
    self._a2 = a2
  
  def print(self):
    print(self._a1, self._a2)

class B:
  def __init__(self, b1, b2):
    self._b1 = b1
    self._b2 = b2

  def print(self):
    print(self._b1, self._b2)
class C(A,B):
  def __init__(self, a1, a2, b1, b2):
    A.__init__(self, a1, a2)
    B.__init__(self, b1, b2)

class D(B, A):
  def __init__(self, a1, a2, b1, b2):
    A.__init__(self, a1, a2)
    B.__init__(self, b1, b2)
  
  def print(self):
    print('Print call from Class D : ')
    A.print(self)
    B.print(self)

  
c1 = C(1,2, 3,4)
c1.print()
  
d1 = D(1,2, 3,4)
d1.print()