import time
start = time.time()
start2 = time.time()
result = ""
result2 = ""
for i in range (1, 100001):
    result += str(i)
print (result)
print("+= Time:", time.time()- start)

for x in range (1, 100001):
    result = str(x)
print ("".join(result2))
print("+= jointime:", time.time()- start2)