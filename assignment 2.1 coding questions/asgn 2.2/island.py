# no of isalands
class Solution:
    def numIsland(self, grid: list[list[str]]) -> int:
         if not grid:  
            return 0  

    def explore(r, c):
        queue = deque()
        visited.add((r, c))
        queue.append((r, c))
        while queue:
            row, col = queue.popleft()
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nr, nc = row + dr, col + dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == '1' and (nr, nc) not in visited:
                    queue.append((nr, nc))
                    visited.add((nr, nc))
                    rows, cols = len(grid), len(grid[0])
                    visited = set()
                    island_count = 0
                    for r in range(rows):
                        for c in range(cols):
                            if grid[r][c] == '1' and (r, c) not in visited:
                                explore(r, c)
                                island_count+=1
                    return island_count
