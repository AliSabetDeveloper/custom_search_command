# 🔎 custom_search_command
A search command that finds a specific file in a directory tree using DFS or BFS, with a built_in comparison between them and showing the directory and file visited result.
# 🧐 Why
I wanted to recap what I learned by solving problems in Quera, and more importantly, I wanted to see why we care about time complexity
and how given data affects on algorithms we choose (not just blindly accept theories).
# 🔑 Usage
```bash
search <path> <file_name> [--strategy bfs|dfs]
```
As you see, path is directory tree which we intend to search in and file_name is the target file (which they are positional arguments). The strategy is the optional switch which you can choose BFS or DFS there (the default is BFS).
here's an example:
```bash
search /home/hp/test01 file28 --strategy dfs
```
makes this output: (note that this output is true in my directory tree and obviously you shouldn't expect the same result when you run in you directory tree unless you have the same directory tree that I have in my shell)
```bash
{'file_name': '/home/hp/test01/dir03/dir21/dir49/file28', 'file_visited': 7, 'directory_visited': 8}
0.0003938150002795737
```
if you type an incorrect option for strategy switch, you get a clear error, Something like this:
```bash
usage: search [-h] [--strategy {bfs,dfs}] path file_name
search: error: argument --strategy: invalid choice: 'dfsd' (choose from bfs, dfs)

```
and if you forget how this command works, just type:
```bash
search --help
```
# 🔐 Design choices
## ▪️Skipping symlinks:
I skipped symlinks because following symlinks is not my purpose in this project.Adding symlinks support would only add unnecessary complexity to my project.For instance, imagine user enter a path and a target file and that path contains a symlink which points to a totally different path. In this case, it will search in a path that user didn't intend to.Or worse than that, if a symlink points to its parent, it will make circular reference which crashes the program.
## ▪️BFS with deque rather than pop:
For this design, I have practical reason. I want to show why I intended to compare them when there is a good theoretical reason to choose between them:
Firstly, I like to share the result I have achieved during several scenarios (I run each scenario you see in this chart several times for more reliable result for time.):

![BFS pop vs deque timing](https://github.com/AliSabetDeveloper/custom_search_command/blob/2d3306b21435e90dd3b94ce254134d92a2573de0/bfs_pop_vs_bfs_deque(time).png?raw=true)

🔹The first note I want to mention here is the given data. As you see when the give data is small (like 1000 directories or 10000 directories) the difference between deque and pop performance is too small.But as the data grows bigger, the difference between them gets much more noticeable.For instance, the difference between deque and pop is much more significant when the given data is 200000 directories rather than 100000 directories.
🔹More interestingly, when the given data is small, it really doesn't matter what algorithm you choose. Time complexity shows each algorithm's scale of performance, But it doesn't necessarily show us which algorithm is better to use. In another words, maybe the difference in performance isn't that significant to care about. Or even one algorithm may has less time complexity but consumes more memory and resources. this is an engineering choice to decide which algorithm is the best implementation for our case.
# 📊 Findings:
Now I want to show the difference between BFS and DFS, But first I want to share the result:

![BFS vs DFS visited directories](https://github.com/AliSabetDeveloper/custom_search_command/blob/9751c2d07b6d2a9644b12223f45fb9e59c75ed76/bfs_vs_dfs(directories).png?raw=true)

This chart is saying that when the target file is closer to root, the BFS finds it faster with less visited directories, But if the target file is deeper, DFS finds it faster with less visited directories. This result matches what theory would predict, because BFS searches level-by-level so each directory in a same distance from root will be visited before moving to next level while DFS searches depth-first.

The same result shows on visited files:

![BFS vs DFS visited files](https://github.com/AliSabetDeveloper/custom_search_command/blob/9751c2d07b6d2a9644b12223f45fb9e59c75ed76/bfs_vs_dfs(files).png?raw=true)

finally, to confirm timing for each scenario (I run each scenario you see in this chart several times for more reliable result for time.):

![BFS vs DFS timing](https://github.com/AliSabetDeveloper/custom_search_command/blob/9751c2d07b6d2a9644b12223f45fb9e59c75ed76/bfs_vs_dfs(time).png?raw=true)

these results confirm my previous words that the given data has high effect on the algorithm we choose to use. If the given data were bigger and more complex, the difference would be more significant.
# 🚀 Getting started
## Requirements:
1- python3

2- shell
## Optional:
3- matplotlib

## installation:
First, clone the repository:
```bash
git clone https://github.com/AliSabetDeveloper/custom_search_command.git
cd custom_search_command
```

For making this repo a real command, we need to verify whether ~/.local/bin is already exists or not. Use this command to verify:
```bash
echo $PATH
```
If you see $HOME/.local/bin somewhere in the output, you're ready to go. But if not, use this command:
```bash
export PATH="$HOME/.local/bin:$PATH"
```
This command only affects on open shell and it's gone the moment that the terminal is closed. To make this automatically every time a new terminal opens, use this:
```bash
export PATH="$HOME/.local/bin:$PATH"
source ~/.bashrc
```
Or if you're using shell instead of bash, use this:
```bash
export PATH="$HOME/.local/bin:$PATH"
source ~/.zshrc
```
Then reopen the terminal to take the effect.

Finally use this command to make it a real Linux command (make your current working directory is in custom_search_command directory):
```bash
ln -s "$(pwd)/interface.py" ~/.local/bin/search
```
To make sure everything is okay, use this:
```bash
search --help
```
if you see this:
```bash
usage: search [-h] [--strategy {bfs,dfs}] path file_name

Search a directory for a file using BFS or DFS

positional arguments:
  path                  Directory to search in
  file_name             Name of the file to search for

options:
  -h, --help            show this help message and exit
  --strategy {bfs,dfs}  Search strategy (default: bfs)
```
then, congratulation. You're search command is ready to go.

                                            made with ❤️ , python and linux
