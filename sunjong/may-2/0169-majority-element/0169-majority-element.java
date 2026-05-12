class Solution {
    public int majorityElement(int[] nums) {
        int majority = nums.length / 2;
        Arrays.sort(nums);

        int num = nums[0];
        int cnt = 0;
        for (int i = 0; i < nums.length; i++) {
            if (num != nums[i]) {
                num = nums[i];
                cnt = 0;
            }
            cnt++;
            if (cnt > majority) break;
        }
        return num;
    }
}