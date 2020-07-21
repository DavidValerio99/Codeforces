def pasos(x):
    steps = 0
    i = 5
    while i > 0:     
        steps += int(x)//i
        x = x%i
        i-=1    
    print (steps)
        
x = int(input())
pasos(x)