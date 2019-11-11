# x = input('Please enter your income:')
# y = input('Please enter your extra income:')
# z = int(x)+int(y)
# print(z)
# result = eval(input('please enter a char'))
# print(result)
# x = 3
# r = x %2
# if (r == 0):
#     print('Even')
#     if x>5:
#         print('Great')
#     else:
#         print('Low')
# else:
#     print("Odd")
# print("Bye")
# x =int(input('Please enter a number between 1 to 5 : '))
# if (x==1):
#     print('one')
# elif (x == 2):
#     print('Two')
# elif (x == 3):
#     print('Three')
# elif (x == 4):
#     print('Four')
# elif (x == 5):
#     print('Five')
# else:
#     print('You entered the wrong number...')
# i = 1
# while i<=5:
#     print('Feras', end=' ')
#     j = 1
#     while j<=4:
#         print('Daoud', end=' ')
#         j=j+1
#     i+=1
#     print()
#
# for i in range(20):
#     if (i%2!=0):
#         print(i)
# av =10
# x = int(input('How many candies you want: '))
#
# i = 1
# while i <= x:
#     if i>av:
#         print('out of stock')
#         break
#     print('candy')
#     i+=1
# print('bye')
# for i in range(1,101):
#     if i%3==0 or i%5==0:
#         continue
#     print(i,end=' ')
#
# print('bye')
# for i in range(1,101):
#     if i%2!=0:
#         pass
#     else:
#         print(i)
# print('bye')
# for i in range(5):
#     if i == 3:
#         pass
#     print('Hi', i)
# for i in range(1,4):
#     print('# # # #')
# print()

# for c in range(4):
#     for j in range(4-c):
#         print('#', end=' ')
#     print()
# nums = [2,3,96,22,55,32,0,33,62]
# for num in nums:
#     if num %2==0:
#         print(num)
#         break
# else:
#     print('Not found')
# num = 100
# for i in range(0,num):
#     if i% 2==0:
#         print('even number: ',i)
#     else:
#         print('odd number: ',i)
# from array import *

# vals = array('f',[5,9,2,5,-8,7])
# print(vals.buffer_info())
# for i in range(len(vals)):
#     print(vals[i])
#
# vals2 = array('u',['f','a','g','h'])
# for e in vals2:
#     print(e)
#
# vals3 = array('i',[1,3,5,49,67,6,4,1,2])
# for i in range(len(vals3)):
#     print(vals3[i])
#
# arr = array('i',[])
# n = int(input('Enter the length of the array:'))
# for i in range(n):
#     x = int(input('Please enter the next value: '))
#     arr.append(x)
# print(arr)
# from numpy import *
# arr1 = array([2,3,5,6,4,9,9,8,])
# print(arr1)

