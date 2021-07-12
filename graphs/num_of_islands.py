class Solution:
    def numIslands(self, grid):

        def sink_node(i, j):
            rows = len(grid)
            columns = len(grid[0])

            if 0 <= i < rows and 0 <= j < columns and grid[i][j] == "1":
                grid[i][j] = "0"

                sink_node(i+1, j)
                sink_node(i-1, j)
                sink_node(i, j+1)
                sink_node(i, j-1)

                return 1

            return 0

        counter = 0

        for i in range(len(grid)):

            for j in range(len(grid[i])):
                counter += sink_node(i, j)

        return counter


# ----TESTING----
grid = [["1", "0", "1", "1", "0", "1", "1"]]
testing = Solution()
print(testing.numIslands(grid))
