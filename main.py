import copy
import random

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


def gene_rand_vals():
    v9 = [i for i in range(81, 101)]
    # v8 = [i for i in range(81, 91)]
    v7 = [i for i in range(61, 81)]
    # v6 = [i for i in range(61, 71)]
    v5 = [i for i in range(41, 61)]
    random.shuffle(v9)
    # random.shuffle(v8)
    random.shuffle(v7)
    # random.shuffle(v6)
    random.shuffle(v5)
    remain = [i for i in range(1, 41)]
    remain.sort(reverse=True)
    ret = v9 + v7 + v5 + remain
    print(ret)
    return ret


def core(cells):
    """
    Main Algorithm
    """
    final_ans = []

    # ----中央から探すアルゴリズム----------------------------------------------------
    vals = [i for i in range(100, 0, -1)]
    while True:
        if len(vals) == 0:
            break
        target = vals[0]

        # ----Greedy----------------------------------------------------
        # 探索
        if target < 70 and target > 40:
            rank_points = []
            # 適当に100くらいやる
            for y in range(0, H):
                for x in range(0, W):
                    if cells[y][x] == target and cells[y][x] >= 0:
                        dummy_cells = copy.deepcopy(cells)
                        cnt, _ = search_counter(dummy_cells, target, x, y)
                        rank_points.append([cnt, target, (x, y)])

            rank_points.sort(key=lambda x: x[0], reverse=True)
            # 適当に2個くらいやったら探索する
            for i in rank_points[:2]:
                target = i[1]
                x = i[2][0]
                y = i[2][1]
                if cells[y][x] == target and cells[y][x] >= 0:
                    ans, cells = search_reduce([], cells, target, x, y)
                    final_ans.append(ans)
                    ans = []

        # 1
        for y in range(12, 18):
            for x in range(12, 18):
                if cells[y][x] == target and cells[y][x] >= 0:
                    ans, cells = search_reduce([], cells, target, x, y)
                    final_ans.append(ans)
                    if DEBUG_MODE:
                        debug_ans.append([target, ans])
                    ans = []

        # 2
        for y in range(6, 12):
            for x in range(6, 12):
                if cells[y][x] == target and cells[y][x] >= 0:
                    ans, cells = search_reduce([], cells, target, x, y)
                    final_ans.append(ans)
                    if DEBUG_MODE:
                        debug_ans.append([target, ans])
                    ans = []

        # 3
        for y in range(18, 24):
            for x in range(18, 24):
                if cells[y][x] == target and cells[y][x] >= 0:
                    ans, cells = search_reduce([], cells, target, x, y)
                    final_ans.append(ans)
                    if DEBUG_MODE:
                        debug_ans.append([target, ans])
                    ans = []

        # 4
        for y in range(18, 24):
            for x in range(6, 12):
                if cells[y][x] == target and cells[y][x] >= 0:
                    ans, cells = search_reduce([], cells, target, x, y)
                    final_ans.append(ans)
                    if DEBUG_MODE:
                        debug_ans.append([target, ans])
                    ans = []

        # 5
        for y in range(6, 12):
            for x in range(18, 24):
                if cells[y][x] == target and cells[y][x] >= 0:
                    ans, cells = search_reduce([], cells, target, x, y)
                    final_ans.append(ans)
                    if DEBUG_MODE:
                        debug_ans.append([target, ans])
                    ans = []

        # 6
        for y in range(12, 18):
            for x in range(6, 12):
                if cells[y][x] == target and cells[y][x] >= 0:
                    ans, cells = search_reduce([], cells, target, x, y)
                    final_ans.append(ans)
                    if DEBUG_MODE:
                        debug_ans.append([target, ans])
                    ans = []

        # 7
        for y in range(6, 12):
            for x in range(12, 18):
                if cells[y][x] == target and cells[y][x] >= 0:
                    ans, cells = search_reduce([], cells, target, x, y)
                    final_ans.append(ans)
                    if DEBUG_MODE:
                        debug_ans.append([target, ans])
                    ans = []

        # 8
        for y in range(12, 18):
            for x in range(18, 24):
                if cells[y][x] == target and cells[y][x] >= 0:
                    ans, cells = search_reduce([], cells, target, x, y)
                    final_ans.append(ans)
                    if DEBUG_MODE:
                        debug_ans.append([target, ans])
                    ans = []
        
        # 9
        for y in range(18, 24):
            for x in range(12, 18):
                if cells[y][x] == target and cells[y][x] >= 0:
                    ans, cells = search_reduce([], cells, target, x, y)
                    final_ans.append(ans)
                    if DEBUG_MODE:
                        debug_ans.append([target, ans])
                    ans = []

        # 周辺
        for y in range(0, H):
            for x in range(0, W):
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

    # if DEBUG_MODE:
    #     print4cells(cells)

    # Let's go!
    final_ans, cells = core(cells)

    if DEBUG_MODE:
        # print4cells(cells)
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