# arr = array([12,3,5,6])
# print(arr)
# from numpy import *
# arr = linspace(0,16,2)
# print(arr)
#
# arr1 = logspace(1,40,40)
# print(arr1)
#
# arr3 = zeros(5)
# print(arr3)
#
# arr2 = ones(5)
# print(arr2)
#
# arr4 = array([1,2,3,4,5])
# arr4=arr4+5
# print(arr4)
#
# arr5 = array([1,3,46,6,4,5])
# arr6 = arr5.copy()
#
# print(arr5,arr6)
# print(id(arr6),id(arr5))
# from numpy import *
# arr1 = array([
#         [2,3,5,5,6,7],
#         [6,3,5,4,3,4]
# ])
# arr2 = arr1
# arr3 = arr2.flatten()
# arr4 = arr3.reshape(2,2,3)
# print(arr1,'\n')
# print(arr2)
# print(arr3)
# print(arr4)
# m = matrix('4 2 7 3 ; 5 3 6 6; 5 3 6 5')
# m1 = matrix('4 2 7 3 ; 5 3 6 6; 5 3 6 5')
# m2=m + m1
# # print(m2)
# def update(last):
#     print(id(last))
#     last[1]=25
#     print(id(last))
#     print('x',last)
#
# last =[10, 20, 30]
# print(id(last))
# update(last)
# print('last', last)
# def add(*b):
#     print(b)
#     c = 0
#     for i in b:
#         c = c+i
#         c+=1
#         print(c)
#
# add(4,5,7,35,6)
# def person(name, age):
#     print(name)
#     print(age)
# person('Feras', 25)
# def person(**b):
#     print(b)
#     for i,j in b.items():
#         print(i,j)
# person(name='Feras', age =28 , family = 'Daoud',number = 774928000)
#scope
# a = 10
# def something():
#     a = 12
#     print('local variable ',a)
#     x = globals()['a']
#     print(id(x),x)
# something()
# print(id(a),a)
#list in function
# def count (list):
#     even =0
#     odd =0
#     for i in list:
#         if i%2 == 0:
#             even+=1
#         else:
#             odd+=1
#     print(even,odd)
# list= [24,35,3,4,65,89,5,6,56,4,21,30]
# count(list)
# print()
# print('Please enter your father name:')
# names=[input()for i in range(5)]
# def nameCount(names):
#     return sum(1 for i in names if len(i) >5)
# print(nameCount(names))
#Fibonacci sequence
# def fib(n):
#     a = 0
#     b = 1
#     if n == 1:
#         print(a)
#     elif n<0:
#         print('Please enter a valid value..')
#     else:
#         print(a)
#         print(b)
#         for i in range(2,n):
#             c= a+b
#             a=b
#             b=c
#             if c > 100:
#                 break
#             print(c)
# fib(100)
# factorial number
# print('please enter a number: ')
# n = int(input())
# def fact(n):
#     f = 1
#     for i in range(1,n+1):
#         f = f * i
#     return f
# result = fact(n)
# print(result)
# recurrsion
# import  sys
# sys.setrecursionlimit(2000)
# print(sys.getrecursionlimit())
# i = 1
# def greet():
#     global i
#     i +=1
#     print('Hello', i)
#     greet()
#
# greet()
#factorial using recursion
# import sys
# print('Please enter an integer number: ')
# n = int(input())
# def fact(n):
#     if n== 0:
#         return 1
#     return n*fact(n-1)
# result = fact(n)
# print(result)
# lamabda in python(Anonymous Function)
# f = lambda a :a*a
# result = f(5)
# print(result)
# x = lambda c,d : c+d
# result1 = x
# print(x(2,5))
#filter(), map(), reduce()
# from functools import reduce
# nums = [2,3,5,4,6,45,8,23,24,10]
# evens = list(filter(lambda n : n%2==0,nums))
# print(evens)
#
# doubles = list(map(lambda a:a*a, nums))
# print(doubles)
#
# sums = reduce(lambda c,b:c+b ,nums)
# print(sums)
#Decorators
# def div(a,b):
#     print(a/b)
#
# def smart_div(func):
#
#     def inner(a,b):
#         if a<b:
#             a,b=b,a
#         return func(a,b)
#     return inner
# div = smart_div(div)
# div(2,4)
#Modules
# from Calc import *
# a = 9
# b = 7
# result = sub(a,b)
# print(result)
# print(add(a,b))
# x = lambda a:a*2
# result =x(input())
# print(result)
# class Computer:
# #
# #     def __init__(self,cpu,ram):
# #         self.cpu = cpu
# #         self.ram = ram
# #
# #     def config(self):
# #         print('Config is :',self.cpu, self.ram)
# #
# # comp1=Computer('i5', 16 )
# # comp1.config()
# # comp2=Computer('i7', 8)
# # comp2.config()
# class Computer:
#     def __init__(self):
#         self.name ='Feras'
#         self.age = 25
#
#     def updte(self):
#         self.age=26
#
#
# c1 = Computer()
# c1.name = 'Anna'
# c1.updte()
# c2 = Computer()
# if c1.name == c2.name:
#     print('They are the same')
# else:
#     print('They are different')
# print(c1.name,c1.age)
# print(c2.name,c2.age)
# class Car:
#     wheels = 4
#     def __init__(self):
#         self.mil = 10
#         self.com = 'BMW'
#
# c1 =Car()
# c2 = Car()
# c1.mil = 8
# Car.wheels = 5
#
# print(c1.mil, c1.com, c1.wheels)
# print(c2.mil, c2.com, c2.wheels)
# class Student:
#     school = 'Al-fateh'
#     def __init__(self, m1, m2, m3):
#         self.m1= m1
#         self.m2= m2
#         self.m3= m3
#
#     def avg(self):
#         return (self.m1+self.m2+self.m3)/3
#
#     @classmethod
#     def getSchool(Cls):
#         return Cls.school
#
#     @staticmethod
#     def info():
#         print('This is a Student class.. in abc module and it is static class')
# s1 = Student(34,65,69)
# s2 = Student(22,77,12)
# print(s1.avg())
# print(Student.getSchool())
# Student.info()
# class Student:
#     def __init__(self,name, rollno):
#         self.name = name
#         self.rollno = rollno
#         self.lap = self.Laptop()
#
#     def show(self):
#         print(self.name, self.rollno)
#         self.lap.show()
#
#     class Laptop:
#
#         def __init__(self):
#             self.brand = 'HP'
#             self. cpu = 'i7'
#             self.ram = 8
#
#         def show(self):
#             print(self.brand, self.cpu, self.ram)
#
#
# s1 = Student('Feras',20)
# s2 = Student('Anna', 30)
# s1.show()
# s2.show()
# class A:
#
#     def __init__(self):
#         print('in a init')
#
#     def feature1(self):
#         print('Feature1 is working...')
#
#
#     def feature2(self):
#         print('Feature2 is working...')
# class B:
#
#     def __init__(self):
#         print('in b init')
#
#     def feature3(self):
#         print('Feature3 is working...')
#
#     def feature4(self):
#         print('Feature4 is working...')
#
# class C(A,B):
#
#     def __init__(self):
#         super().__init__()
#         print('in c init')

