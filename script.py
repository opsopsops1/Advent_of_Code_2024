# -*- coding: utf-8 -*-
# @Author: Bobo
# @Date:   2024-12-26 12:01:36

import argparse, importlib, datetime
from utils.files import Files

def main():
  parser = argparse.ArgumentParser(description="Advent of Code solution script")
  parser.add_argument("-d", "--day", dest="day", default=1, metavar="day_number", type=int, help="Required, day number of the AoC event")
  parser.add_argument("-p", "--part", dest="part", default=1, metavar="part_number", type=int, help="Required, part number of the day of the AoC event")
  parser.add_argument("--add", action="store_true", help="Optional, create daily file")
  parser.add_argument("--add_test_file", metavar="test_number", type=int, help="Optional, create additional test files")
  parser.add_argument("--skip_test", action="store_true", help="Optional, skipping tests")
  parser.add_argument("--benchmark", action="store_true", help="Optional, benchmarking the code, and also skipping tests")

  args = parser.parse_args()
  if not 0 < args.day < 26:
    print("Day number must be between 1 and 25.")
    exit()
  elif args.add is True:
    print(f"Adding day: {args.day}")
    Files.add_day(year=2024, day=args.day)
  elif args.add_test_file is not None:
    print("Adding test file for day", args.day, ", no", args.add_test_file)
    Files.add_test_file(args.day, args.add_test_file)
  elif args.part not in [1, 2]:
    print("Part number must be between 1 and 2.")
    exit()
  else:
    print(f"Solving day {args.day} part {args.part}\n")
    sol = importlib.import_module(f"solutions.day{args.day:02d}").Solution(args.day, args.skip_test, args.benchmark)
    print(f"The answer is\n{answer}\n" if (answer := sol.solve(part_num=args.part)) is not None else "???")
    sol.benchmark(_print=True)
    

if __name__ == "__main__":
  main()
