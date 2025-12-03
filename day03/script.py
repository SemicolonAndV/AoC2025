from collections import deque

def max_single_j_index(bank):
    # look for first occurrence of max value for remaining bank values
    max_j = str(max(int(b) for b in bank))
    # return index of first occurrence
    return bank.index(max_j)

def max_joltage(bank, remaining):
    if remaining == 0:
        return ""
    # check only parts where it's possible to continue
    limit = len(bank) - remaining
    index = max_single_j_index(bank[:1 + limit])
    # continue searching for max values in a substring, starting fromval right after the max value found 
    return bank[index] + max_joltage(bank[index+1:], remaining - 1)


with open('day03/input.txt', 'r') as file:
    data = [x.strip() for x in file.readlines()]

# with open('day03/example.txt', 'r') as file:
#     data = [x.strip() for x in file.readlines()]
    
part_1 = sum(int(max_joltage(bank, 2)) for bank in data)
part_2 = sum(int(max_joltage(bank, 12)) for bank in data)

print(f"Part 1: {part_1}")
print(f"Part 2: {part_2}")