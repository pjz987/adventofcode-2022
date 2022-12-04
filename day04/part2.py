with open('input.txt', 'r') as f:
    contents = f.read()

pairs = contents.split()

partially_contained_ranges = 0

for pair in pairs:
    range1, range2 = [[int(num) for num in rng.split('-')] for rng in pair.split(',')]
    range1 = set(range(range1[0], range1[1] + 1))
    range2 = set(range(range2[0], range2[1] + 1))
    len1 = len(range1)
    len2 = len(range2)
    if range1.intersection(range2):
        partially_contained_ranges += 1

print(partially_contained_ranges)