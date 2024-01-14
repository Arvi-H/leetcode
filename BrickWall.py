class Solution(object):
    def leastBricks(self, wall):
        edges = {}

        for row in wall:
            width_sum = 0
            for brick in row[:-1]: # Except the last one
                width_sum += brick

                if width_sum in edges:
                    edges[width_sum] += 1
                else:
                    edges[width_sum] = 1
             
        max_edges = 0
        for count in edges.values():
            max_edges = max(max_edges, count)

        print(edges)
        return len(wall) - max_edges

s = Solution()
wall = [[1,2,2,1],[3,1,2],[1,3,2],[2,4],[3,1,2],[1,3,1,1]]
s.leastBricks(wall)