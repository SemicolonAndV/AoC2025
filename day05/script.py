with open('day05/input.txt', 'r') as file:
    data = [x.strip() for x in file.readlines()]
    

# with open('day05/example.txt', 'r') as file:
#     data = [x.strip() for x in file.readlines()]
    
good = set()
lst = []
for entry in data:
    if "-" in entry:
        start, stop = entry.split("-")
        lst.append([int(start), int(stop)])
    elif entry != "":
        for x in lst:
            if x[0] <= int(entry) <= x[1]:
                good.add(entry)

lst.sort()
merged = [lst[0]]
for start, stop in lst[1:]:
    # check if previous record overlaps with next one and extend the range if so
    if start <= merged[-1][1]:
        merged[-1][1] = max(stop, merged[-1][1])
    else:
        # otherwise add the new range 
        merged.append([start, stop])
        
# add 1 as ranges are inclusive
s = sum([y-x+1 for x, y in merged])
print(f"Part 1: {len(good)}")
print(f"Part 2: {s}")
