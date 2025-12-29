f = open("Calendrier/jour2.txt")
lines = f.readlines()

list = []

for line in lines:
    total = 0
    line = line.strip()
    for c in line:
        n = int(c)
        total = total + n
    list.append(total) 
        
    
print(list)

# 23
