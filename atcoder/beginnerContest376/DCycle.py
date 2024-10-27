import sys
from typing import Dict


class WeightedUnionFind:
    def __init__(self, n):
        self.par = [i for i in range(n + 1)]
        self.rank = [0] * (n + 1)
        # 根への距離を管理
        self.weight = [0] * (n + 1)

    # 検索
    def find(self, x):
        if self.par[x] == x:
            return x
        else:
            y = self.find(self.par[x])
            # 親への重みを追加しながら根まで走査
            self.weight[x] += self.weight[self.par[x]]
            self.par[x] = y
            return y

    # 併合
    def union(self, x, y, w):
        rx = self.find(x)
        ry = self.find(y)
        # xの木の高さ < yの木の高さ
        if self.rank[rx] < self.rank[ry]:
            self.par[rx] = ry
            self.weight[rx] = w - self.weight[x] + self.weight[y]
        # xの木の高さ ≧ yの木の高さ
        else:
            self.par[ry] = rx
            self.weight[ry] = -w - self.weight[y] + self.weight[x]
            # 木の高さが同じだった場合の処理
            if self.rank[rx] == self.rank[ry]:
                self.rank[rx] += 1

    # 同じ集合に属するか
    def same(self, x, y):
        return self.find(x) == self.find(y)

    # xからyへのコスト
    def diff(self, x, y):
        return self.weight[x] - self.weight[y]


n, m = map(int, input().split())

result = sys.maxsize
uf = WeightedUnionFind(n)

temp_result_dict: Dict[int, int] = {}

for i in range(m):
    a, b = map(int, input().split())
    if uf.same(a, b):
        temp_result = abs(uf.diff(a, b)) + 1
        root = uf.find(a)
        temp_result_dict[root] = temp_result
    uf.union(a, b, 1)

for k in temp_result_dict:
    if temp_result_dict[k] < result:
        result = temp_result_dict[k]

print(-1 if result == sys.maxsize else result)
