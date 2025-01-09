# -*- coding: utf-8 -*-
# @Author: Bobo
# @Date:   2025-01-08 00:26:12

from utils.solution_base import SolutionBase
from collections import defaultdict

MOD = 16777216

class Solution(SolutionBase):
  def processing(self, x):
    x = ((x*64)^x)%MOD
    x = (x//32)^x
    x = ((x*2048)^x)%MOD
    return x
  def part1(self, data):
    total = 0
    for line in data:
      x = int(line)
      for t in range(2000):
        x = self.processing(x)
      total += x
    return total

  def part2(self, data):
    prices = []
    for x in map(int, data):
      price = []
      for _ in range(2000):
        x = ((x*64)^x)%MOD
        x = ((x//32)^x)%MOD
        x = ((x*2048)^x)%MOD
        price.append(x%10)
      prices.append(price)

    diff = [[b-a for a, b in zip(price, price[1:])] for price in prices]

    amounts = defaultdict(int)
    for buyer_idx, d in enumerate(diff):
      keys = set()
      for i in range(len(d)-3):
        key = tuple(d[i:i+4])
        if key in keys:
          continue
        amounts[key] += prices[buyer_idx][i+4]
        keys.add(key)
    return max(amounts.values())
