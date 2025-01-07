# -*- coding: utf-8 -*-
# @Author: Bobo
# @Date:   2024-12-28 18:05:14

from utils.solution_base import SolutionBase
from queue import Queue

class Solution(SolutionBase):
  def get_endpoint(self, _map, i, j):
    h, w = len(_map), len(_map[0])
    dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    endpoints = []
    q = Queue()
    q.put((i,j))
    while not q.empty():
      si, sj = q.get()
      nxt = _map[si][sj]+1

      for d_i, d_j in dirs:
        ni = si + d_i
        nj = sj + d_j
        if 0 <= ni < h and 0 <= nj < w and _map[ni][nj] == nxt:
          if nxt == 9:
            endpoints.append((ni,nj))
          else:
            q.put((ni,nj))
    return endpoints


  def part1(self, data):
    _map = [list(map(int, line)) for line in data]
    h, w = len(_map), len(_map[0])
    res = 0
    
    for i in range(h):
      for j in range(w):
        if _map[i][j] == 0:
          res += len(set(self.get_endpoint(_map, i, j)))

    return res

  def part2(self, data):
    _map = [list(map(int, line)) for line in data]
    h, w = len(_map), len(_map[0])
    res = 0
    
    for i in range(h):
      for j in range(w):
        if _map[i][j] == 0:
          res += len(self.get_endpoint(_map, i, j))

    return res