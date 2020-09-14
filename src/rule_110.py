from time import sleep


def compute(cells):
    new_list = [0]
    i = 1

    while i < len(cells) -1:
        c = cells[i]

        c_l = cells[i - 1]
        
        c_r = cells[i + 1]
        
        if c == 0 and (c_l == 1 and c_r == 0):
            new_list.append(0)
        elif (c == 0 and c_r == 0 and c_l == 0) or (c == 1 and c_r == 1 and c_l == 1):
            new_list.append(0)
        else:
            new_list.append(1)

        i = i + 1
    new_list.append(0)
    return new_list


def make_binary(cells):
    new_list = []
    for c in cells:
        if c != 0 and c!= 1:
            new_list.append(0)
        else:
            new_list.append(c)

    return new_list


def generate(cells):
    built_list = ""
    for c in cells[1:-1]:
        if c is 0:
            built_list = built_list + ". "
        else:
            built_list = built_list + "O "
    
    print(built_list)
    return built_list


def validate(cells):
    for c in cells:
        if c not in [0,1]:
            raise ValueError("Invalid character")


cells = [0, 0, 0, 0, 0, 0, 0, 0, 1, 0]
cells = make_binary(cells)


def main():
    n_list = cells
    while True:
        generate(n_list)
        n_list = compute(n_list)
        sleep(.7)

#main()
