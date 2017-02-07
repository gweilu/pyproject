# -*- coding: utf-8 -*-
import  math
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

