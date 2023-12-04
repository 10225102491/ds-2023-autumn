import random
def insert_sort(arr):
    for i in range(1,len(arr)):
        x = i 
        while x > 0 and arr[x] < arr[x-1]:
            arr[x],arr[x-1]=arr[x-1],arr[x]
            x = x - 1
arr = []
for i in range(20):
    arr.append(random.randint(0,10))
print("before sort:",end='')
print(arr)
insert_sort(arr)
print("after sort:",end='')
print(arr)