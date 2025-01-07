# -*- coding: utf-8 -*-
# @Author: Bobo
# @Date:   2024-12-28 12:42:05

from utils.solution_base import SolutionBase
from collections import defaultdict

class Solution(SolutionBase):
  def part1(self, data):
    antennas = self.find_antennas(data)
    signal = set()
    for loc in antennas.values():
      l = len(loc)
      for l1 in range(l):
        for l2 in range(l1+1,l):
          x1, y1 = loc[l1]
          x2, y2 = loc[l2]
          dx, dy = x2-x1, y2-y1
          nx1, ny1 = x1-dx, y1-dy
          nx2, ny2 = x2+dx, y2+dy
          if 0 <= nx1 < len(data) and 0 <= ny1 < len(data[0]):
            signal.add((nx1, ny1))
          if 0 <= nx2 < len(data) and 0 <= ny2 < len(data[0]):
            signal.add((nx2, ny2))
    return len(signal) 

  def part2(self, data):
    antennas = self.find_antennas(data)
    signal = set()
    for loc in antennas.values():
      l = len(loc)
      for i in range(l):
        for j in range(i+1, l):
          diff = tuple(y-x for x, y in zip(loc[i],loc[j]))
          for idx, _dir in [(i, 1), (j, -1)]:
            pos = loc[idx]
            while 0 <= pos[0] < len(data) and 0 <= pos[1] < len(data[0]):
              signal.add(pos)
              pos = tuple(p-_dir*d for d, p in zip(diff, pos))
    return len(signal)

  def find_antennas(self, _map):
    antennas = defaultdict(list)
    h, w = len(_map), len(_map[0])
    for i in range(h):
      for j in range(w):
        if _map[i][j] != '.':
          antennas[_map[i][j]].append((i,j))

    return antennas
