
def problem(a):
    for i in a:
        if i==1:
            return "HARD"
    else:
        return "EASY"
n = int(input())
a = map(int,input().split(" "))
print(problem(a))

