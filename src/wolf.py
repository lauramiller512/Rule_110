from time import sleep
import itertools
import sys


def parse_rule(rule_number):
    return list(map(int, list(str(bin(int(rule_number)))[2:].zfill(8))))


def make_states():
    return list(list(itertools.product([1, 0], repeat=3)))

def make_map(s, r):
    return dict(zip(s, r))

def compute(cells, rule_map):
    # need to examine pairs in grid to determine cells

    print(" ".join(["." if not a else "X" for a in cells]))

    l = len(cells)
    new = []
    for i in range(l):
        neighbours = (cells[(i - 1) % l], cells[i], cells[(i + 1) % l])
        new.append(rule_map[neighbours])
    

    sleep(.5)
    return new

def main():
    cells = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
    rule_number = input(str(("Enter rule number: ")))
    rule_number = parse_rule(rule_number)
    states = make_states()
    rule_map = make_map(states, rule_number)
    try: 
        while True:
            cells = compute(cells, rule_map)
    except KeyboardInterrupt:
        sys.exit("Game over")

if __name__ ==  "__main__":
    main()
