from pathlib import Path
p = Path("/home/hp/dir1")



def dfs_search(path, file_name, result=None):
    if result is None:
        result = {"file_name": None, "file_visited": 0, "directory_visited": 1}
    sub_dirs = []
    try:
        print(path)
        for item in path.iterdir():
            if not item.is_symlink():
                if item.is_file():
                    result["file_visited"] += 1
                    if item.name == file_name:
                        result["file_name"] = str(item)
                        return result
                elif item.is_dir():
                    sub_dirs.append(item)
    except:
        print(f"permission denied: {path.absolute()}")
    for sub_dir in sub_dirs:
        result["directory_visited"] += 1
        result = dfs_search(sub_dir, file_name, result)
        if result["file_name"] is not None:
            return result
    return result



print(dfs_search(p, 'file8'))
