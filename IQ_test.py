def even(n,numeros):
    paridad = 0
    for i in range(n):
        if (numeros[i]%2 == 0):
            paridad+=1
    if paridad > 1:
        for i in range(n):
            if (numeros[i]%2 != 0):
                index = i 
    else:
        for i in range(n):
            if (numeros[i]%2 == 0):
                index = i  
    return index

n = int(input())
numeros = map(int,input().split(" "))

print (even(n,numeros))