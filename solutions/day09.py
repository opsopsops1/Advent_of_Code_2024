# -*- coding: utf-8 -*-
# @Author: Bobo
# @Date:   2024-12-28 12:43:52

from utils.solution_base import SolutionBase

class Solution(SolutionBase):
  def part1(self, data):
    disk = data[0]
    disk_length = len(disk)
    checksum = 0
    
    disk_space = []
    for i in range(disk_length):
      if i%2 == 1:
        for t in range(int(disk[i])):
          disk_space.append(-1)
      else:
        for t in range(int(disk[i])):
          disk_space.append(i//2)
    r_idx = len(disk_space)-1
    for l_idx in range(len(disk_space)):
      if l_idx > r_idx:
        break
      if disk_space[l_idx] != -1:
        checksum += disk_space[l_idx] * l_idx
      else:
        while disk_space[r_idx] == -1 and l_idx < r_idx:
          r_idx -= 1
        if l_idx < r_idx:
          checksum += disk_space[r_idx] * l_idx
          r_idx -= 1

    return checksum

  def part2(self, data):
    disk = list(map(int, data[0]))
    disk_length = len(disk)
    checksum = 0

    new_disk = []
    for i in range(disk_length):
      if i%2 == 0:
        new_disk.append([i, i//2, disk[i]])
      else:
        new_disk.append([i, -1, disk[i]])

    r_i = disk_length-1
    while r_i > 0:
      if new_disk[r_i][1] == -1:
        r_i -= 1
        continue

      for s_i in range(1, disk_length, 2):
        if s_i >= r_i:
          continue
        if disk[r_i] <= new_disk[s_i][2]:
          new_disk[s_i][2] -= disk[r_i]
          new_disk.append([new_disk[s_i][0], r_i//2, disk[r_i]])
          new_disk[r_i][1] = -1
          break

      r_i -= 1
    
    pos = 0
    r = 0
    new_disk = sorted(new_disk, key=lambda x: (x[0], -x[1]))
    for l in new_disk:
      if l[2] == 0:
        continue
      for x in range(l[2]):
        if l[1] != -1:
          checksum += pos * l[1]
        pos += 1

    return checksum
