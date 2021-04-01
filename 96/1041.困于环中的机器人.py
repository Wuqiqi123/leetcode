#
# @lc app=leetcode.cn id=1041 lang=python
#
# [1041] 困于环中的机器人
#

# @lc code=start
class Solution(object):

    def isRobotBounded(self, instructions):
        """
        :type instructions: str
        :rtype: bool
        """
        last_point = [[0, 0], [0, 1]]
        L_rotate = [(0, 1), (-1, 0), (0, -1), (0, 1)]
        for i in instructions * 4:
            if i == "G"
                current_point = [[last_point[0] + last_point[1][0], last_point[1] + last_point[1][1]], 
                                    last_point[1]]
            elif i == "L":
                current_point = [last_point[0], ]
            elif i == "R":
                current_point = [last_point[0], ]
# @lc code=end

