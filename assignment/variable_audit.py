""" 
Q1. VARIABLE AUDIT
    Look at this code. Without running it, predict the output. Then verify.

        a = 10
        b = a
        a = a + 5
        print(a, b)          # → ___  (why doesn't b change?)

        x = [1, 2, 3]
        y = x
        x.append(4)
        print(x, y)          # → ___  (why DOES y change here?)

    Explain the difference in one sentence using the word "reference".
"""

a=10
b=a
a=a+5
print(a,b)

x = [1, 2, 3]
y = x
x.append(4)
print(x, y)
