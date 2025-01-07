# -*- coding: utf-8 -*-
# @Author: Bobo
# @Date:   2024-12-26 20:30:23

from utils.solution_base import SolutionBase
from collections import defaultdict
import functools

class Solution(SolutionBase):
  def part1(self, data):
    rules, updates = self.extract_data(data)
    res = 0

    for u in updates:
      if self.is_valid(rules, u):
        res += u[len(u)//2]
    return res

  def part2(self, data):
    rules, updates = self.extract_data(data)
    res = 0

    for u in updates:
      if not self.is_valid(rules, u):
        new_u = self.fix_updates(rules, u)

        res += new_u[len(new_u)//2]
    return res

  def extract_data(self, data):
    sep = data.index('')

    rules = defaultdict(set)
    for line in data[:sep]:
      a, b = map(int, line.split('|'))
      rules[a].add(b)

    updates = [list(map(int,u.split(',')))  for u in data[sep+1:]]
    return rules, updates
  
  def is_valid(self, rules, update):
    for i in range(len(update)):
      for j in range(i+1, len(update)):
        if update[j] not in rules[update[i]]:
          return False
    return True
  
  def fix_updates(self, rules, update):
    order = defaultdict(int)
    for i in range(len(update)):
      for j in range(len(update)):
        if i == j:
          continue
        if update[j] in rules[update[i]]:
          order[update[i]] += 1
    new_u = sorted(update, key=lambda x: order[x], reverse = True)
    return new_u