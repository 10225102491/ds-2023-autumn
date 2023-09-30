a = int(input("请输入需要求阶乘的数字："))
ans=1
for i in range(2,a+1):
    ans*=i
print(str(a)+"!="+str(ans))
