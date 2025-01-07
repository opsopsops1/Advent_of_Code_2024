# -*- coding: utf-8 -*-
# @Author: Bobo
# @Date:   2024-12-30 16:45:21

from utils.solution_base import SolutionBase
from queue import Queue

dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

class Solution(SolutionBase):
  def part1(self, data):
    h, w = 103, 101
    if len(data) == 12:
      h, w = 7, 11

    quads = [0, 0, 0, 0]
    for line in data:
      r, v = line.split(' ')
      x, y = map(int,r[2:].split(','))
      vx, vy = map(int,v[2:].split(','))
      nx = (x + 100*(vx+w)) % w
      ny = (y + 100*(vy+h)) % h
      if nx == w//2 or ny == h//2:
        continue
      quad_idx = int(nx > w//2) + int(ny > h//2)*2
      quads[quad_idx] += 1
    return quads[0]*quads[1]*quads[2]*quads[3]

  def part2(self, data):
    h, w = 103, 101
    robots = []

    for line in data:
      r, v = line.split(' ')
      x, y = map(int,r[2:].split(','))
      vx, vy = map(int,v[2:].split(','))
      robots.append(((x, y), (vx, vy)))

    for t in range(1, 10**6):
      G = [['.' for _ in range(w)] for _ in range(h)]
      for (x, y), (vx, vy) in robots:
        nx = (x + t*(vx+w)) % w
        ny = (y + t*(vy+h)) % h
        G[ny][nx] = '#'
      
      used = set()
      group = 0

      for y in range(h):
        for x in range(w):
          if G[y][x] == '#' and (x, y) not in used:
            group += 1
            q = Queue()
            q.put((x,y))
            while not q.empty():
              sx, sy = q.get()
              used.add((sx, sy))
              for dx, dy in dirs:
                nx, ny = sx+dx, sy+dy
                if 0 <= nx < w and 0 <= ny < h and G[ny][nx] == '#' and (nx, ny) not in used:
                  q.put((nx, ny))

      if group < 200:
        print(t, group)
        for line in G:
          print("".join(line))
        print()

