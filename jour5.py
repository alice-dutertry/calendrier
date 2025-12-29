f = open("Calendrier/jour5.txt")
lines = f.readlines()

result = 0

for line in lines:
    max = 9
    line = line[:-1]
    for c in line:
        n = int(c)
        if max > n:
            max = n
    print(max)
    result = result + max
    
print(result)

# 198
# FAUXXXXX PROGRAMME NE DONNE PAS LE PLUS PETIT CHIFFRE DE CHAQUE LIGNE 