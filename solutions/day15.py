# -*- coding: utf-8 -*-
# @Author: Bobo
# @Date:   2024-12-30 18:23:17

from utils.solution_base import SolutionBase
dirs = {"^": (-1, 0), "v": (1, 0), "<": (0, -1), ">": (0, 1)}

class Solution(SolutionBase):
  dirs = {
        "^": (-1, 0),
        "v": (1, 0),
        "<": (0, -1),
        ">": (0, 1),
  }

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


  def get_robot_pos(self, grid):
    h, w = len(grid), len(grid[0])
    for i in range(h):
      for j in range(w):
        if grid[i][j] == "@":
          return (i, j)

  def resize_grid(self, grid):
    _mappings = {
    "#": "##",
    "O": "[]",
    ".": "..",
    "@": "@.",
    }
    new_grid = [list("".join(_mappings[c] for c in line)) for line in grid]
    return new_grid

  def moving(self, grid, pos, moves, part):
    for move in moves:
      """
      # zip looks nice but way too slow
      ny, nx = (a + b for a, b in zip(pos, self.dirs[move]))
      """
      ny = pos[0] + self.dirs[move][0]
      nx = pos[1] + self.dirs[move][1]

      if grid[ny][nx] == ".":
        pos = (ny, nx)
      elif grid[ny][nx] == "#":
        continue
      else:
        edges, adjs = self.get_adjs_and_edges(grid, pos, move, part)
        blocked = 0
        dy, dx = self.dirs[move]
        for box in edges:
          ny, nx = (box[0] + dy, box[1] + dx)
          if grid[ny][nx] == "#":
            blocked += 1
        if blocked == 0:
          grid = self.update_grid(grid, adjs, move)
          pos = (pos[0] + dy, pos[1] + dx)
    return grid

  def get_adjs_and_edges(self, grid, pos, move, part=1):
    y, x = pos
    dy, dx = self.dirs[move]

    adjs = set()
    if part == 1 or move in "<>":
      while True:
        ny, nx = y + dy, x + dx
        if grid[ny][nx] in ".#":
          return [(ny - dy, nx - dx)], adjs
        y = ny
        x = nx
        adjs.add((y, x))
    else:
      edges = []
      queue = [(y, x)]
      while queue:
        y, x = queue.pop(0)
        if (y, x) in adjs:
          continue
        adjs.add((y, x))
        ny, nx = y + dy, x + dx
        if grid[ny][nx] in ".#":
          edges.append((y, x))
        elif grid[ny][nx] == "[":
          queue.append((ny, nx))
          queue.append((ny, nx + 1))
        elif grid[ny][nx] == "]":
          queue.append((ny, nx))
          queue.append((ny, nx - 1))

    return edges, adjs - {(pos[0], pos[1])}
  
  def update_grid(self, grid, adjs, move):
    sorted_coords = []

    # sort coords from the edge to the robot's position
    match move:
      case "^":
        sorted_coords = sorted(adjs, key=lambda x: x[0])
      case "v":
        sorted_coords = sorted(adjs, key=lambda x: x[0], reverse=True)
      case "<":
        sorted_coords = sorted(adjs, key=lambda x: x[1])
      case ">":
        sorted_coords = sorted(adjs, key=lambda x: x[1], reverse=True)

    dy, dx = self.dirs[move]
    for coord in sorted_coords:
      y, x = coord
      ny, nx = y + dy, x + dx
      grid[ny][nx] = grid[y][x]
      grid[y][x] = "."

    return grid
  
  def get_coords_sum(self, grid, part=1):
    box = "[" if part == 2 else "O"
    rows, cols = len(grid), len(grid[0])

    _sum = sum(100 * y + x for y in range(rows) for x in range(cols) if grid[y][x] == box)
    return _sum

  def part2(self, data):
    pos = data.index("")
    grid, moves = [list(row) for row in data[:pos]], list("".join(data[pos+1:]))

    grid = self.resize_grid(grid)
    pos = self.get_robot_pos(grid)
    grid[pos[0]][pos[1]] = "."

    grid = self.moving(grid, pos, moves, 2)
    _sum = self.get_coords_sum(grid, 2)

    return _sum
