def main():
    size = int(input())
    cell = input().split()

    for i in range(0, len(cell)):
        cell[i] = int(cell[i])
    m = -1
    for i in range(0, 23):
        if m < check_cycle(cell, i):
            m = check_cycle(cell, i)
    print(m)


def check_cycle(cell, start):
    i = start
    if i in cell:
        cycle = [i]
        j = i
        while 1:
            for k in cycle:
                if cycle.count(k) >= 2:
                    if cycle[0] == cycle[-1]:
                        return len(cycle)-1
                    else:
                        return 0
            else:
                cycle.append(cell[j])
                j = cell[j]
    else:
        return 0


main()