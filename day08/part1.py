with open('input.txt', 'r') as f:
    contents = f.read()
# contents = ("""30373
# 25512
# 65332
# 33549
# 35390""")
rows = contents.split()
for i, row in enumerate(rows):
    rows[i] = list(map(lambda tree: int(tree), row))


def is_tallest(tree: int, x: int, y: int, column: list, row: list) -> bool:
    # print()
    # print(f'{x}, {y}, {tree}')
    # column
    above = column[:y]
    below = column[y + 1:]
    # print('above', above)
    # print('below', below)

    # row
    left = row[:x]
    right = row[x + 1:]
    # print('left', left)
    # print('right', right)

    if 0 in [x, y]:
        return True
    if x == len(row) - 1:
        return True
    if y == len(column) - 1:
        return True

    if tree > max(above):
        return True
    if tree > max(below):
        return True
    if tree > max(left):
        return True
    if tree > max(right):
        return True
    
    return False


visible_trees = 0

for y, row in enumerate(rows):
    for x, tree in enumerate(row):
        column = [rows[i][x] for i in range(len(rows))]
        if is_tallest(tree, x, y, column, row):
            # print(tree, x, y)
            visible_trees += 1
            # print()
        # # top or bottom of a column
        # if y == 0 or y == len(rows) - 1:
        #     visible_trees += 1
        #     # continue
        # # start or end of a row
        # if x == 0 or x == len(row) - 1:
        #     visible_trees += 1
        #     # continue
        # is_tallest(tree, x, y, column, row)
        # print(x, y, tree)
        # print('column', column[:y], column[y:])
        # print('row', row[:x], row[x:])
        # print()
        # # if (tree > max(column[:y]) and tree > max(column[y:])
        # #     and tree > max(row[:x]) and tree > max(row[x:])):
        # #     visible_trees += 1
        
        
print(visible_trees)