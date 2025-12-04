from copy import deepcopy

with open('day04/input.txt', 'r') as file:
    data = [[x.strip() for x in line] for line in file.readlines()]

# with open('day04/example.txt', 'r') as file:
#     data = [[x.strip() for x in line] for line in file.readlines()]

for r in data:
    if r[-1] == "":
        r.pop()
x_max, y_max = len(data[0]), len(data)
dirs = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
found = set()
prev_found = 0
new_found = 21372137
curr_data = deepcopy(data)
while prev_found != new_found:
    prev_found = new_found
    for i in range(y_max):
        for j in range(x_max):
            if curr_data[i][j] != "@":
                continue
            curr = 0
            for d in dirs:
                x, y = i+d[0], j+d[1]
                if x < 0 or x > x_max-1 or y < 0 or y > y_max-1:
                    continue
                if curr_data[x][y] == "@":
                    curr += 1
            if curr < 4:
                found.add((i, j))
                data[i][j] = "x"
    if new_found == 21372137:
        print(f"Part 1: {len(found)}")
        
    new_found = len(found)
    curr_data = deepcopy(data)
    
print(f"Part 2: {len(found)}")