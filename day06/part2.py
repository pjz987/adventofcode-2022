with open('input.txt', 'r') as f:
    contents = f.read()

i = 0
j = 14
while True:
    if len(set(contents[i:j])) == 14:
        break
    i += 1
    j += 1
print(j)