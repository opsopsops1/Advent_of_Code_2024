# -*- coding: utf-8 -*-
# @Author: Bobo
# @Date:   2025-01-05 18:52:57

from utils.solution_base import SolutionBase
from queue import Queue

dirs = [(0, 1), (-1, 0), (0, -1), (1, 0)]  # > ^ < v

class Solution(SolutionBase):
  def part1(self, data):
    h, w = len(data), len(data[0])
    dist = [[[10**18 for _ in range(4)] for wi in range(w)] for hi in range(h)]
    dist[h-2][1][0] = 0
    
    q = Queue()
    q.put((h-2, 1))
    while not q.empty():
      x, y = q.get()
      dl = dist[x][y]
      m_i = -1
      m_m = 10**18
      for i in range(4):
        if dl[i] < m_m:
          m_m = dl[i]
          m_i = i

      dist[x][y][(m_i+1)%4] = min(dist[x][y][(m_i+1)%4], dist[x][y][m_i]+1000)
      dist[x][y][(m_i+3)%4] = min(dist[x][y][(m_i+3)%4], dist[x][y][m_i]+1000)

      for di in range(4):
        nx, ny = x+dirs[di][0], y+dirs[di][1]
        if data[nx][ny] == '#':
          continue
        if dist[nx][ny][di] > dist[x][y][di]+1:
          q.put((nx, ny))
          dist[nx][ny][di] = min(dist[nx][ny][di], dist[x][y][di]+1)

    return min(dist[1][w-2])



  def part2(self, data):
    h, w = len(data), len(data[0])
    q = Queue()
    q.put(([(h-2, 1)], 0, 0))
    r = []
    visited = {}
    while not q.empty():
      his, sc, d = q.get()
      x, y = his[-1]
      if (x, y) == (1, w-2):
        r.append((his, sc))
        continue

      if (x, y, d) in visited and visited[(x, y, d)] < sc:
        continue
      visited[(x, y, d)] = sc
      for di in range(4):
        if (di+2)%4 == d:
          continue

        nx, ny = x+dirs[di][0], y+dirs[di][1]
        if data[nx][ny] == '#' or (nx, ny) in his:
          continue

        if di == d:
          q.put((his+[(nx, ny)], sc+1, d))
        else:
          q.put((his, sc+1000, di))

    
    mi = min([x[1] for x in r])
    br = [x[0] for x in r if x[1] == mi]
    tile = {t for b in br for t in b}
    return len(tile)