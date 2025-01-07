# -*- coding: utf-8 -*-
# @Author: Bobo
# @Date:   2024-12-30 12:18:15

from utils.solution_base import SolutionBase

class Solution(SolutionBase):
  memo = {}
  def blink(self, stone, times):
    if times == 0:
      return 1

    if (stone, times) in self.memo.keys():
      return self.memo[(stone,times)]

    if stone == 0:
      size = self.blink(1, times-1)
    else:
      stone_str = str(stone)
      stone_digit = len(stone_str)
      if stone_digit %2 == 0:
        size = self.blink(int(stone_str[:stone_digit//2]), times-1) + self.blink(int(stone_str[stone_digit//2:]), times-1)
      else:
        size = self.blink(stone*2024, times-1)

    self.memo[(stone,times)] = size
    return size

  def part1(self, data):
    stones = map(int, data[0].split())
    res = sum(self.blink(stone, 25) for stone in stones)
    return res

  def part2(self, data):
    stones = map(int, data[0].split())
    res = sum(self.blink(stone, 75) for stone in stones)
    return res