# -*- coding: utf-8 -*-
# @Author: Bobo
# @Date:   2025-01-08 13:04:51

from utils.solution_base import SolutionBase
from itertools import combinations
import networkx as nx

class Solution(SolutionBase):
  def part1(self, data):
    G = nx.Graph()
    for line in data:
      com_1, com_2 = line.split("-")
      G.add_edge(com_1, com_2)
    
    cliques = [c for c in nx.find_cliques(G) if len(c) >= 3 and any(n[0] == "t" for n in c)]
    sets = set()
    for c in cliques:
      for nodes in combinations(c, 3):
        if any(n[0] == "t" for n in nodes):
          sets.add(tuple(sorted(nodes)))
    return len(sets)
    
  def part2(self, data):
    G = nx.Graph()
    for line in data:
      com_1, com_2 = line.split("-")
      G.add_edge(com_1, com_2)
    
    cliques = nx.find_cliques(G)
    target = sorted(cliques, key=lambda x: -len(x))[0]
    
    return ",".join(sorted(target))