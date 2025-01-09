# -*- coding: utf-8 -*-
# @Author: Bobo
# @Date:   2025-01-08 14:23:31

from utils.solution_base import SolutionBase
from queue import Queue

class Solution(SolutionBase):
  def part1(self, data):
    wires_values, gates = tuple([spi.split("\n") for spi in "\n".join(data).split("\n\n")])
    wires = {}
    gates = [g.split() for g in gates]
    gates.sort(key=lambda x: (x[0] not in wires)+(x[2] not in wires))
    for wire in wires_values:
      w, v = wire.split(": ")
      wires[w] = int(v)

    q = Queue()
    for gate in gates:
      q.put(gate)
    while not q.empty():
      gate = q.get()
      w1, op, w2, w3 = gate[0], gate[1], gate[2], gate[4]
      if w1 not in wires or w2 not in wires:
        q.put(gate)
        continue
      if op == "AND":
        wires[w3] = wires[w1] & wires[w2]
      if op == "OR":
        wires[w3] = wires[w1] | wires[w2]
      if op == "XOR":
        wires[w3] = wires[w1] ^ wires[w2]

    z_wire = [v for k, v in sorted([val for val in  wires.items() if val[0][0] == "z"], key=lambda x: x[0], reverse=True)]
    val = int("".join(map(str,z_wire)), 2)
    return val
    
  def build_gate_connections(self, gate_input):
    gate_connections = []
    for output, (in1, gate, in2) in gate_input.items():
      gate_connections.append(f"{in1} {gate} {in2} -> {output}")
    return gate_connections

  def print_gate_connections(self, gate_input, key, depth=0):
    if depth == 3 or key[0] in ("x", "y"):
      return key
    in1, gate, in2 = gate_input[key]
    return f"({key}=[{self.print_gate_connections(gate_input, in1, depth + 1)} {gate} {self.print_gate_connections(gate_input, in2, depth + 1)}])"

  def part2(self, data):
    # No solve
    pos = data.index("")
    wires_values = data[:pos]
    gates = data[pos+1:]

    x_bin = "".join([line.split(": ")[1] for line in wires_values if line.startswith("x")])[::-1]
    y_bin = "".join([line.split(": ")[1] for line in wires_values if line.startswith("y")])[::-1]
    z_bin = bin(int(x_bin,2)+int(y_bin,2))[2:][::-1]

    gate_input = {}
    for line in gates:
      in1, gate, in2, _, out = line.split()
      gate_input[out] = (in1, gate, in2)
    
    swap_tmp = []
    result = []
    while True:
      curr_gates = self.build_gate_connections(gate_input)
      z_check = bin(self.part1(data[:pos+1] + curr_gates))[2:][::-1]

      if z_bin == z_check:
        break

      for i in range(len(z_bin)):
        if z_check[i] != z_bin[i] or len(swap_tmp) == 1:
          key1 = f"z{i:02}"
          if z_bin[i] != z_check[i]:
            print("unmatch bit:", key1)
          else:
            print("look for possible unmatch:", key1)

          in1, gate, in2 = gate_input[key1]
          connections = self.print_gate_connections(gate_input, key1)
          print(connections)
          if gate == "XOR":
            if in1[0] in ("x", "y") and in2[0] in ("x", "y"):
              continue

            l_lv1_in1, l_lv1_gate, l_lv1_in2 = gate_input[in1]
            r_lv1_in1, r_lv1_gate, r_lv1_in2 = gate_input[in2]

            if l_lv1_gate == "XOR" and l_lv1_in1[0] in ("x", "y"):
              if r_lv1_gate != "OR":
                swap_tmp.append(in2)
              else:
                _, r_lv1_in1_lv2_gate, _ = gate_input[r_lv1_in1]
                if r_lv1_in1_lv2_gate != "AND":
                  swap_tmp.append(r_lv1_in1)
                _, r_lv1_in2_lv2_gate, _ = gate_input[r_lv1_in2]
                if r_lv1_in2_lv2_gate != "AND":
                  swap_tmp.append(r_lv1_in2)
            else:
              if l_lv1_gate != "OR":
                swap_tmp.append(in1)
              else:
                _, l_lv1_in1_lv2_gate, _ = gate_input[l_lv1_in1]
                if l_lv1_in1_lv2_gate != "AND":
                  swap_tmp.append(l_lv1_in1)
                _, l_lv1_in2_lv2_gate, _ = gate_input[l_lv1_in2]
                if l_lv1_in2_lv2_gate != "AND":
                  swap_tmp.append(l_lv1_in2)
          else:
            swap_tmp.append(key1)

          print("invalid format, need swap:", swap_tmp[-1], end="\n\n")

          if len(swap_tmp) == 2:
            break

      gate_input[swap_tmp[0]], gate_input[swap_tmp[1]] = gate_input[swap_tmp[1]], gate_input[swap_tmp[0]]
      result.extend(swap_tmp)
      swap_tmp = []

    return ",".join(sorted(result))
