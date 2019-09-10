/*
 * @lc app=leetcode id=307 lang=java
 *
 * [307] Range Sum Query - Mutable
 *
 * https://leetcode.com/problems/range-sum-query-mutable/description/
 *
 * algorithms
 * Medium (28.04%)
 * Total Accepted:    68.9K
 * Total Submissions: 245.1K
 * Testcase Example:  '["NumArray","sumRange","update","sumRange"]\n[[[1,3,5]],[0,2],[1,2],[0,2]]'
 *
 * Given an integer array nums, find the sum of the elements between indices i
 * and j (i ≤ j), inclusive.
 * 
 * The update(i, val) function modifies nums by updating the element at index i
 * to val.
 * 
 * Example:
 * 
 * 
 * Given nums = [1, 3, 5]
 * 
 * sumRange(0, 2) -> 9
 * update(1, 2)
 * sumRange(0, 2) -> 8
 * 
 * 
 * Note:
 * 
 * 
 * The array is only modifiable by the update function.
 * You may assume the number of calls to update and sumRange function is
 * distributed evenly.
 * 
 * 
 */

class NumArray {
    
    FenWickTree tree_;
    int[] nums_;
    public NumArray(int[] nums) {
        nums_ = nums;
        tree_ = new FenWickTree(nums.length);
        for(int i = 0; i < nums.length; ++i){
            tree_.update(i+1, nums[i]);
        }
    }
    
    public void update(int i, int val) {
        tree_.update(i + 1, val - nums[i]);
        nums_[i] = val;
    }
    
    public int sumRange(int i, int j) {
        return tree_.query(j+1) - tree_.query(i);
    }
    class FenWickTree{
        int sums_[];
        public FenWickTree(int n){
            sums_ = new int[n+1];
        }
        public void update(int i, int delta){
            while(i<sums_.length){
                sums_[i] += delta;
                i += i & -i;
            }
        }
        public int query(int i){
            int sum = 0;
            while(i>0){
                sum += sums_[i];
                i -= i & -i;
            }
            return sum;
        }
    }
    
}

/**
 * Your NumArray object will be instantiated and called as such:
 * NumArray obj = new NumArray(nums);
 * obj.update(i,val);
 * int param_2 = obj.sumRange(i,j);
 */

