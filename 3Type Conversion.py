birth_year= int(input("enter your birth year:" ))
print(type(birth_year))
age=2026-birth_year
print(type(age))
print(age)
""" output is
    enter your birth year:2005
    <class 'int'>
    <class 'int'>
    21"""

#ask a user weight(in pounds) and conver into a kilogram and print on terminal
weight = float(input("enter your weight in pounds:" ))
kilogram = weight * 0.45
print("your weight in kilogram is:",kilogram)
