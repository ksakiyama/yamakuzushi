DEBUG_MODE = 0


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
        p = self.search_top()
        while p is not None:
            while True:
                x = p[0]
                y = p[1]
                self.final_ans.append([y, x])
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
    solver.run()

    final_ans = solver.final_ans

    if DEBUG_MODE:
        cells = solver.cells
        print4cells(cells)
        with open("debug.txt", "w") as f:
            for ans in final_ans:
                line = " ".join(str(i+1) for i in ans)
                f.write(line + "\n")
    else:
        for ans in final_ans:
            line = " ".join(str(i+1) for i in ans)
            print(line)

    return 0


if __name__ == "__main__":
    main()
