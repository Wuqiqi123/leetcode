#
# @lc app=leetcode.cn id=923 lang=python
#
# [923] 三数之和的多种可能
#   8

# @lc code=start
class Solution(object):
    def threeSumMulti(self, arr, target):
        """
        :type arr: List[int]
        :type target: int
        :rtype: int
        """

        MOD = 10**9 + 7
        ans = 0
        arr.sort()

        for i, value in enumerate(arr):
            j = i + 1
            k = len(arr) - 1
            T = target - arr[i]

            while j < k:
                if arr[j] + arr[k] < T:
                    j += 1
                elif arr[j] + arr[k] > T:
                    k -= 1
                elif arr[j] != arr[k]:
                    ## So here we find the part i j ,k
                    left_num = right_num = 1
                    while arr[j] == arr[j+1] and j + 1 < k:
                        left_num += 1
                        j += 1
                    while arr[k] == arr[k-1] and k - 1 > j:
                        right_num += 1
                        k -= 1
                    
                    ans += left_num * right_num
                    ans %= MOD

                    j += 1
                    k -= 1
                else:
                    ans += (k-j+1) * (k-j) / 2
                    ans %= MOD
                    break

        return ans
            
        
# @lc code=end

