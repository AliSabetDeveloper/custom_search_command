from pathlib import Path

for i in range(10000):
    path = Path("dir" + str(i))
    path.mkdir()
