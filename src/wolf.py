from time import sleep

rule = input(str(("Enter rule number: ")))

cells = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]

grid = {
    111: 3,
    110: 3,
    101: 3,
    100: 3,
    011: 3,
    010: 3,
    001: 3,
    000: 3
}

def make_binary(rule):
    binary = bin(rule)

    # remove the first two chars from the bin
    binary = binary[2:].zfill(8)
    print(binary)

def compute(cells):
    # currently only  computes based on 110
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
    


make_binary(rule)
compute(cells)

# 1. turns rule number into binary string
# 2. apply rule to list
