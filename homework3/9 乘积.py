import random
lenth = 12
a = []
b = []
for i in range(lenth):
    a.append(random.randint(1,9))
p = 1
for i in range(lenth):
    b.append(p)
    p *= a[i]
p = 1
for i in range(lenth-1,-1,-1):
    b[i] *= p
    p *= a[i]
print("a:",a)
print("b:",b)