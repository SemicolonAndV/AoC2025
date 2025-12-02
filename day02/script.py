import re

def check_validity_1(n):
    s = str(n)
    if len(s) % 2 != 0:
        return 0
    l = len(s)//2
    x, y = s[:l], s[l:]
    if x == y:
        return n
    return 0

def check_validity_2(n):
    s = str(n)

    res = bool(re.fullmatch(r"(.+)\1+", s))        
    if res:
        return n
    return 0

with open('day02/input.txt', 'r') as file:
    data = [tuple(x.split("-")) for x in file.read().strip().split(",")]
    
# with open('day02/example.txt', 'r') as file:
#     data = [tuple(x.split("-")) for x in file.read().strip().split(",")]
    
part_1 = 0
part_2 = 0
for entry in data:
    for i in range(int(entry[0]), int(entry[1])+1):
        part_1 += check_validity_1(i)
        part_2 += check_validity_2(i)
        
print(f"Part 1: {part_1}")
print(f"Part 2: {part_2}")