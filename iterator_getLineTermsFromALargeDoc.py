# -*- coding: utf-8 -*-

'''
@file   iterator_getLineTermsFromALargeDoc.py
@author shulong tan (laos1984@gmail.com)
@date   2016-11
@comments  iteratively get line term(s) from a large document, iterator and yield implementation 
'''

# iterator
class getLineTermsofLongDoc(object):
  def __init__(self,file):
    self.file=file

  def __iter__(self):
    return self

  def next(self):
    line=self.file.readline()
    if line:
      terms=line.strip().split('\t')
      if len(terms)==5:
        if terms[4]=="NULL":
          terms[4]=""
        return terms
      else: # skip some bad lines
        print len(terms)
        self.next()
    else: # stop iteration
      raise StopIteration()

#yield
def getLineTermsofLongDoc(fpath):
  f=open(fpath,'rb')
  for line in f:
    terms=line.strip().split('\t')
    if len(terms)!=5:#skip bad lines as normal functions
      continue
    if terms[4]=="NULL":
      terms[4]=""
    yield terms #no return


if __name__ == '__main__':
  fpath='test.txt'
  
  #for iterator
  with open(fpath,'rb') as f:
    for idx, terms in enumerate(getLineTermsofLongDoc(f)):
      print idx
      print terms
  
  #for yield
  for idx, terms in enumerate(getLineTermsofLongDoc(fpath)):
    print idx
    print terms



