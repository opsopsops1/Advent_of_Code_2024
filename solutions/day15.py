# -*- coding: utf-8 -*-
# @Author: Bobo
# @Date:   2024-12-30 18:23:17

from utils.solution_base import SolutionBase
dirs = {"^": (-1, 0), "v": (1, 0), "<": (0, -1), ">": (0, 1)}

class Solution(SolutionBase):
  def part1(self, data):
    _map, move = "\n".join(data).split("\n\n")
    _map, move = [*map(list, _map.split("\n"))], move.replace("\n", "")
    h, w = len(_map), len(_map[0])
    sx, sy = 0, 0
    for i in range(h):
      for j in range(w):
        if _map[i][j] == '@':
          sx, sy = j, i

    for m in move:
      dy, dx = dirs[m]
      nx, ny = sx+dx, sy+dy
      while 0 <= ny < h and 0 <= nx < w and _map[ny][nx] == 'O':
        nx, ny = nx+dx, ny+dy
      if _map[ny][nx] == '#':
        continue
      _map[sy][sx] = '.'
      sx, sy = sx+dx, sy+dy
      if _map[sy][sx] == 'O':
        _map[ny][nx] = 'O'
      _map[sy][sx] = '@'
      
    box_gps = []
    for i in range(h):
      for j in range(w):
        if _map[i][j] == 'O':
          box_gps.append((j, i))
    sum_gps = 0
    for x, y in box_gps:
      sum_gps += x + 100*y
    return sum_gps

  def part2(self, data):
    pass