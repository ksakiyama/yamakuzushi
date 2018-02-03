DEBUG_MODE = 1
W = 30
H = 30
# global W
# global H


def check_border(x, y):
    if x < 0 or x > W - 1:
        return False
    elif y < 0 or y > H - 1:
        return False
    else:
        return True


def search_reduce(ans, cells, target, x, y, first=True):
    """
    Recursive
    """
    if cells[y][x] == target:
        cells[y][x] = cells[y][x] - 1  # 減らす
        ans.append(y)  # 解答を追加
        ans.append(x)
        # 4方向を探索 D,L,T,R
        directions = [(0, 1), (-1, 0), (0, -1), (1, 0)]
        for d in directions:
            dx = x + d[0]
            dy = y + d[1]
            # 境界線を超えない、かつ、目的の整数
            if check_border(dx, dy) and cells[dy][dx] == target:
                # cells[dy][dx] = cells[dy][dx] - 1
                # ans.append(dy)
                # ans.append(dx)
                # TODO Recursive
                ans, cells = search_reduce(ans, cells, target, dx, dy)

    return ans, cells


def core(cells, vals):
    """
    Main Algorithm
    """
    final_ans = []
    while True:
        if len(vals) == 0:
            break
        target = vals[0]
        ans = []
        for y in range(0, H):
            for x in range(0, W):
                if cells[y][x] == target:
                    ans, cells = search_reduce(ans, cells, target, x, y)
                    final_ans.append(ans)
                    ans = []
        vals = vals[1:]

        # if DEBUG_MODE:
        #     print4cells(cells)
        #     if vals[0] < 98:
        #         break

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

    vals = list(set(vals))
    vals.sort(reverse=True)

    if DEBUG_MODE:
        print4cells(cells)
        # print(vals)

    # Let's go!
    final_ans, cells = core(cells, vals)

    if DEBUG_MODE:
        print4cells(cells)
        # print(final_ans[:10])
        for i, v in enumerate(final_ans):
            print("{}:{}".format(i, v))
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