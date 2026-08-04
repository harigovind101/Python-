#1 Print the FizzBuzz sequence from 1 to 50 (multiples of 3 → 'Fizz', 5 → 'Buzz', both → 'FizzBuzz').
for i in range (1,51):
    if i%3 == 0 and i%5 ==0:
        print(i,"FizzBuzz")
    elif i%3 == 0 and i%5 !=0:
        print(i,"Fizz")
    elif i%3 !=0 and i%5 ==0:
        print("Buzz")
    else:
        print("The number",i,"is invalid")
print("DONE")
#2 Write a program that checks if a number is prime.
num = int (input("enter the number:"))
if num > 1:
    for i in range(2,num):
        if num%i == 0:
            print(num,"is not a prime")
            break
    else:
        print(num,"is a prime")
else:
    print(num,"is not a prime")
    
#3 Print a right-angled triangle pattern of stars using nested loops
row = int(input("enter the rows:"))
for i in range(1,row+1):
    for j in range(1,i+1):
        print("*",end="")
    print()