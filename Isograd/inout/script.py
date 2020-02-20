def is_inter(h1, h2):
    if h1[0] > h2[0]:
        h1, h2 = h2, h1
    return h2[0]<h1[1]

file = 'input1.txt'

hours = list()

with open(file, "r") as f:
    n = int(f.readline())
    for i in range(n):
        hours.append(tuple(map(int, f.readline().split())))

hours.sort()

comp = 0

for i in range(n):
    c = 1
    for j in range(n):
        if i==j:
            continue
        if hours[j][0] > hours[i][1]:
            break
        if is_inter(hours[i], hours[j]):
            # print(hours[i], hours[j])
            c += 1
    comp = max(comp, c)
    print(i, comp)

print(comp)
