# -*- coding: utf-8 -*-
# @Author: Bobo
# @Date:   2024-12-26 15:15:09

from utils.solution_base import SolutionBase

class Solution(SolutionBase):
  def part1(self, data):
    res = 0
    report = [list(map(int, line.split())) for line in data]
    for l in report:
      if self.is_safe(l):
        res += 1
    return res

  def part2(self, data):
    res = 0
    for report in data:
      level = [*map(int, report.split())]
      if self.is_safe(level):
        res += 1
      else:
        for i in range(len(level)):
          new_level = level[:i] + level[i+1:]
          if self.is_safe(new_level):
            res += 1
            break
    return res

  def is_safe(self, level):
    diff = [a-b for a, b in zip(level, level[1:])]
    is_monotonic = all(i>0 for i in diff) or all(i < 0 for i in diff)
    is_inrange = all(1<=abs(i)<=3 for i in diff)
    return is_monotonic and is_inrange