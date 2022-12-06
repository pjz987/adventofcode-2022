with open('input.txt', 'r') as f:
    contents = f.read()

crates, moves = contents.split('\n\n')

crate_rows = crates.split('\n')
crates = {}
for i, crate_row in enumerate(crate_rows[::-1]):
    crate_row = crate_row[1::4]
    crate_rows[i] = crate_row
    for j, crate in enumerate(crate_row):
        if i == 0:
            crates[int(crate[0])] = [] # need the key to be an int or str?

crate_rows.pop(0)
for i, row in enumerate(crate_rows):
    for j, crate in enumerate(row):
        if crate != ' ':
            crates[j + 1].append(crate)

moves = moves.split('\n')
for move in moves:
    move = list(map(lambda x: int(x), move.split()[1::2]))
    amount, start, end = move
    start = crates[start]
    end = crates[end]
    for _ in range(amount):
        end.append(start.pop())

top_crates = ''
for crate in crates:
    top_crates += crates[crate][-1]
print(top_crates)