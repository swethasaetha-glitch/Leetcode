// Last updated: 6/4/2026, 9:43:00 PM
class Solution {
    public int searchInsert(int[] nums, int target) {
        int n=nums.length;
        for(int i=0;i<n;i++){
            if(nums[i]>=target){
                return i;
            }
        }
        return nums.length;
    }
}