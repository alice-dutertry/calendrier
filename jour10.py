f = open("Calendrier/jour10.txt")
lines = f.readlines()

for line in lines:
    line = line.strip()
    stop = False
    for pos, c in enumerate(line):
        c = int(c)
        if pos <= len(line) - 4:
            d = int(line[pos +1])
            e = int(line[pos + 2])
            f = int(line[pos + 3])
            if d == c + 1 and e == c + 2 and f == c + 3:
                print(c + d + e + f)
                stop = True
                break
    if stop:
        break

# 26
