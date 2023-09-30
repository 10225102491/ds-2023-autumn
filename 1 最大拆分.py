num = int(input("n:"))
a=int(num/3)
b=int(num%3)
if b == 1:
    a = a - 1
    b = b + 3
if a:
    print("{0}个3".format(a))
if b:
    print("1个{0}".format(b))
