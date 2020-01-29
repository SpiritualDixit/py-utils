def getClassTree(cls):
  """Gets the heirarchy of class inheritence.
  
  Params:
  cls (object): The name of the class.
  
  Example:
  from class_tree import getClassTree as ct
  
  class A: pass
  class B(A): pass
  class C(A): pass
  class D(B): pass
  class E(B, D): pass
  
  print ct(E)
  """
  if not hasattr(cls, '__bases__'):
    raise Exception('{} is not a valid class'.format(cls))
  bases = cls.__bases__
  name = cls.__name__

  if not len(bases):
    return name + '(Root)'

  return name + '\t\n'.join(['  <-- {}'.format(getClassTree(base)) for base in bases])
  
