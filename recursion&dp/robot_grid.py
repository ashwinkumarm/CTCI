def find_path(grid):
    path = []
    if _path(len(grid)-1,len(grid[0])-1, grid, path):
       return path

    return None


def find_path_dp(grid):
    path = []
    failed_points = set()
    if _path_dp(len(grid) - 1, len(grid[0]) - 1, grid, path, failed_points):
        return path

    return None

def _path_dp(r, c, grid, path, failed_points = set()):
    if r < 0 or c < 0 or not grid[r][c]:
        return False

    if str(r) + str(c) in failed_points:
        return False

    origin = False
    if r == 0 and c == 0:
        origin = True

    if origin or _path(r - 1, c, grid, path) or _path(r, c - 1, grid, path):
        path.append(str(r) + str(c))
        return True

    failed_points.add(str(r) + str(c))
    return False

def _path(r, c, grid, path):
    if r < 0 or c < 0 or not grid[r][c]:
        return False

    origin = False
    if r == 0 and c == 0:
        origin = True

    if origin or _path(r-1, c, grid, path) or _path(r, c-1, grid, path):
        path.append(str(r) + str(c))
        return True

    return False

grid = [[1,1,1,1], [1,0,0,1],[1,1,0,1],[1,1,1,1]]
print(find_path_dp(grid))