"""
Q7. ALIASING DEEP DIVE
    Explain the output of this entire sequence (16 values).
    Do it on paper FIRST, then verify with Python.

        a = [1, 2, 3]
        b = a
        c = a[:]
        d = list(a)

        a.append(4)
        b[0] = 99
        c.append(88)
        d[1] = 77

        print(a)  print(b)  print(c)  print(d)
        print(a is b, a is c, b is d)
        print(a == b, a == c, a == d)


"""
a = [1, 2, 3]
b = a
c=a[:]
d = list(a)

a.append(4)
b[0] = 99
c.append(88)

d[1] = 77

print(a)  

print(b) 

print(c)

print(d)
print(a is b, a is c, b is d)
print(a == b, a == c, a == d)