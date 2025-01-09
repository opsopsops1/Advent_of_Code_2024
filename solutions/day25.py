# -*- coding: utf-8 -*-
# @Author: Bobo
# @Date:   2025-01-08 16:20:43

from utils.solution_base import SolutionBase

class Solution(SolutionBase):
  def part1(self, data):
    data = "\n".join(data).split("\n\n")
    locks, keys = [], []
    for pic in data:
      pic2 = pic.split("\n")
      height = []
      
      for r in zip(*pic2):
        height.append(r.count("#")-1)
        
      if pic[0] == "#":
        locks.append(height)
      else:
        keys.append(height)
    
    count = sum(all(c <= 5 for c in [a+b for a, b in zip(l, k)]) for l in locks for k in keys)
    return count
    
  def part2(self, data):
    pass