# -*- coding: utf-8 -*-
import  math
from collections import Iterable
'''
def my_abs(x):
    if not isinstance(x,(int,float)):
        raise TypeError('bad operand tpye')
    if x>=0:
        return x
    else:
        return -x

def quadratic(a,b,c):
    if not isinstance(a,(int)):
        raise TypeError('parameter a is a bad operand type')
    if not isinstance(b,(int)):
        raise TypeError('parameter a is a bad operand type')
    if not isinstance(c,(int)):
        raise TypeError('parameter a is a bad operand type')
    #ax^2+bx+c=0
    #when b^2-4*a*c=0 have one root
    #when b^2-4*a*c>0 have two root
    #when b^2-4*a*c<0 have no  root
    d=b*b-4*a*c
    if d<0:
        print('Sorry the function don\'t have root')
    elif d==0:
        x=-b/2/a
        print ('the function root is : %s'%(x))
    else:
        x1=(-b+math.sqrt(d))/2/a
        x2=(-b-math.sqrt(d))/2/a
        print ('Then function root are : %.2f,%.2f'%(x1,x2))

print ('please input a value:')
a=int(input())
print ('please input b value:')
b=int(input())
print ('please input c value:')
c=int(input())

quadratic(a,b,c)

#默认参数
def enroll(name,gender,age=6,city='qingdao'):
    print('name= ',name)
    print('gender= ', gender)
    print('age= ', age)
    print('city= ', city)
enroll('weilu','F',city='shanghai')

def plist(*num):
    for i in num:
        print (i)
plist(1,2,3)

def person(name,age,*,city='newyork',job):
    print('name: ',name,'\n','age: ',age,'\n',city,'\n',job)
extra={'city':'beijing','job':'Engineer'}
person('weilu','31',job='doctor')

#递归函数
def fact(n):
    if n==1:
        return 1
    return n*fact(n-1)
print(fact(10))

#用递归函数实现汉诺塔的移动
def move(n,a,b,c):
    if n==1:
        print('move',a,'-->',c)
        return
    move(n-1,a,c,b)
    print('move',a,'-->',c)
    move(n-1,b,a,c)
move(2,'甲','乙','丙')

#切片
L=list(range(100))
print(L[0:10])
print(L[10:20])
print(L[::5])
print(L[:])
#迭代
d={'a':1,'b':2,'c':3}
for key,value in d.items():
    print(key,value)
#判断是否可以进行迭代 from collections import Iterable
b=isinstance('abc',Iterable)
b1=isinstance([1,2,3,4],Iterable)
b3=isinstance(123,Iterable)
print (b,b1,b3)
#迭代索引和元素
for i,value in enumerate(['a','b','c']):
    print(i,value)
for x,y in [(1,2),(3,4),(5,6)]:
    print(x,y)
    '''
#列表生产式
L=[m+n for m in 'ABC' for n in 'XYZ']
print(L)
L = ['Hello', 'World', 18, 'Apple', None]
o=[s.lower() for s in L if isinstance(s,str)==True]
print(o)
#生成器
g=(x*x for x in range(10))
for n in g:
    print(n)