import time
from search import bfs_search, dfs_search, bfs_search_deque
from pathlib import Path
path = Path(input())

if not path.exists() or path.is_file():
    print(f"search: {path.absolute()}: No such directory")
    exit(1)

file_name = input()

print("Choose search strategy:\n1- BFS\n2- DFS\n3- BFS deque")

number = input()

while number != '1' and number != '2' and number != '3':
    print("Please enter 1 or 2 or 3:")
    number = input()

if number == '1':
    start = time.perf_counter()
    print(bfs_search(path, file_name))
    elapsed = time.perf_counter() - start
    print(elapsed)
elif number == '2':
    start = time.perf_counter()
    print(dfs_search(path, file_name))
    elapsed = time.perf_counter() - start
    print(elapsed)
else:
    start = time.perf_counter()
    print(bfs_search_deque(path, file_name))
    elapsed = time.perf_counter() - start
    print(elapsed)