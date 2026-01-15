import time as t
import math as m
import numpy as np
import exercises as e

class Exercises:
    def __init__(self):
         pass 
    def ex1(self,a,b,c):
         return e.quadratic_fun(a,b,c)
    def ex2(self,N):
        return e.recaman(N)
    def ex3(self,list):
        return e.reverse(list)
    def ex4(self,list1,list2):
        return e.intersection(list1,list2)
    def ex5(self,N):
        return e.pairs(N)
    def ex6(self):
        return e.comparing()
    def ex7(self,word):
        return e.palindrome(word)
    def ex8(self,string):
        return e.maximum_occurences(string)
    def ex9(self,N):
        return e.primes(N)
class complex:
    def __init__(self,r = 0,i = 0):
        self.r = r 
        self.i = i
    def __add__(self,other):
        r = self.r + other.r
        i = self.i + other.i
        return complex(r,i)
    def __sub__(self,other):
        r = self.r-other.r
        i = self.i - other.i
        return complex(r,i)
    def __mul__(self,other):
        r = self.r * other.r - self.i * other.i
        i = self.r*other.i + self.i*other.i
        return complex(r,i)
    def __truediv__(self,other): #a b c -d
        m = other.r**2 + other.i**2
        r = (self.r*other.r + self.i * other.i)/m
        i = (self.r*other.i - self.i*other.i)/m
        return complex(r,i)
    def __str__(self):
        return "Complex number:({0},{1})".format(self.r,self.i)
    def modulus(self):
        result = m.sqrt(abs(self.r**2 + self.i**2))
        return result
class MyMatrix:
    def __init__(self,N):
        self.data = np.random.rand(N,N)
        self.dimension = N
    def inverse(self):
        return np.linalg.inv(self.data)
    def determinant(self):
        return np.linalg.det(self.data)
    def eigenvalues(self):
        return np.linalg.eig(self.data)
    def __add__(self,other):
        return self.data + other.data
    def __mul__(self,other):
        return self.data * other.data

