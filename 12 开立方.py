a=float(input("请输入需要开立方的数字："))
left=0
right=a
while right-left>0.001:
    mid = (left+right)/2
    if mid**3 <a:
        left=mid
    else:
        right = mid
print(mid)