#
#
# a1 = A()
# a1.feature1()
# a1.feature2()
#
# b1= B()
# b1.feature3()
# b1.feature4()

# c1 = C()
# class PyCharm:

#     def execute(self):
#         print('Compiling')
#         print('Running')
# class MyEditor:
#
#     def execute(self):
#         print('sell Check')
#         print('Convention Check')
#         print('Compiling')
#         print('Running')
#
# class Laptop:
#
#     def code(self,ide):
#         ide.execute()
#
# ide = MyEditor()
# lap1 =Laptop()
# lap1.code(ide)
# class Student:
#
#     def __init__(self,m1,m2):
#         self.m1=m1
#         self.m2= m2
#
#     def __add__(self, other):
#         m1 = self.m1 + other.m1
#         m2 = self.m2 + other.m2
#         s3 = Student(m1,m2)
#         return s3
#
#     def __gt__(self, other):
#         r1 = self.m1 + self.m2
#         r2 = other.m1 + other.m2
#         print(r1,r2)
#         if r1 > r2:
#             return True
#         else:
#             return False
#
#
# s1 = Student(70,5)
# s2 = Student(65,54)
# s3 = s1 + s2
# print(s3.m1)
#
# if s1 > s2:
#     print('s1 wins')
# else:
#     print('s2 wins')
# class Student:
#     def __init__(self,m1,m2):
#         self.m1 = m1
#         self.m2 = m2
#     def sum(self,a=None,b=None,c=None):
#         s= 0
#         if a!=None and b !=None and c !=None:
#             s = a+b+c
#         elif a!= None and b!=None:
#             s = a+b
#         else:
#             s = a
#         return s
# s1 = Student(44,21)
# print(s1.sum(4,5,6))
# class A:
#
#     def show(self):
#         print('in A show')
#
# class B(A):
#
#     def show(self):
#         print('in B show')
#
# s1 = B()
# s1.show()
# class TopTen:
#
#     def __init__(self):
#         self.num = 1
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.num <=10:
#            val = self.num
#            self.num+= 1
#            return val
#         else:
#             raise StopIteration
#
# values = TopTen()
# print(next(values))
# for i in values:
#     print(i)
# a = 4
# b = 2
# try:
#     print('resource open')
#     print(a/b)
#     k = int(input('Enter a number please: '))
#     print(k)
#
# except ZeroDivisionError as e:
#     print('Hey, You can not divide a number by zero',e)
#
# except ValueError as e:
#     print('Invalid Input')
#
# except Exception as e:
#     print('Something went wrong')
#
# finally:
#     print('resource closed')
# from threading import *
# from time import sleep
# class Hello(Thread):
#     def run(self):
#         for i in range(10):
#             print('Hello')
#             sleep(1)
#
# class Hi(Thread):
#     def run(self):
#         for i in range(10):
#             print("Hi")
#             sleep(2)
#
# t1 = Hello()
# t2 = Hi()
#
# t1.start()
#
# t2.start()
# t1.join()
# t2.join()
# print('Bye')
# f = open('MyData', 'w')
# f.write('I will be the best programmer ever just wait me soon ')
# f1 = open('MyData','r')
# print(f1.read())
# pos = -1
#
# def search(list, a):
#     for i in range(len(list)):
#         if list[i]== a:
#             globals() ['pos'] = i
#             return True
#     return False
#
# list = [4,5,87,6,2,4,5,1,9]
# a = 9
# if search(list,a):
#     print('Found',pos+1)
# else:
#     print('Not Found')
import mysql.connector

mydb = mysql.connector.connect(host="localhost",user= "feras", passwd= "12345")

mycursor = mydb.cursor()

mycursor.execute("show databases")

for i in mycursor:
	print(i)

