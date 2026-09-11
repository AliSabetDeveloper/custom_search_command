#!/usr/bin/env python3
import time
from search import bfs_search, dfs_search
from pathlib import Path
import argparse

parser = argparse.ArgumentParser(description="Search a directory for a file using BFS or DFS")
parser.add_argument("path", help= "Directory to search in")
parser.add_argument("file_name", help="Name of the file to search for")
parser.add_argument("--strategy", choices= ["bfs", "dfs"], default="bfs", help= "Search strategy (default: bfs)")

args = parser.parse_args()
path = Path(str(args.path))
file_name = args.file_name
strategy = args.strategy

if not path.exists() or path.is_file():
    print(f"search: {path.absolute()}: No such directory")
    exit(1)

if strategy == "bfs":
    start = time.perf_counter()
    print(bfs_search(path, file_name))
    elapsed = time.perf_counter() - start
    print(elapsed)
else:
    start = time.perf_counter()
    print(dfs_search(path, file_name))
    elapsed = time.perf_counter() - start
    print(elapsed)