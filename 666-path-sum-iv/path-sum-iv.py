class Solution:
    def pathSum(self, nums: List[int]) -> int:
        # (depth, position): value
        node_values = {(int(str(num)[0]), int(str(num)[1])): int(str(num)[2]) for num in nums}

        def dfs(depth, position, current_sum):
            key = (depth, position)
            if key not in node_values:
                return 0

            current_sum += node_values[key]
            if (depth + 1, position * 2 - 1) not in node_values and (depth + 1, position * 2) not in node_values:
                return current_sum

            left_sum = dfs(depth + 1, position * 2 - 1, current_sum)
            right_sum = dfs(depth + 1, position * 2, current_sum)
            
            return left_sum + right_sum

        return dfs(1, 1, 0)
