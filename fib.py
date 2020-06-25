import time
a = 0
b = 1
c = 0
while True:
    c = a + b
    a = b
    b = c
    print(c)