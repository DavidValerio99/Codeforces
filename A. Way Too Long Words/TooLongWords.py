
def words(word):
    x = len(word)
    if x > 10:
        return word[0] + str(x-2)+ word[x-1]
    else: 
        return word

palabras = int(input())
while palabras:
    print(words(input()))
    palabras-=1