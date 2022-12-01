with open('input.txt', 'r') as f:
    content = f.read()

elf_snacks = content.split('\n\n')
elf_snacks_itemized = list(map(lambda total: total.split(), elf_snacks))
for i, elf in enumerate(elf_snacks_itemized):
    elf_snacks_itemized[i] = list(map(lambda snack: int(snack), elf))
elf_snack_totals = list(map(lambda snacks: sum(snacks), elf_snacks_itemized))
biggest_snack_load = max(elf_snack_totals)
print(biggest_snack_load)