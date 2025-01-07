# -*- coding: utf-8 -*-
# @Author: Bobo
# @Date:   2025-01-06 12:27:39

from utils.solution_base import SolutionBase
from queue import Queue

dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

class Solution(SolutionBase):
  size = None
  grid = None
  corrupted = None
  corrupted_len = None

  def parse_data(self, data):
    self.corrupted = [tuple(map(int, line.split(","))) for line in data]
    self.size = 71
    self.corrupted_len = 1024
    if len(self.corrupted) == 25:
      self.size = 7
      self.corrupted_len = 12
      
  def get_grid(self):
    self.grid = [["."] * self.size for h in range(self.size)]
    for x, y in self.corrupted[:self.corrupted_len]:
      self.grid[y][x] = '#'
    
  def bfs(self):
    dist = [[100000] * self.size for h in range(self.size)]
    dist[0][0] = 0
    q = Queue()
    q.put((0, 0))

    while not q.empty():
      x, y = q.get()
      d = dist[y][x]

      for dx, dy in dirs:
        nx, ny = x+dx, y+dy
        if self.size > nx >= 0 and self.size > ny >= 0 and self.grid[ny][nx] == '.' and dist[ny][nx] > d + 1:
          dist[ny][nx] = d + 1
          q.put((nx, ny))
    return dist

  def bfs2(self, seen, p):
    q = Queue()
    q.put(p)
    while not q.empty():
      x, y = q.get()
      seen.add((x, y))
      for dx, dy in dirs:
        nx, ny = x+dx, y+dy
        if nx < 0 or ny < 0 or nx >= self.size or ny >= self.size:
          continue
        if self.grid[ny][nx] == '#':
          continue
        if (nx, ny) in seen:
          continue
        q.put((nx, ny))
    return seen

  def part1(self, data):
    self.parse_data(data)
    self.get_grid()
    dist = self.bfs()
    return dist[self.size-1][self.size-1]

  def part2(self, data):
    self.parse_data(data)
    self.corrupted_len = len(self.corrupted)
    self.get_grid()
    seen = set()
    seen = self.bfs2(seen, (0, 0))

    for i in range(self.corrupted_len-1, -1, -1):
      x, y = self.corrupted[i]
      self.grid[y][x] = '.'
      view = False
      for dx, dy in dirs:
        nx, ny = x+dx, y+dy
        if (nx, ny) in seen:
          view = True
      if view:
        seen = self.bfs2(seen, (x, y))
        if (self.size-1, self.size-1) in seen:
          return ",".join(map(str, self.corrupted[i]))
