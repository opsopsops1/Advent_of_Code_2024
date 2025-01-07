# -*- coding: utf-8 -*-
# @Author: Bobo
# @Date:   2024-12-27 12:32:15

from utils.solution_base import SolutionBase

class Solution(SolutionBase):
  def part1(self, data):
    result = []
    for line in data:
      t, e = line.split(": ")
      t = int(t)
      ex = list(map(int,e.split()))
      exx = ex[:]
      possible =es = [exx.pop(0)]
      while exx:
        cur = exx.pop(0)
        tmp = []
        for p in possible:
          tmp.append(cur+p)
          tmp.append(cur*p)
        possible = tmp
      if t in possible:
        result.append(t)
      
    return sum(result)

  def part2(self, data):
    result = []
    for line in data:
      t, e = line.split(": ")
      t = int(t)
      ex = list(map(int,e.split()))
      exx = ex[:]
      possible =es = [exx.pop(0)]
      while exx:
        cur = exx.pop(0)
        tmp = []
        for p in possible:
          tmp.append(p+cur)
          tmp.append(p*cur)
          nx = int(str(p)+str(cur))
          if nx <= t:
            tmp.append(nx)
        possible = tmp
      if t in possible:
        result.append(t)
      
    return sum(result)

