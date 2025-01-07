# -*- coding: utf-8 -*-
# @Author: Bobo
# @Date:   2025-01-06 14:31:39

from utils.solution_base import SolutionBase
from collections import defaultdict

class Solution(SolutionBase):
  def is_valid(self, patterns, towel):
    def matching_pos(pos):
      if pos == len(patterns):
        return True

      for t in towel:
        next_pos = pos + len(t)
        if next_pos <= len(patterns) and patterns[pos:next_pos] == t:
          if matching_pos(next_pos):
            return True
      return False
    return matching_pos(0)

  def count_valid_design(self, patterns, towel):
    memo = defaultdict(int)
    def matching_pos(pos):
      if pos == len(patterns):
        return 1

      if pos in memo:
        return memo[pos]

      matches = 0

      for t in towel:
        next_pos = pos + len(t)
        if next_pos <= len(patterns) and patterns[pos:next_pos] == t:
          matches += matching_pos(next_pos)

      memo[pos] = matches
            
      return matches

    return matching_pos(0)

  def part1(self, data):
    towel = sorted(data[0].split(", "), key=len)
    patterns = data[2:]

    count = 0
    for line in patterns:
      if self.is_valid(line, towel):
        count += 1

    return count

  def part2(self, data):
    towel = sorted(data[0].split(", "), key=len)
    patterns = data[2:]

    count = 0
    for line in patterns:
      count += self.count_valid_design(line, towel)

    return count