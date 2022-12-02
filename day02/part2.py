with open('input.txt', 'r') as f:
    contents = f.read()
games = contents.split('\n')

def get_hand(opponent, result):
    if opponent == 'A': # rock
        if result == 'X': # lose
            return 'scissors'
        if result == 'Y': # draw
            return 'rock'
        if result == 'Z': # win
            return 'paper'

    if opponent == 'B': # paper
        if result == 'X': # lose
            return 'rock'
        if result == 'Y': # draw
            return 'paper'
        if result == 'Z': # win
            return 'scissors'

    if opponent == 'C': # scissors
        if result == 'X': # lose
            return 'paper'
        if result == 'Y': # draw
            return 'scissors'
        if result == 'Z': # win
            return 'rock'

hand_to_points = {
    'rock': 1,
    'paper': 2,
    'scissors': 3,
}
result_to_points = {
    'X': 0,
    'Y': 3,
    'Z': 6,
}

points = 0

for game in games:
    opponent, result = game.split()
    hand = get_hand(opponent, result)
    points += hand_to_points[hand] + result_to_points[result]

print(points)