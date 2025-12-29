f = open("jour7.txt")
lines = f.readlines()

result = 0

for line in lines:
    min = 9
    line = line.strip()
    for d in line:
        n = int(d)
        if min > n:
            min = n
            print(min)
    result = result + min
    
print(result)

# 287