with open('input.txt', 'r') as f:
    contents = f.read()
rucksacks = contents.split()

from string import ascii_letters

priorities_sum = 0

for rucksack in rucksacks:
    # rucksack = rucksacks[i]
    # print(len(rucksack), rucksack)
    length = len(rucksack)
    half = int(length/2)
    compartment_1 = set(rucksack[0:half])
    compartment_2 = set(rucksack[half:])
    common_items = compartment_1.intersection(compartment_2)
    shared_item = list(common_items)[0]
    # print(shared_item)
    priorities_sum += ascii_letters.index(shared_item) + 1

print(priorities_sum)
