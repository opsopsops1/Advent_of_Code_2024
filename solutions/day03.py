# -*- coding: utf-8 -*-
# @Author: Bobo
# @Date:   2024-12-26 17:54:56

from utils.solution_base import SolutionBase
import re

class Solution(SolutionBase):
  def part1(self, data):
    pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
    match = re.findall(pattern, "".join(data))
    return sum(int(x)*int(y) for x, y in match)

  def part2(self, data):
    pattern = r"(mul\((\d{1,3}),(\d{1,3})\)|do\(\)|don't\(\))"
    match = re.findall(pattern, "".join(data))

    enabled = True
    res = 0
    for line in match:
      if line[0] == "do()":
        enabled = True
      elif line[0] == "don't()":
        enabled = False
      else:
        if enabled:
          res += int(line[1])*int(line[2])
    return res

