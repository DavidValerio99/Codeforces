import math

kids = int(input())
a = map(int,input().split(" "))
count = count2 = count3 = count4 = 0
for i in a:
    #self students that must be allocated
    if i==1:
        count+=1
    #groups of two
    elif i==2:
        count2+=1
    #groups of three
    elif i==3:
        count3+=1
    #groups of four
    elif i==4:
        count4+=1

taxis = count4 + math.ceil(count2//2) + math.ceil((count3 + count)//2)
print(taxis)
