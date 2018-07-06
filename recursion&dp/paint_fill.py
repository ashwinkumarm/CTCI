def paint_fill(grid, r, c, nc):
    if grid[r][c] == nc:
        return False
    return _paint(grid, r, c, grid[r][c], nc)


def _paint(grid, r, c, oc, nc):
    if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]) or grid[r][c] != oc:
        return False

    grid[r][c] = nc
    _paint(grid, r + 1, c, oc, nc)
    _paint(grid, r, c + 1, oc, nc)
    _paint(grid, r - 1, c, oc, nc)
    _paint(grid, r , c - 1, oc, nc)

    return True

grid = [[0,1,1,1,0], [0,1,1,0,0],[0,0,1,0,0]]
paint_fill(grid, 1, 1, 2)
print(grid)