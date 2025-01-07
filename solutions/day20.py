# -*- coding: utf-8 -*-
# @Author: Bobo
# @Date:   2025-01-06 16:41:02

from utils.solution_base import SolutionBase
from queue import Queue

dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

class Solution(SolutionBase):
  def find_shortest_path(self, _map):
    h, w = len(_map), len(_map[0])
    start, end = None, None
    for i in range(h):
      for j in range(w):
        if _map[i][j] == 'S':
          start = (i, j)
        if _map[i][j] == 'E':
          end = (i, j)
    q = Queue()
    viewed = set()
    q.put((start, [start]))
    while not q.empty():
      (x, y), path = q.get()
      viewed.add((x,y))
      if (x, y) == end:
        return path

      for dx, dy in dirs:
        nx, ny = x+dx, y+dy
        if 0 < nx < h-1 and 0 < ny < w-1 and _map[nx][ny] != '#' and (nx, ny) not in viewed:
          q.put(((nx, ny), path + [(nx, ny)]))

  def find_cheat(self, path, moves, saves):
    dist = {}
    save_list = {}
    for i, cord in enumerate(path):
      dist[cord] = i

    for (x, y) in path:
      for dx in range(-moves, moves+1):
        for dy in range(-moves, moves+1):
          if dx == 0 and dy == 0:
            continue

          manhattan_dist = abs(dx)+abs(dy)
          if manhattan_dist > moves:
            continue

          nx, ny = x+dx, y+dy
          if (nx, ny) not in dist:
            continue

          save_dist = dist[(nx, ny)]-dist[(x, y)]-manhattan_dist
          if saves <= save_dist:
            save_list[save_dist] = save_list.get(save_dist, 0) + 1

    cheats = 0
    for k, v in save_list.items():
      # if len(path) < 100:
      #   print(v, k)
      cheats += v

    return cheats


  def part1(self, data):
    shortest_path = self.find_shortest_path(data)
    cheat_move = 2
    saves = 100 if len(data) > 15 else 0
    return self.find_cheat(shortest_path, cheat_move, saves)

  def part2(self, data):
    shortest_path = self.find_shortest_path(data)
    cheat_move = 20
    saves = 100
    return self.find_cheat(shortest_path, cheat_move, saves)