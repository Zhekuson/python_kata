class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        num_islands = 0

        def bfs(cur_i, cur_j):
            if (
                    0 <= cur_i < len(grid)
            ) and (
                    0 <= cur_j < len(grid[0])
            ):
                if (cur_i, cur_j) in visited:
                    return
                if grid[cur_i][cur_j] == "1":
                    visited.add((cur_i, cur_j))
                    # print(f"1 calling {cur_i + 1, cur_j}")
                    bfs(cur_i + 1, cur_j)
                    # print(f"2 calling {cur_i, cur_j + 1}")
                    bfs(cur_i, cur_j + 1)
                    bfs(cur_i - 1, cur_j)
                    bfs(cur_i, cur_j - 1)
            else:
                return

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "1":
                    if not (i, j) in visited:
                        num_islands += 1
                        bfs(i, j)

        return num_islands