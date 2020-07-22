import math 

#def gdc(a,b): 
#    if(b==0): 
#        return a 
#    else: 
#        return gdc(b,a%b) 

def game(a,b,c):
    turn = 1
    while c > 0:
        #Turn de Simon
        if turn:
            c = c - math.gcd(a,c)
            turn = 0
        else:
            if (b > c):
                return 0
            c = c - math.gcd(b,c) 
            turn = 1
    return 1


simon     = int(input())
antisimon = int(input())
stones    = int(input())
print(game (simon,antisimon,stones))