import copy
import random

DEBUG_MODE = 1
W = 30
H = 30

debug_ans = []


def exit():
    import sys
    sys.exit()


def check_border(x, y):
    if x < 0 or x > W - 1:
        return False
    elif y < 0 or y > H - 1:
        return False
    else:
        return True


class Cell:
    def __init__(self, v=0, x=-1, y=-1):
        self.v = v
        self.x = x
        self.y = y


def compare_cells(cell_a, cell_b, bias):
    # if cell_a.v > cell_b.v:
    #     return cell_a
    # return cell_b
    point_bias_a = max(0, cell_a.x + cell_a.y - bias)
    point_bias_b = max(0, cell_b.x + cell_b.y - bias)
    if (cell_a.v + bias) > (cell_b.v + bias):
        return cell_a
    return cell_b


def search_max_cell(cells, step):
    maxCell = Cell()
    for y in range(0, H):
        for x in range(0, W):
            tmpCell = Cell(cells[y][x], x, y)
            maxCell = compare_cells(maxCell, tmpCell, step)

    return maxCell


def reduce_cell(ans, cells, targetCell):
    """
    Recursive
    """
    org_v = targetCell.v
    v = org_v
    x = targetCell.x
    y = targetCell.y

    if cells[y][x] == v:
        cells[y][x] = cells[y][x] - 1
        ans.append(y)
        ans.append(x)
        # directions = [(0, -1), (-1, 0), (0, 1), (1, 0)] # tsuka
        directions = [(0, 1), (1, 0), (-1, 0), (-1, 0)]
        # directions = [(-1, 0), (0, -1)]
        for d in directions:
            v = org_v - 1
            if v == 0:
                continue
            dx = x + d[0]
            dy = y + d[1]
            # aaa
            if check_border(dx, dy) and cells[dy][dx] == v:
                ans, cells = reduce_cell(ans, cells, Cell(v, dx, dy))

    return ans, cells


def core(cells):
    """
    Main Algorithm
    """
    final_ans = []
    step = 0
    while True:
        # 探索
        targetCell = search_max_cell(cells, step)

        if targetCell.v == 0:
            break

        # bbb
        ans, cells = reduce_cell([], cells, targetCell)
        final_ans.append(ans)
        step = step + 1

    return final_ans, cells


def print4cells(cells):
    print("====" * 5)
    for row in cells:
        for r in row:
            print("{0:3d}".format(r), end=" ")
        print("")


def main():
    lines = []
    if not DEBUG_MODE:
        for i in range(0, 30):
            x = input()
            lines.append(x)
    else:
        with open("test1.txt", "r") as f:
            lines = [i.rstrip("\n") for i in f.readlines()]

    # convert int cells
    cells = []
    vals = []
    for y in lines:
        tmp = []
        for x in y.split(" "):
            tmp.append(int(x))
            vals.append(int(x))
        cells.append(tmp)

    if DEBUG_MODE:
        print4cells(cells)

    # Let's go!
    final_ans, cells = core(cells)

    if DEBUG_MODE:
        print4cells(cells)
        with open("debug.txt", "w") as f:
            for ans in final_ans:
                line = " ".join(str(i+1) for i in ans)
                f.write(line + "\n")
        print("Te:{}".format(len(final_ans)))
    else:
        # Output
        for ans in final_ans:
            # print(ans)
            # print(type(ans))
            line = " ".join(str(i+1) for i in ans)
            print(line)

    return 0


if __name__ == "__main__":
    main()
