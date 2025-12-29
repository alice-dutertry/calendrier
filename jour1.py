f = open("jour1.txt")
lines = f.readlines()

result = 0

for line in lines:
    max = -1
    line = line.strip()
    for c in line:
        n = int(c)
        if max < n:
            max = n
            print(max)
    result = result + max
    
print(result)

# 511