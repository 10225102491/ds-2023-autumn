
c=2000
g=c/2
while g*g-c>0.000000001 or c-g*g>0.000000001:
    g=(g+c/g)/2
print("when c = 2000,sqrt(c)={}".format(g)) 
c=2
g=c/2
while g*g-c>0.0000000000001 or c-g*g>0.0000000000001:
    g=(g+c/g)/2
print("when g = c/2,sqrt(c)={}".format(g))
c=2
g=c
while g*g-c>0.0000000000001 or c-g*g>0.0000000000001:
    g=(g+c/g)/2
print("when g = c,sqrt(c)={}".format(g))
c=2
g=c/4
while g*g-c>0.0000000000001 or c-g*g>0.0000000000001:
    g=(g+c/g)/2
print("when g = c/4,sqrt(c)={}".format(g))
c=10
g=c/2
while g*g*g-c>0.0000000000001 or c-g*g*g>0.0000000000001:
    g=(g*2+c/g/g)/3
print("when g = c/4,c**(1/3)={}".format(g))