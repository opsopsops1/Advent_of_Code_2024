# -*- coding: utf-8 -*-
# @Author: Bobo
# @Date:   2024-12-26 12:09:00

from utils.solution_base import SolutionBase

class Solution(SolutionBase):
  def part1(self, data):
    l, r = zip(*[map(int, line.split()) for line in data])
    dist = sum([abs(x-y) for x, y in zip(sorted(l), sorted(r))])
    return dist

  def part2(self, data):
    l, r = zip(*[map(int, line.split()) for line in data])
    sim = sum([x*r.count(x) for x in l])
    return sim