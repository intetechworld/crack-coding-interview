"""
You are given an inclusive range [lower, upper] and a sorted unique integer array nums, where all elements are in the inclusive range.
A number x is considered missing if x is in the range [lower, upper] and x is not in nums.
Return the smallest sorted list of ranges that cover every missing number exactly. That is, no element of nums is in any of the ranges, and each missing number is in one of the ranges.
Each range [a,b] in the list should be output as:

"a->b" if a != b
"a" if a == b

Example 1:
Input: nums = [0,1,3,50,75], lower = 0, upper = 99
Output: ["2","4->49","51->74","76->99"]
Explanation: The ranges are:
[2,2] --> "2"
[4,49] --> "4->49"
[51,74] --> "51->74"
[76,99] --> "76->99"

Example 2:
Input: nums = [-1], lower = -1, upper = -1
Output: []
Explanation: There are no missing ranges since there are no missing numbers.
Constraints:
-109 <= lower <= upper <= 109
0 <= nums.length <= 100
lower <= nums[i] <= upper
All the values of nums are unique.
"""

# Soltuion
class Solution:
    def formatRange(self,a,b):
        if a == b:
            return str(a)
        else:
            return str(a) + "->" + str(b)
    def func(self,nums,lower,upper):
        nums = [lower-1] + nums + [upper+1] 
        result = [] 
        for i in range(1,len(nums)):
            if nums[i] - nums[i-1] > 1:
                result.append(self.formatRange(nums[i-1]+1,nums[i]-1))
        return result
obj = Solution()
print(obj.func([0,1,3,50,75],0,99))

## Time complexity  - O(N)
## Space complexity - O(1)




