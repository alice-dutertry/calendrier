f = open("Calendrier/jour4.txt")
lines = f.readlines()

mult = 1
for line in lines:
    line = line.strip()
    sommeligne = 0
    for c in line:
        n = int(c)
        sommeligne = sommeligne + n
        
    mult = mult * sommeligne

print(mult)

# 01/03