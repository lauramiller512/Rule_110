from time import sleep

def compute(cells):
    print(" ".join(["." if not c else "X" for c in cells]))
    l = len(cells)
    new = []
    for i in range(l):
        neighbours = (cells[(i - 1) % l], cells[i], cells[(i + 1) % l])
        if neighbours in [(1, 0, 0), (1, 1, 1), (0, 0, 0)]:
            new.append(0)
        else:
            new.append(1)
    sleep(.5)
    compute(new)
compute([0, 0, 0, 0, 0, 0, 0, 0, 0, 1])
