with open('day01/input.txt', 'r') as file:
    data = file.readlines()
    
# with open('day01/example.txt', 'r') as file:
#     data = file.readlines()
dial = 50
part_1 = 0
part_2 = 0
for entry in data:
    x = int(entry[1:])
    for i in range(x):
        if entry[0] == "L":
            dial -= 1
        elif entry[0] == "R":
            dial += 1                
        if dial % 100 == 0:
            part_2 += 1
    dial = dial % 100
    if dial == 0:
        part_1 += 1

print(f"Part 1: {part_1}")
print(f"Part 2: {part_2}")