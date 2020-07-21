
def wins(x):
    A = D = 0
    juego = input()
    for i in range(x):
        if juego[i]=="A":
            A+=1
        else:
            D+=1
    #More A
    if A > D: 
        print("Anton")
    #More D
    elif D > A: 
        print("Danik")
    #BOTH    
    else:    
        print ("Friendship")

x = int(input())
wins(x)