# https://leetcode.com/problems/robot-return-to-origin/

class Solution:
    def judgeCircle(self, moves: str) -> bool:
        vertical = 0
        horizontal = 0
        for move in moves:
            if move == 'U':
                vertical += 1
            elif move == 'D':
                vertical -= 1
            elif move == 'R':
                horizontal += 1
            elif move == 'L':
                horizontal -= 1

        return horizontal == 0 and vertical == 0


s = Solution()
print(s.judgeCircle("LDRRLRUULR"))
