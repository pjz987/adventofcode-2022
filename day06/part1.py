with open('input.txt', 'r') as f:
    contents = f.read()

i = 0
j = 4
while True:
    if len(set(contents[i:j])) == 4:
        break
    i += 1
    j += 1
print(j)