temperature = 15
if temperature > 25:
    print("it is a hot day")
    print("drink water")
elif temperature < 10:
    print("it is a cold day")
    print("wear woolen clothes")
else:
    print("it normally")
print("DONE")

#--------------------------------------------------------------------------------------------------------------------------------------
#voter age
name = input("enter your name:")
age = int (input("enter your age:"))
if age >=18:
    print("congratulations!")
    print ("you are eligible to vote")
else:
    print("sorry"\
          " you are not eligible to vote")
print("Thank You",name,"for your time")

"""
enter your name:hari 
enter your age:21
congratulations!
you are eligible to vote
Thank You hari  for your time"""

age = 18
message = "ok" if age >= 18 else "not ok"
print(message)