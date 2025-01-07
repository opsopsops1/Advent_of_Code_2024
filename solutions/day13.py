# -*- coding: utf-8 -*-
# @Author: Bobo
# @Date:   2024-12-30 15:53:51

from utils.solution_base import SolutionBase

class Solution(SolutionBase):
  def part1(self, data):
    machines = "\n".join(data).split("\n\n")
    tokens = 0
    for machine in machines:
      str_a, str_b, str_p = machine.split("\n")
      b_a = [*map(lambda x: int(x[2:]), str_a.split(": ")[1].split(", "))]
      b_b = [*map(lambda x: int(x[2:]), str_b.split(": ")[1].split(", "))]
      prize = [*map(lambda x: int(x[2:]), str_p.split(": ")[1].split(", "))]

      times_b = (prize[0]*b_a[1]-prize[1]*b_a[0]) / (b_b[0]*b_a[1]-b_b[1]*b_a[0])
      times_a = (prize[0]-times_b*b_b[0]) / b_a[0]
      if 0 <= times_a <= 100 and 0 <= times_b <= 100 and times_a.is_integer() and times_b.is_integer():
        tokens += int(3*times_a + times_b)
    return tokens


  def part2(self, data):
    machines = "\n".join(data).split("\n\n")
    tokens = 0
    for machine in machines:
      str_a, str_b, str_p = machine.split("\n")
      b_a = [*map(lambda x: int(x[2:]), str_a.split(": ")[1].split(", "))]
      b_b = [*map(lambda x: int(x[2:]), str_b.split(": ")[1].split(", "))]
      prize = [*map(lambda x: int(x[2:])+10000000000000, str_p.split(": ")[1].split(", "))]

      times_b = (prize[0]*b_a[1]-prize[1]*b_a[0]) / (b_b[0]*b_a[1]-b_b[1]*b_a[0])
      times_a = (prize[0]-times_b*b_b[0]) / b_a[0]
      if times_a.is_integer() and times_b.is_integer():
        tokens += int(3*times_a + times_b)
    return tokens