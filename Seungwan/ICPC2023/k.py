n = int(input())
star_list = []
for i in range(n):
    star_list.append(list(map(int, input().split())))

symmetry_star = {}

for i in range(len(star_list)):
    for j in range(len(star_list)):
        if (star_list[i][0] + star_list[j][0]) % 2 == 1 or (star_list[i][1] + star_list[j][1]) % 2 == 1:
            continue
        x = (star_list[i][0] + star_list[j][0]) / 2
        y = (star_list[i][1] + star_list[j][1]) / 2
        if (x, y) in symmetry_star:
            symmetry_star[(x, y)] += 1
        else:
            symmetry_star[(x, y)] = 1

print(max(symmetry_star.values()))
