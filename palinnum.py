#!/usr/bin/python
import sys
import math

def determinPail(x):
   a = str(x)[::-1]
   print('rev Number:%s'%(a))
   if(x == int(a)):
      print(True)
   else: 
      print(False)

def main():
   x = input('Input number:')
   print('Num:%d'%(x))
   determinPail(x)

if __name__ == '__main__':
   main()
