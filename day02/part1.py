with open('input.txt', 'r') as f:
    contents = f.read()
games = contents.split('\n')

def get_result(opponent, me):
    if opponent == 'A': # rock
        if me == 'X': # rock
            return 'draw'
        if me == 'Y': # paper
            return 'win'
        if me == 'Z': # scissors
            return 'lose'

    if opponent == 'B': # paper
        if me == 'X': # rock
            return 'lose'
        if me == 'Y': # paper
            return 'draw'
        if me == 'Z': # scissors
            return 'win'

    if opponent == 'C': # scissors
        if me == 'X': # rock
            return 'win'
        if me == 'Y': # paper
            return 'lose'
        if me == 'Z': # scissors
            return 'draw'

hand_to_points = {
    'X': 1,
    'Y': 2,
    'Z': 3,
}
result_to_points = {
    'lose': 0,
    'draw': 3,
    'win': 6,
}

points = 0

for game in games:
    opponent, me = game.split()
    result = get_result(opponent, me)
    points += hand_to_points[me] + result_to_points[result]

print(points)