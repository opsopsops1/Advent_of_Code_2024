# -*- coding: utf-8 -*-
# @Author: Bobo
# @Date:   2024-12-30 14:40:16

from utils.solution_base import SolutionBase

dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

class Solution(SolutionBase):
  def parse_data(self, data):
    grid = []
    cord_by_type = {}
    h, w = len(data), len(data[0])
    for x in range(h):
      line = list(data[x].strip())
      grid.append(line)
      for y in range(w):
        _type = data[x][y]
        if _type not in cord_by_type:
          cord_by_type[_type] = set()
        cord_by_type[_type].add((x, y))
    return grid, cord_by_type

  def get_curr_group(self, grid, cord):
    _type = grid[cord[0]][cord[1]]
    h, w = len(grid), len(grid[0])

    adj = set()
    stack = [cord]
    while stack:
      x, y = stack.pop()
      if (x, y) in adj:
        continue

      adj.add((x, y))
      for dx, dy in dirs:
        nx, ny = x+dx, y+dy
        if 0 <= nx < h and 0 <= ny < w and grid[nx][ny] == _type:
          stack.append((nx, ny))
    return adj

  def part1(self, data):
    grid, cord_by_type = self.parse_data(data)
    types = cord_by_type.keys()

    def get_connected_count(grid, cord):
      h, w = len(grid), len(grid[0])
      x, y = cord
      count = 0
      for dx, dy in dirs:
        nx, ny = x+dx, y+dy
        if 0 <= nx < h and 0 <= ny < w and grid[x][y] == grid[nx][ny]:
          count += 1
      return count
    
    prices = {}
    for _type in types:
      prices[_type] = 0
      cords = cord_by_type[_type]

      while cords:
        curr = cords.pop()
        curr_group = self.get_curr_group(grid, curr)
        cords -= curr_group
        connected_count = {}
        for cord in curr_group:
          connected_count[cord] = get_connected_count(grid, cord)

        price = len(curr_group) * (len(curr_group)*4 - sum(connected_count.values()))
        prices[_type] += price
    return sum(prices.values())


  def part2(self, data):
    grid, cord_by_type = self.parse_data(data)
    types = cord_by_type.keys()

    def get_group_side(group):
      min_x = min(group, key=lambda x: x[0])[0]
      max_x = max(group, key=lambda x: x[0])[0]
      min_y = min(group, key=lambda x: x[1])[1]
      max_y = max(group, key=lambda x: x[1])[1]
      h, w = max_x-min_x+1, max_y-min_y+1
      new_group = [(x-min_x, y-min_y) for x, y in group]

      grid = [[" " for y in range(w+2)] for x in range(h+2)]
      for x, y in new_group:
        grid[x+1][y+1] = 'O'
      
      sides = 0
      for t in [0, 1]:
        for x in range(1, h+1):
          sides += len("".join(["-" if above!=curr and curr=="O" else " " for above, curr in zip(grid[x-1], grid[x])]).split())
          sides += len("".join(["-" if below!=curr and curr=="O" else " " for below, curr in zip(grid[x+1], grid[x])]).split())

        # rotate
        grid = list(zip(*grid[::-1]))
        h, w = w, h

      return sides

    prices = {}
    for _type in types:
      prices[_type] = 0
      cords = cord_by_type[_type]

      while cords:
        curr = cords.pop()
        curr_group = self.get_curr_group(grid, curr)
        cords -= curr_group
        
        group_side = get_group_side(curr_group)
        price = len(curr_group) * group_side
        prices[_type] += price
        

    return sum(prices.values())