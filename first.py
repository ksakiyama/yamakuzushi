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


# 2つ以上変更できるならTrue
def search_counter(cells, target, x, y):
    """
    Recursive Counter
    """
    org_target = target
    flag = False
    if cells[y][x] == target:
        # cells[y][x] = cells[y][x] - 1
        # 4方向を探索 D,L,T,R
        directions = [(0, 1), (-1, 0), (0, -1), (1, 0)]
        for d in directions:
            target = org_target - 1
            if target == 0:
                continue
            dx = x + d[0]
            dy = y + d[1]
            # 境界線を超えない、かつ、目的の整数
            if check_border(dx, dy) and cells[dy][dx] == target:
                # TODO Recursive
                return True

    return flag


def search_reduce(ans, cells, target, x, y):
    """
    Recursive
    """
    org_target = target

    if cells[y][x] == target:
        cells[y][x] = cells[y][x] - 1
        ans.append(y)
        ans.append(x)
        # 4方向を探索 D,L,T,R
        # directions = [(0, 1), (-1, 0), (0, -1), (1, 0)]
        directions = [(-1, 0), (0, -1)]
        for d in directions:
            target = org_target - 1
            if target == 0:
                continue
            dx = x + d[0]
            dy = y + d[1]
            # 境界線を超えない、かつ、目的の整数
            if check_border(dx, dy) and cells[dy][dx] == target:
                # TODO Recursive
                ans, cells = search_reduce(ans, cells, target, dx, dy)

    return ans, cells


def core(cells):
    """
    Main Algorithm
    """
    final_ans = []

    vals = [i for i in range(100, 0, -1)]
    while True:
        if len(vals) == 0:
            break
        target = vals[0]

        # 周辺
        for y in range(H - 1, -1, -1):
            for x in range(W - 1, -1, -1):
                if cells[y][x] == target and cells[y][x] >= 0:
                    ans, cells = search_reduce([], cells, target, x, y)
                    final_ans.append(ans)
                    if DEBUG_MODE:
                        debug_ans.append([target, ans])
                    ans = []

        # targetを更新
        vals = vals[1:]

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
        # print4cells(cells)
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
