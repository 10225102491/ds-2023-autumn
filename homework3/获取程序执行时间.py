import time
start = time.time()
for i in range(200000000):
    i += 1
end = time.time()
print("cost {} s ".format(end-start))