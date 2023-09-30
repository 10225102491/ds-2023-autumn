max=10000000
sum=0
for i in range(1,max):
    sum = sum + 1/i/i
print("pi={}".format((sum*6)**(1/2)))
sum=0
for i in range(1,max,2):
    sum = sum +1/i/i
print("pi={}".format((sum*8)**(1/2)))
sum=0
for i in range(1,max):
    sum = sum + 1/i/i/i/i
print("pi={}".format((sum*90)**(1/4)))