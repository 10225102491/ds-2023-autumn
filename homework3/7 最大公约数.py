def gcd(a,b):
    return gcd(b,a%b) if a % b else b
a=int(input("a:"))
b=int(input("b:"))
print("最大公约数为:{}".format(gcd(a,b)))