def even(numeros):
    paridad = 0
    a = int(input())
    for i in range(numeros):
        if (a[i]%2 == "0"):
            paridad+=1
    if paridad > 1:
        for i in range(numeros):
            if (a[i]%2 != "0"):
                index = i 
    else:
        for i in range(numeros):
            if (a[i]%2 == "0"):
                index = i  
    return index

numeros = int(input())
print (even(numeros))