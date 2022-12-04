with open('input.txt', 'r') as f:
    contents = f.read()
rucksacks = contents.split()

elf_groups = []

temp_group = []
for i, rucksack in enumerate(rucksacks):
    counter = i + 1
    temp_group.append(rucksack)
    if counter % 3 == 0:
        elf_group = temp_group.copy()
        elf_groups.append(elf_group)
        temp_group.clear()

# print(elf_groups[:3])
for group in elf_groups[:3]:
    print(group)


from string import ascii_letters

priorities_sum = 0

for group in elf_groups:
    rucksack_1, rucksack_2, rucksack_3 = group
    rucksack_1 = set(rucksack_1)
    rucksack_2 = set(rucksack_2)
    rucksack_3 = set(rucksack_3)
    badge = list(rucksack_1.intersection(rucksack_2).intersection(rucksack_3))[0]
    priorities_sum += ascii_letters.index(badge) + 1

print(priorities_sum)
