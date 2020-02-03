#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import print_function
CHAR_LT = '├── '
CHAR_L = '└── '
CHAR_PIPE = '│   '


class ClassTree(object):
  """Gets the class tree of inheritence.
  
  class A: pass
  class B: pass
  class C(A): pass
  class D(B): pass
  class E(D): pass
  class F(C, E): pass
  x = ClassTree(F)
  x.getRootClass().printChilds()
  """
  _classes = {}
  def __init__(self, cls, useHistory=False):
    if not hasattr(cls, '__bases__'):
      raise Exception('{} is not a valid class'.format(cls))
    self.counter = 0
    self.name = cls.__name__
    self.children = []
    self._classes = {}
    self.parents = []
    if not useHistory:
      self.__class__._classes = {}
    self.prepareParents(cls)

  def getRootClass(self):
    if not self.__class__._classes:
      return None
    for cls in self.__class__._classes.values():
      if not cls.getParent():
        return cls
    return None

  def getChildren(self):
    return self.children

  def getParent(self):
    return self.parents

  def addParent(self, parentClass):
    self.parents.append(parentClass)

  def addChild(self, childClass):
    self.children.append(childClass)

  def __iter__(self):
    self.counter = 0
    return self

  def next(self):
    if self.counter >= len(self.children):
      raise StopIteration
    child = self.children[self.counter]
    self.counter += 1
    return child

  def getName(self):
    return self.name

  def prepareParents(self, cls):
    parents = cls.__bases__
    if not parents and self.name != object.__name__:
      parents = (object, )
    for parent in parents:
      clsName = parent.__name__
      if clsName in self.__class__._classes:
        parentClass = self.__class__._classes[clsName]
      else:
        parentClass = ClassTree(parent, True)
        self.__class__._classes[clsName] = parentClass
      parentClass.addChild(self)
      self.addParent(parentClass)

  def printChilds(self, prefix='', level=0):
    childsLen = len(self.children)
    name = self.name
    if level == 0:
      print(name)
    for index, child in enumerate(self.children):
      cname = child.name
      if index == childsLen - 1:
        print(prefix + CHAR_L + cname)
        if child.children:
          child.printChilds(prefix + "    ", level +1)
      else:
        print(prefix + CHAR_LT + cname)
        if child.children:
          child.printChilds(prefix + CHAR_PIPE, level + 1)



ClassTree.__next__ = ClassTree.next # For Python 3 compatibility
