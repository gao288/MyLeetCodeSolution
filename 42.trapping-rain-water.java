class Solution {
    public int trap(int[] height) {
    int curr = 0;
		int find = 0;
		int rain = 0;
		int next_rain= 0;
		while(curr < height.length){
			find++;

			if(find == height.length){
				curr++;
				next_rain = 0;
				find = curr;
			}
			else if(height[find] < height[curr]){
				next_rain += height[curr] - height[find];

			}
			else{
				rain += next_rain;
				next_rain = 0;
				curr = find;
			}

		}
		return rain;

    }
    public static void main(String [] args){
    	Solution S = new Solution();
    	int height[] = {4,2,3};
    	System.out.println(S.trap(height));
	}
}
