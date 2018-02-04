#include <iostream>
#include <string>
#include <vector>
#include <array>

using namespace std;

typedef struct Point {
  int x;
  int y;
} POINT;

class Solver {
private:
  const int w;
  const int h;
  vector< vector<int> > cells;
  array<int, 4> dxs{0, -1, 0, 1};
  array<int, 4> dys{-1, 0, 1, 0};

public:
  Solver() : w(30), h(30) {
    cells.resize(h);
  }

  void input() {
    int s;
    for (int y = 0; y < h; y++) {
      for (int x = 0; x < w; x++) {
        cin >> s;
        cells[y].push_back(s);
      }
    }
  }

  void run() {
    array<int, 2> p = search_top();
    while ((p[0] >= 0 && p[1] >= 0)) {
      while (1) {
        int x = p[0];
        int y = p[1];
        cout << y+1 << " " << x+1 << endl;
        cells[y][x] = cells[y][x] - 1;

        array<int , 2> next{-1, -1};
        for (int i = 0; i < 4; i++) {
          int nx = x + dxs[i];
          int ny = y + dys[i];
          if (!check_border(nx, ny)) {
            continue;
          }
          if ((cells[y][x] == cells[ny][nx]) && (cells[ny][nx] > 0)) {
            next[0] = nx;
            next[1] = ny;
            break;
          }
        }
        if (next[0] >= 0 && next[1] >= 0) {
          p = next;
          continue;
        }
        break;
      }
      // 更新
      p = search_top();
    }
  }

  bool compare_around(int x, int y) {
    for (int i = 0; i < 4; i++) {
      int nx = x + dxs[i];
      int ny = y + dys[i];
      if (!check_border(nx, ny)) {
        continue;
      }
      if (cells[y][x] < cells[ny][nx]) {
        return false;
      }
    }
    return true;
  }

  array<int, 2> search_top() {
    array<int, 2> point;
    for (int y = 0; y < h; y++) {
      for (int x = 0; x < w; x++) {
        if (cells[y][x] <= 0) {
          continue;
        }
        if (compare_around(x, y)) {
          point[0] = x;
          point[1] = y;
          return point;
        }
      }
    }
    point[0] = -1;
    point[1] = -1;
    return point;
  }

  bool check_border(int x, int y) {
    if (x < 0 || x >= w || y < 0 || y >= h) {
      return false;
    }
    return true;
  }
};

int main() {
  Solver solver;
  solver.input();
  solver.run();

  return 0;
}
