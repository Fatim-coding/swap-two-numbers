def swap(a,b):
  a = a^b
  b = a^b
  a = a^b
  print("After swapping: a =",a,"and b =",b)

def swap2(a,b):
  a = (a&b)+(a|b)
  b = a+(~b)+1
  a = a+(~b)+1
  print("After swapping: a =",a,"and b =",b)

swap(3,80)
swap2(3,80)
  

