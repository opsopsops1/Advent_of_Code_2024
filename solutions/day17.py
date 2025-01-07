# -*- coding: utf-8 -*-
# @Author: Bobo
# @Date:   2025-01-05 22:17:42

from utils.solution_base import SolutionBase

class Solution(SolutionBase):
  def part1(self, data):
    reg, p = "\n".join(data).split("\n\n")
    a, b, c = [int(line.split(": ")[1]) for line in reg.split("\n")]
    program = list(map(int, p.split(": ")[1].split(",")))
    ptr = 0
    out = []
    while ptr < len(program):
      p1, op, flag = program[ptr], program[ptr+1], 1
      if p1 not in [1, 3, 4]:
        op = (op if op < 4 else [a, b, c][op-4])

      if p1 == 0:
        a >>= op
      elif p1 == 1:
        b ^= op
      elif p1 == 2:
        b = op%8
      elif p1 == 3:
        if a != 0:
          ptr = op
          flag = 0
      elif p1 == 4:
        b ^= c
      elif p1 == 5:
        out.append(str(op%8))
      elif p1 == 6:
        b = a>>op
      else:
        c = a>>op
      if flag:
        ptr += 2

    return ",".join(out)



  def part2(self, data):
    reg, p = "\n".join(data).split("\n\n")
    program = p.split(": ")[1]
    program_line = list(map(int, program.split(",")))
    def run_program(reg, program):
      ptr = 0
      out = []
      a, b, c = reg
      while ptr < len(program):
        p1, op = program[ptr], program[ptr+1]
        if p1 not in [1, 3, 4]:
          op = (op if op < 4 else [a, b, c][op-4])

        if p1 == 0:
          a >>= op
        elif p1 == 1:
          b ^= op
        elif p1 == 2:
          b = op%8
        elif p1 == 3:
          if a != 0:
            ptr = op
            continue
        elif p1 == 4:
          b ^= c
        elif p1 == 5:
          out.append(op%8)
        elif p1 == 6:
          b = a>>op
        else:
          c = a>>op
        ptr += 2
      return out

    # for i in range(80):
    #   result = run_program([i, 0, 0], program_line)
    #   print(i, result)

    A = sum(7 * 8**i for i in range(len(program_line) - 1)) + 1
    while True:
      result = run_program([A, 0, 0], program_line)

      if result == program_line:
        return A

      add = 0
      for i in range(len(result) - 1, -1, -1):
        if result[i] != program_line[i]:
          add = 8**i
          A += add
          break
