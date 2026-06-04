# Last updated: 6/4/2026, 9:42:40 PM
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_val=nums[0]
        min_val=nums[0]
        ans=nums[0]
        for i in range(1,len(nums)):
            num=nums[i]
            if num<0:
                max_val,min_val=min_val,max_val
            max_val=max(num,num*max_val)
            min_val=min(num,num*min_val)
            ans=max(ans,max_val)
        return ans