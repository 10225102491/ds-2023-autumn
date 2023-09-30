a=input("请输入需要判断的字符串:")
for i in range(1,len(a)):
    if a[i-1]==a[i]:
        print("存在连续字母")
        break
else:
    print("不存在连续字母")