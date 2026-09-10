import matplotlib.pyplot as plt
import numpy as np

scenarios = ["Deep target\n(file28)" , "Shallow target\n(file40)"]
bfs_dirs = [43, 16]
dfs_dirs = [8 , 64]

x = np.arange(len(scenarios))
width = 0.35

fig1, ax1 = plt.subplots()
ax1.bar(x - width/2, bfs_dirs, width, label="BFS")
ax1.bar(x + width/2, dfs_dirs, width, label="DFS")

ax1.set_ylabel("Directory visited")
ax1.set_title("BFS vs DFS: directories visited by target depth")
ax1.set_xticks(x)
ax1.set_xticklabels(scenarios)
ax1.legend()

plt.savefig("bfs_vs_dfs(directories).png")

bfs_files = [49 , 20]
dfs_files = [7, 61]

x = np.arange(len(scenarios))
fig2, ax2 = plt.subplots()
ax2.bar(x - width/2, bfs_files, width, label="BFS")
ax2.bar(x + width/2, dfs_files, width, label="DFS")

ax2.set_ylabel("Files visited")
ax2.set_title("BFS vs DFS: files visited by target depth")
ax2.set_xticks(x)
ax2.set_xticklabels(scenarios)
ax2.legend()

plt.savefig("bfs_vs_dfs(files).png")

bfs_time = [0.0026, 0.0015]
dfs_time = [0.0009, 0.0030]

x = np.arange(len(scenarios))
fig3, ax3 = plt.subplots()
ax3.bar(x - width/2, bfs_time, width, label="BFS")
ax3.bar(x + width/2, dfs_time, width, label="DFS")

ax3.set_ylabel("Time (seconds)")
ax3.set_title("BFS vs DFS: execution time by target depth")
ax3.set_xticks(x)
ax3.set_xticklabels(scenarios)
ax3.legend()

plt.savefig("bfs_vs_dfs(time).png")






