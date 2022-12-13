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

def direction_check(tree: int, trees: list[int]) -> int:
    viewing_distance = 0
    for other_tree in trees:
        viewing_distance +=1
        if tree <= other_tree:
            break
    return viewing_distance


def scenic_score(tree: int, x: int, y: int, column: list, row: list) -> int:
    # print()
    # print(f'{x}, {y}, {tree}')

    # column
    above = column[:y]
    above.reverse()
    below = column[y + 1:]

    # row
    left = row[:x]
    left.reverse()
    right = row[x + 1:]

    above_vd = direction_check(tree, above)
    below_vd = direction_check(tree, below)
    left_vd = direction_check(tree, left)
    right_vd = direction_check(tree, right)

    return above_vd * below_vd * left_vd * right_vd



    # if 0 in [x, y]:
    #     return True
    # if x == len(row) - 1:
    #     return True
    # if y == len(column) - 1:
    #     return True

    # if tree > max(above):
    #     return True
    # if tree > max(below):
    #     return True
    # if tree > max(left):
    #     return True
    # if tree > max(right):
    #     return True
    
    # return False


scenic_scores = []

for y, row in enumerate(rows):
    for x, tree in enumerate(row):
        column = [rows[i][x] for i in range(len(rows))]
        scenic_scores.append(scenic_score(tree, x, y, column, row))


print(max(scenic_scores))