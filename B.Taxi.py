import math
 
 
kids = int(input())
count = 0
while kids:
    a= int(input())
    count+=a
    print (count)
    kids-=1

print(math.ceil(float(count/4)))
