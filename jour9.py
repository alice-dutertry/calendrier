f = open("Calendrier/jour9.txt")
lines = f.readlines()

lst = []

for line in lines:
      total = 0
      line = line.strip()
      for c in line:
        n = int(c)
        total = total + n
      lst.append(total)

total = 1

for nb in lst:
    total = total*nb

total = str(total)
print(total[0:4])

# 3467
