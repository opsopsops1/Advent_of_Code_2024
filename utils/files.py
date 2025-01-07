# -*- coding: utf-8 -*-
# @Author: Bobo
# @Date:   2024-12-26 11:57:50

import os, sys, json
import urllib.request
from pathlib import Path

class Files():
  @staticmethod
  def download_puzzle_input(year=2022, day=0):
    url = f"https://adventofcode.com/{year}/day/{day}"
    headers = Files.get_headers()
    session = Files.get_session()
    
    headers["Referer"] = url
    headers["Cookie"] = f"session={session}"
    req = urllib.request.Request(url+"/input", method="GET", headers=headers)
    with urllib.request.urlopen(req) as response:
      if response.status == 200:
        content = response.read().decode("utf-8")

    return content

  @staticmethod
  def add_day(year, day):
    path = Files.get_path()

    solution = os.path.realpath(os.path.join(f"{path}", "solutions", f"day{day:02}.py"))
    solution_path = Path(solution)
    if not solution_path.exists():
      solution_path.touch()
      print("Created file:", solution_path)

    folder = os.path.realpath(os.path.join(f"{path}", "data", f"day{day:02}"))
    folder_path = Path(folder)
    if not folder_path.exists():
      folder_path.mkdir(parents=True, exist_ok=True)

    files = ["puzzle_input.txt", "test_1_input.txt", "test_1_part1_result.txt", "test_1_part2_result.txt"]
    for file in files:
      file_path = Path(os.path.join(folder, file))
      if not file_path.exists():
        file_path.touch()
        print("Created file:", file_path)

    input_path = Path(os.path.join(folder, files[0]))
    if input_path.stat().st_size == 0:
      # ...
      with open(input_path, 'w+') as f:
        f.write(Files.download_puzzle_input(year, day))
        print("Download puzzle input to:", input_path)

  @staticmethod
  def add_test_file(day, test_num):
    path = Files.get_path()
    folder = os.path.realpath(os.path.join(f"{path}", "data", f"day{day:02}"))
    folder_path = Path(folder)
    if not folder_path.exists():
      folder_path.mkdir(parents=True, exist_ok=True)

    files = [f"test_{test_num}_input.txt", f"test_{test_num}_part1_result.txt", f"test_{test_num}_part2_result.txt"]
    for file in files:
      file_path = Path(os.path.join(f"{folder}", f"{file}"))
      if not file_path.exists():
        file_path.touch()
        print("Created test file:", file_path)

  @staticmethod
  def get_session():
    session = ""
    path = Files.get_path()
    session_path = os.path.realpath(os.path.join(f"{path}", "..", "aoc_session"))
    with open(session_path, 'r') as f:
      session = f.read().strip()
    return session

  @staticmethod
  def get_headers():
    header = {}
    path = Files.get_path()
    header_path = os.path.realpath(os.path.join(f"{path}", "aoc_headers.json"))
    with open(header_path, 'r') as f:
      header = json.load(f)
    return header
    
  @staticmethod
  def get_path():
    return path if os.path.isdir(path := os.path.realpath(sys.argv[0])) else os.path.dirname(path)
