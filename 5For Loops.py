for num in range(5):
    print("hello")
"""
hello
hello
hello
hello
hello"""

for num in range(5):
    print("hello",num)
"""
hello 0
hello 1
hello 2
hello 3
hello 4
"""

for num in range(5):
    print("hello",num+1)
"""
hello 1
hello 2
hello 3
hello 4
hello 5"""

for num in range(5):
    print("hello",num+1,(num+1)*".","tata")
"""
hello 1 . tata
hello 2 .. tata
hello 3 ... tata
hello 4 .... tata
hello 5 ..... tata"""

for i in range(1,10):
    print("hello",i)
"""
hello 1
hello 2
hello 3
hello 4
hello 5
hello 6
hello 7
hello 8
hello 9"""

for i in range (1,10,2):
    print("hello",i,(i)*"s")

