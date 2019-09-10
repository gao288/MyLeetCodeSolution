import java.util.ArrayList;
import java.util.Arrays;

/*
 * @lc app=leetcode id=18 lang=java
 *
 * [18] 4Sum
 *
 * https://leetcode.com/problems/4sum/description/
 *
 * algorithms
 * Medium (30.11%)
 * Total Accepted:    223.9K
 * Total Submissions: 742.7K
 * Testcase Example:  '[1,0,-1,0,-2,2]\n0'
 *
 * Given an array nums of n integers and an integer target, are there elements
 * a, b, c, and d in nums such that a + b + c + d = target? Find all unique
 * quadruplets in the array which gives the sum of target.
 * 
 * Note:
 * 
 * The solution set must not contain duplicate quadruplets.
 * 
 * Example:
 * 
 * 
 * Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.
 * 
 * A solution set is:
 * [
 * ⁠ [-1,  0, 0, 1],
 * ⁠ [-2, -1, 1, 2],
 * ⁠ [-2,  0, 0, 2]
 * ]
 * 
 * 
 */


//time: O(n^3)
//Space: O(n)
class Solution {
    public List<List<Integer>> fourSum(int[] nums, int target) {
        List<List<Integer>> res = new ArrayList<>();
        if(nums.length<4){
            return res;
        }
        Arrays.sort(nums);
        for(int i = 0; i < nums.length - 3; ++i){
            if(i > 0 && nums[i] == nums[i-1]){
                continue;
            }
            for(int j = i+1; j < nums.length - 2; ++j){
                if(j > i+1 && nums[j] == nums[j-1]) continue;
                int low = j + 1, high = nums.length-1;
                while(low < high){
                    int sum = nums[i] + nums[j] + nums[low] + nums[high];
                    if(sum == target){
                        res.add(Arrays.asList(nums[i],nums[j],nums[low],nums[high]));
                        while(low < high && nums[low] == nums[low+1]) low++;
                        while(low < high && nums[high] == nums[high - 1]) high--;
                        low++;
                        high--;
                    }else if(sum < target){
                        low++;
                    }else{
                        high--;
                    }
                }
            }
        }
        return res;
    }
}

