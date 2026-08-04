#1 Write a program that swaps two variables without using a third variable.
a="apple"
b="banana"
a,b = b,a
print("a is",a)
print("b is",b)

#2 Take a person's name and age as input and print a formatted sentence using both.
name = input("enter your name:")
age = int(input("enter your age:"))
print("hello my name is",name,"i am",age,"years old")
"""
enter your name:hari
enter your age:21
hello my name is hari i am 21 years old
"""


#3 Convert a temperature from Celsius to Fahrenheit using a formula
celsius = float(input("enter your temperature in celsius:"))
fahrenheit = (celsius * 9/5)+32
print("temerature in fahrenheit is",fahrenheit)
"""
enter your temperature in celsius:37.5
temerature in fahrenheit is 99.5"""
