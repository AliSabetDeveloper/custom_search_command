from pathlib import Path
p = Path("/home/hp/dir1")



def dfs_search(path, file_name):
    sub_dirs = []
    try:
        for item in path.iterdir():
            if not item.is_symlink():
                if item.is_file():
                    if item.name == file_name:
                        return item.absolute()
                elif item.is_dir():
                    sub_dirs.append(item)
    except:
        print(f"permission denied: {path.absolute()}")
    for sub_dir in sub_dirs:
        result = dfs_search(sub_dir, file_name)
        if result is not None:
            return result
    return None



print(dfs_search(p, 'file1'))
