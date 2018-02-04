DEBUG_MODE = 1
debug_ans = []


def exit():
    import sys
    sys.exit()


class Solver():
    def __init__(self, cells):
        self.cells = cells
        self.directions = [(0, -1), (-1, 0), (0, 1), (1, 0)]
        self.w = 30
        self.h = 30
        self.final_ans = []

    def run(self):
        target = self.search_top()
        while target is not None:
            x = target[0]
            y = target[1]

            ans = self.reduce_cell([], x, y)
            self.final_ans.append(ans)

            # 更新
            target = self.search_top()

    def reduce_cell(self, ans, x, y):
        """
        再帰関数
        """
        org_v = self.cells[y][x]

        self.cells[y][x] = self.cells[y][x] - 1
        ans.append(y)
        ans.append(x)

        for d in self.directions:
            v = org_v - 1
            if v == 0:
                continue
            dx = x + d[0]
            dy = y + d[1]
            # 境界チェック、かつ、値のチェック
            if self.check_border(dx, dy) and self.cells[dy][dx] == v:
                ans = self.reduce_cell(ans, dx, dy)
            return ans
        return ans

    def run2(self):
        p = self.search_top()
        while p is not None:
            while True:
                x = p[0]
                y = p[1]
                self.final_ans.append([y, x])
                # self.final_ans.append(x)
                self.cells[y][x] = self.cells[y][x] - 1

                next_p = None
                for d in self.directions:
                    nx = x + d[0]
                    ny = y + d[1]
                    if not self.check_border(nx, ny):
                        continue
                    if self.cells[y][x] == self.cells[ny][nx] and self.cells[ny][nx] > 0:
                        next_p = (nx, ny)
                        break
                if next_p is not None:
                    target = next_p
                    continue
                break

            # 更新
            p = self.search_top()

    def compare_around(self, x, y):
        """
        (x, y)の上下左右を探索し、周囲より値が高ければTrue
        """
        for d in self.directions:
            dx = x + d[0]
            dy = y + d[1]
            if not self.check_border(dx, dy):
                continue
            if self.cells[y][x] < self.cells[dy][dx]:
                return False
        return True

    def search_top(self):
        """
        探索して、山のてっぺんを見つけたらその座標を返す。それ以外はNone
        """
        for y in range(0, self.h):
            for x in range(0, self.w):
                if (self.cells[y][x] <= 0):
                    continue
                if self.compare_around(x, y):
                    return (x, y)
        return None

    def check_border(self, x, y):
        if x < 0 or x > self.w - 1:
            return False
        elif y < 0 or y > self.h - 1:
            return False
        else:
            return True


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
    for y in lines:
        tmp = []
        for x in y.split(" "):
            tmp.append(int(x))
        cells.append(tmp)

    if DEBUG_MODE:
        print4cells(cells)

    # Let's go!
    solver = Solver(cells)
    solver.run2()

    cells = solver.cells
    final_ans = solver.final_ans

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
