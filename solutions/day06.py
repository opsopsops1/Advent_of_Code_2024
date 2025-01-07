# -*- coding: utf-8 -*-
# @Author: Bobo
# @Date:   2024-12-27 12:02:18

from utils.solution_base import SolutionBase
import json

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

class Solution(SolutionBase):
  def part1(self, data):
    h, w = len(data), len(data[0])
    si, sj = self.get_guard_pos(data)
    now_dir = 0

    used = set()
    used.add((si,sj))
    while 1:
      ni = si + di[now_dir]
      nj = sj + dj[now_dir]
      if ni < 0 or nj < 0 or ni >= h or nj >= w:
        break
      if data[ni][nj] == '#':
        now_dir = (now_dir+1)%4
      else:
        si, sj = ni, nj
        used.add((si,sj))
    return len(used)

  def part2(self, data):
    is_leave, visited = self.patrol(data)
    res = 0
    
    for i, j in visited.keys():
      _map_copy = data.copy()
      to_list = list(_map_copy[i])
      to_list[j] = '#'
      _map_copy[i] = "".join(to_list)

      pos = visited[(i,j)][0]
      idx = visited[(i,j)][1]

      is_leave_copy, visited_copy = self.patrol(_map_copy, pos=pos, idx=idx)
      if not is_leave_copy:
        res += 1

    return res


  def get_guard_pos(self, _map):
    for i in range(len(_map)):
      for j in range(len(_map[0])):
        if _map[i][j] == '^':
          return (i, j)

  def patrol(self, _map, pos=None, idx=None):
    if not pos:
      pos = self.get_guard_pos(_map)

    if not idx:
      idx = 0

    h, w = len(_map), len(_map[0])
    visited = dict()

    while 1:
      n_pos = (pos[0]+di[idx], pos[1]+dj[idx])
      # print(n_pos)

      if n_pos[0] < 0 or n_pos[1] < 0 or n_pos[0] >= h or n_pos[1] >= w:
        return True, visited

      if _map[n_pos[0]][n_pos[1]] == '#':
        idx = (idx+1)%4
      else:
        if n_pos not in visited.keys():
          visited[n_pos] = (pos, idx)
        elif visited[n_pos] == (pos, idx):
          return False, visited
        pos = n_pos
