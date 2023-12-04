a=int(input("a:"))
if a < 2:
    print("no")
elif a < 4:
    print("yes")
else:
    flag = 1
    i = 2
    while i*i <= a:
        if a % i == 0:
            flag = 0
        i = i + 1
    if flag == 1:
        print("yes")
    else:
        print("no")