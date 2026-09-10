
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
        result = dfs_search(sub_dir, file_name, result)
        result["directory_visited"] += 1
        if result["file_name"] is not None:
            return result
    return result

def bfs_search(path, file_name):
    list_dir = [path.absolute()]
    file_visited = 0
    directory_visited = 0
    while len(list_dir) != 0:
        try:
            for item in list_dir[0].iterdir():
                if not item.is_symlink():
                    if item.is_dir():
                        list_dir.append(item.absolute())
                    elif item.is_file():
                        file_visited += 1
                        if item.name == file_name:
                            directory_visited += 1
                            return {"file_name": str(item), "file_visited": file_visited, "directory_visited": directory_visited}
        except:
            print(f"permission denied: {list_dir[0]}")
        directory_visited += 1
        list_dir.pop(0)
    return {"file_name": None, "file_visited": file_visited, "directory_visited": directory_visited}
