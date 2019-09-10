/*
 * @lc app=leetcode id=55 lang=java
 *
 * [55] Jump Game
 */
class Solution55 {
    public boolean canJump(int[] nums) {
        boolean[] dp = new boolean[nums.length];
        dp[nums.length-1] = true;
        for(int i = nums.length-2 ; i >= 0; i--){
            for(int j = nums[i]; j>0;j--){
                if(i+j < nums.length){
                    dp[i] |= dp[i+j];
                }
            }
        }

        return dp[0];
    }
    public static void main(String[] args) {
        Solution55 S = new Solution55();
        System.out.println(S.canJump(new int[]{2,3,1,1,4}));
    }
}

