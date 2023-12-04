res=float(input("十进制数:"))
minus = 2
while minus <= res:
    minus *= 2
minus /= 2
ans =""
if minus * 2 <= res :
    minus *= 2
while minus >= 1:
    if res >= minus:
        res -= minus
        ans += '1'
    else: 
        ans += '0'
    minus /= 2 
if res!=0:
    ans += '.'
while res >= 0.000000001 :
    if res >= minus:
        res -= minus
        ans += '1'
    else: 
        ans += '0'
    minus /= 2 
print(ans)