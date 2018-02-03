import copy
DEBUG_MODE = 0
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


def search_counter(cells, target, x, y, start=0):
    """
    Recursive Counter
    """
    cnt = start
    org_target = target
    if cells[y][x] == target:
        cells[y][x] = cells[y][x] - 1
        cnt = cnt + 1
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
                cnt, cells = search_counter(cells, target, dx, dy, cnt)

    return cnt, cells


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
                ans, cells = search_reduce(ans, cells, target, dx, dy)

    return ans, cells


def core(cells):
    """
    Main Algorithm
    """
    final_ans = []

    # ----Greedy----------------------------------------------------
    # 探索
    rank_points = []
    vals = [i for i in range(100, 25, -1)]
    # 適当に100くらいやる
    for turn in range(0, 20):
        for target in vals:
            for y in range(5, 25):
                for x in range(5, 25):
                    if cells[y][x] == target and cells[y][x] >= 0:
                        dummy_cells = copy.deepcopy(cells)
                        cnt, _ = search_counter(dummy_cells, target, x, y)
                        rank_points.append([cnt, target, (x, y)])

        # 最も良いポイントは？
        # print(rank_points)
        ans = []
        rank_points.sort(key=lambda x: x[0], reverse=True)
        # 適当に10個くらいやったら探索する
        for i in rank_points[:10]:
            target = i[1]
            x = i[2][0]
            y = i[2][1]
            if cells[y][x] == target and cells[y][x] >= 0:
                ans, cells = search_reduce(ans, cells, target, x, y)
                final_ans.append(ans)
                ans = []

    # ----後始末----------------------------------------------------
    vals = [i for i in range(100, 0, -1)]
    while True:
        if len(vals) == 0:
            break
        target = vals[0]
        ans = []

        # まず中央
        for y in range(5, 25):
            for x in range(5, 25):
                if cells[y][x] == target and cells[y][x] >= 0:
                    ans, cells = search_reduce(ans, cells, target, x, y)
                    final_ans.append(ans)
                    if DEBUG_MODE:
                        debug_ans.append([target, ans])
                    ans = []
        # 周辺
        for y in range(0, H):
            for x in range(0, W):
                if cells[y][x] == target and cells[y][x] >= 0:
                    ans, cells = search_reduce(ans, cells, target, x, y)
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

    # vals = list(set(vals))
    # vals.sort(reverse=True)

    if DEBUG_MODE:
        print4cells(cells)

    # Let's go!
    final_ans, cells = core(cells)

    if DEBUG_MODE:
        print4cells(cells)
        # with open("debug.txt", "w") as f:
        #     for i, v in enumerate(debug_ans):
        #         print("{}:{}:{}".format(i, v[0], v[1]))
        #         f.write("{}:{}:{}\n".format(i, v[0], v[1]))
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

"""
[
    50, 49, 48, 47, 46, 45, 44, 43, 42, 41, 
40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 
30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 
100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 
90, 89, 88, 87, 86, 85, 84, 83, 82, 81, 
80, 79, 78, 77, 76, 75, 74, 73, 72, 71, 
70, 69, 68, 67, 66, 65, 64, 63, 62, 61, 
60, 59, 58, 57, 56, 55, 54, 53, 52, 51, 
50, 49, 48, 47, 46, 45, 44, 43, 42, 41, 
40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 
30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 
20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 
10, 9, 8, 7, 6, 5, 4, 3, 2, 1
]
"""
