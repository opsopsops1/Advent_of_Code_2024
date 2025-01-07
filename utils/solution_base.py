# -*- coding: utf-8 -*-
# @Author: Bobo
# @Date:   2024-12-26 12:00:40

from utils.puzzle_reader import PuzzleReader
import timeit

class SolutionBase():
  def __init__(self, day_num: int = 0, skip_test: bool = False, benchmark: bool = False):
    self.day_num = day_num
    self.skip_test = skip_test
    self._benchmark = benchmark
    self.benchmark_times = []
    self.data = PuzzleReader.get_puzzle_input(self.day_num)

  def get_test_input(self):
    return PuzzleReader.get_test_input(self.day_num)

  def get_test_output(self, part_num):
    return PuzzleReader.get_test_output(self.day_num, part_num)

  def solve(self, part_num: int):
    if not self.skip_test:
      self.test_runner(part_num)

    func = getattr(self, f"part{part_num}")
    self.benchmark()
    result = func(self.data)
    self.benchmark()
    return result

  def test_runner(self, part_num):
    test_input = self.get_test_input()
    test_output = self.get_test_output(part_num)
    test_counter = 1
    # print(test_input)
    # print(test_output)

    func = getattr(self, f"part{part_num}")
    for i, o in zip(test_input, test_output):
      if len(o):
        if (test_result := str(func(i))) == o:
          print(f"Test {test_counter} passed!")
        else:
          print(f"Test {test_counter} NOT passed.\n"
                f"Your result: \n{test_result}\n"
                f"Test output: \n{o}\n"
                "----------------------------------------")
      test_counter += 1
    print()

  def benchmark(self, _print=False):
    if _print and len(self.benchmark_times) > 0 and len(self.benchmark_times)%2 == 0:
      t = self.benchmark_times[-1] - self.benchmark_times[-2]
      units = ["s", "ms", "µs", "ns"]
      unit_idx = 0
      while t < 1:
        t *= 1000
        unit_idx += 1
      print(f"benchmarking: {t:.2f} {units[unit_idx]}")
    elif self._benchmark:
      self.benchmark_times.append(timeit.default_timer())
  