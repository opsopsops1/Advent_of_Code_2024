# -*- coding: utf-8 -*-
# @Author: Bobo
# @Date:   2024-12-26 12:00:13

import os, sys, glob

class PuzzleReader():
  @staticmethod
  def get_puzzle_input(day_num):
    # return [line.strip("\n") if is_raw else line.strip() for line in open(f"{PuzzleReader.get_path()}/data/day{day_num:02d}/puzzle_input.txt", "r").readlines()]
    return [line.strip("\n") for line in open(os.path.join(f"{PuzzleReader.get_path()}", "data", f"day{day_num:02d}", "puzzle_input.txt"), "r").readlines()]

  @staticmethod
  def get_test_input(day_num):
    inputs = []
    for file_name in sorted(glob.glob(os.path.join(f"{PuzzleReader.get_path()}", "data", f"day{day_num:02d}", "test_") + "[0-9]" + "_input.txt")):
      inputs += [[line.strip("\n") for line in open(file_name, "r").readlines()]]
    return inputs

  @staticmethod
  def get_test_output(day_num, part_num):
    outputs = []
    for file_name in sorted(glob.glob(os.path.join(f"{PuzzleReader.get_path()}", "data", f"day{day_num:02d}", "test_") + "[0-9]" + f"_part{part_num}_result.txt")):
      outputs += [open(file_name, "r").read().strip()]
    return outputs

  @staticmethod
  def get_path():
    return path if os.path.isdir(path := os.path.realpath(sys.argv[0])) else os.path.dirname(path)
