successful = True
for i in range(5):
    print("attempt",i+1)
    if successful:
        print("congratulations")
        break
else:
    print("sorry you have failed")
"""
attempt 1
congratulations
"""

#-----------NESTED LOOPS---------------------------------------------
for x in range(3):
    for y in range(2):
        print((x,y))
#---------------------ITERABLE---------------------------------
for x in "python":
    print(x)