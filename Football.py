
def game(x):
    a=len(x)
    count1 = count0 = 0
    for i in range(a):
        if x[i]== "1":
            count1+=1
            count0= 0
            #print (count1)
        else:
            count0+= 1
            count1 = 0
            #print (count0)
        if count0 == 7 or  count1 == 7:
                return "YES"
    return "NO"

x = input()
print(game(x))