num = input("请输入序列，数字之间以空格隔开:").split(' ')
length = len(num)-1
ans1=[]
ans2=[]
for i in num:
    ans1.insert(0,i)
while ~length:
    ans2.append(num[length])
    length-=1
print(ans1)
print(ans2)
