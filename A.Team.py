problemas = int(input())
count = 0
while problemas:
    a= int(input())
    b= int(input())
    c= int(input())
    if (a and b or a and c or b and c ):
        count+=1
    problemas-=1
print(count)    
