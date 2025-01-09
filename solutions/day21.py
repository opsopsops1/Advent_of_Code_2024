# -*- coding: utf-8 -*-
# @Author: Bobo
# @Date:   2025-01-06 23:17:53

from utils.solution_base import SolutionBase
from collections import defaultdict
from functools import cache


keypad1 = ["789", "456", "123", "#0A"]
keypad2 = ["#^A", "<v>"]

class Solution(SolutionBase):
  def get_keypad_step(self, keypad):
    moves = defaultdict(list)
    if keypad[0][0] == "#":
      nosign_x = 0
    else:
      nosign_x = len(keypad)-1
    for x1, row1 in enumerate(keypad):
      for y1, c1 in enumerate(row1):
        for x2, row2 in enumerate(keypad):
          for y2, c2 in enumerate(row2):
            if c1 == "#" or c2 == "#" or c1 == c2:
              continue

            if x1 == x2:
              d = ">" if y2 > y1 else "<"
              moves[c1+c2].append(d*abs(y2-y1)+"A")
            elif y1 == y2:
              d = "v" if x2 > x1 else "^"
              moves[c1+c2].append(d*abs(x2-x1)+"A")
            else:
              d1 = ">" if y2 > y1 else "<"
              d2 = "v" if x2 > x1 else "^"
              
              if y2 != 0 or (x1 != nosign_x):
                moves[c1+c2].append(d1*abs(y2-y1)+d2*abs(x2-x1)+"A")
              if y1 != 0 or (x2 != nosign_x):
                moves[c1+c2].append(d2*abs(x2-x1)+d1*abs(y2-y1)+"A")
               
    return moves

  def build_moves(self, move, current=[], idx=0):
    if len(move) == idx:
      return [current]

    results = []
    for value in move[idx]:
      new_result = self.build_moves(move, current + [value], idx+1)
      results.extend(new_result)

    return results

  def press_keypad(self, key, move):
    code = "A" + key
    moves = [move[a+b] if a!=b else "A" for a, b in zip(code, code[1:])]
    moves = self.build_moves(moves)
    return moves
    

  @cache
  def translate_step_length(self, key, times):
    if key[0].isnumeric():
      moves = self.press_keypad(key, self.move_1)
    else:
      moves = self.press_keypad(key, self.move_2)

    if times == 0:
      return min([sum(map(len, move)) for move in moves])
    else:
      return min([sum(self.translate_step_length(curr_code, times - 1) for curr_code in move) for move in moves])



  def part1(self, data):
    self.move_1 = self.get_keypad_step(keypad1)
    self.move_2 = self.get_keypad_step(keypad2)

    total = 0
    for line in data:
      min_len = self.translate_step_length(line, 2)
      num = int(line[:-1])
      total += min_len * num
    return total

  def part2(self, data):
    self.move_1 = self.get_keypad_step(keypad1)
    self.move_2 = self.get_keypad_step(keypad2)

    total = 0
    for line in data:
      min_len = self.translate_step_length(line, 25)
      num = int(line[:-1])
      total += min_len * num
    return total