import random
def mergesort(t):
    l = len(t)
    if l == 1:
        return t
    mid = l>>1
    tl = t[0:mid]
    tl = mergesort(tl)
    tr = t[mid:]
    tr = mergesort(tr)
    p = 0
    q = 0
    r = 0
    while p < mid and q < l - mid :
        if tl[p] < tr[q]:
            t[r] = tl[p]
            p += 1
        else:
            t[r] = tr[q]
            q += 1 
        r += 1
    while p < mid:
        t[r] = tl[p]
        p += 1
        r += 1
    while q < l - mid:
        t[r] = tr[q]
        q += 1 
        r += 1
    return t
def bubblesort(t):
    l = len(t)
    for k in range(l ):
        for i in range(1,l):
            if t[i-1] > t[i]:
                temp = t[i-1]
                t[i - 1] = t[i]
                t[i] = temp
    return t
a = []
for i in range(30):
    a.append(random.randint(0,10000))
b = a.copy() 
c = a.copy()
print(mergesort(b))
print(bubblesort(c))