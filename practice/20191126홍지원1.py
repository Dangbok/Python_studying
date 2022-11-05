Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def Hello(x):
	print(x)

	
>>> 
>>> Hello(3)
3
>>> Hello(5)
5
>>> def add(a,b):
	return (a+b)

>>> add(1,2)
3
>>> add(5,6)
11
>>> def Fun1():
	print("Fun1입니다")

	
>>> def
SyntaxError: invalid syntax
>>> def Fun2(x):
	print(x, "입니다")

	
>>> Fun1()
Fun1입니다
>>> Fun1(3)
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    Fun1(3)
TypeError: Fun1() takes 0 positional arguments but 1 was given
>>> Fun2()
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    Fun2()
TypeError: Fun2() missing 1 required positional argument: 'x'
>>> Fun2(3)
3 입니다
>>> def Fun3(x,y):
	for i in range(y):
		print(x, "님 반가워요")

		
>>> Fun3("홍길동",5)
홍길동 님 반가워요
홍길동 님 반가워요
홍길동 님 반가워요
홍길동 님 반가워요
홍길동 님 반가워요
>>> def function1(x):
	a=3;b=5
	y=a*b+x+b
	print(y)

	
>>> d=function1(10)
30
>>> print(d)
None
>>> def function2(x):
	a=3;b=5
	y=a*x+b
	return(y)

>>> d=function2(10)
>>> print(d)
35
>>> def square(a):
	c=a*a
	return(c)

>>> square(4)
16
>>> square(8)
64
>>> #연습문제
>>> def triangle(c):
	a=3;h=2
	c=a*h/2
	return(c)

>>> triangle(3)
3.0
>>> def triangle(a,h):
	c=a*h/2
	return(c)

>>> 
>>> int(triangle(3,2))
3
>>> 
