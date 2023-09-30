import random
import math
def cal(times):
    sum = 0
    for i in range(times):
        x=random.uniform(2,3)
        y=random.uniform(0,21)
        if x*x+4*x*math.sin(x)<y:
            sum =sum+1
    return 21*(sum/times)
times = 100000000
print("x*x+4*x*sin(x)在[2,3]的积分为{}".format(cal(times)))
        