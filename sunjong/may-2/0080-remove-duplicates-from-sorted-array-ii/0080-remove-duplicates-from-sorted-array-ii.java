class Solution {
    public int removeDuplicates(int[] nums) {
        int idx = 2;
        for (int i = 2; i < nums.length; i++) {
            if (nums[idx - 1] == nums[i] && nums[idx - 2] == nums[i]) continue;
            nums[idx] = nums[i];
            idx++;
        }
        return idx;
    }
}