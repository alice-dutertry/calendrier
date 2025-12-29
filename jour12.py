f = open("jour12.txt")
lines = f.readlines()

result = float('inf')
for line in lines :
    line = line.strip()
    min = 9
    for c in line :
        c = int(c)
        if min > c:
            min = c
    somme = 0
    for c in line:
        c = int(c)
        if c != min:
            somme += c
    if somme < result:
        result = somme
print(result)

# 16