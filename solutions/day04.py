# -*- coding: utf-8 -*-
# @Author: Bobo
# @Date:   2024-12-26 20:03:38

from utils.solution_base import SolutionBase

class Solution(SolutionBase):
  def part1(self, data):
    res = 0
    h = len(data)
    w = len(data[0])
    for i in range(h):
      for j in range(w):
        if j < w-3:
          if data[i][j:j+4] == "XMAS" or data[i][j:j+4] == "SAMX":
            res += 1
        if i < h-3:
          if (data[i][j] == 'X' and data[i+1][j] == 'M' and data[i+2][j] == 'A' and data[i+3][j] == 'S') or (data[i][j] == 'S' and data[i+1][j] == 'A' and data[i+2][j] == 'M' and data[i+3][j] == 'X'):
            res += 1
        if j < w-3 and i < h-3:
          if (data[i][j] == 'X' and data[i+1][j+1] == 'M' and data[i+2][j+2] == 'A' and data[i+3][j+3] == 'S') or (data[i][j] == 'S' and data[i+1][j+1] == 'A' and data[i+2][j+2] == 'M' and data[i+3][j+3] == 'X'):
            res += 1
        if j >= 3 and i < h-3:
          if (data[i][j] == 'X' and data[i+1][j-1] == 'M' and data[i+2][j-2] == 'A' and data[i+3][j-3] == 'S') or (data[i][j] == 'S' and data[i+1][j-1] == 'A' and data[i+2][j-2] == 'M' and data[i+3][j-3] == 'X'):
            res += 1

    return res

  def part2(self, data):
    res = 0
    h = len(data)
    w = len(data[0])
    for i in range(1,h-1):
      for j in range(1,w-1):
        if ((data[i-1][j-1] == 'M' and data[i][j] == 'A' and data[i+1][j+1] == 'S') or (data[i-1][j-1] == 'S' and data[i][j] == 'A' and data[i+1][j+1] == 'M')) and ((data[i-1][j+1] == 'M' and data[i][j] == 'A' and data[i+1][j-1] == 'S') or (data[i+1][j-1] == 'M' and data[i][j] == 'A' and data[i-1][j+1] == 'S')):
          res += 1
    return res

