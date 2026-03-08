class Solution {
    public double findMaxAverage(int[] nums, int k) {
        long window_sum=0;
        for (int i=0; i<k;i++){
            window_sum+=nums[i];
        }
        long max_sum=window_sum;

        for (int i=k;i<nums.length;i++){
            window_sum+=nums[i]-nums[i-k];
            max_sum=Math.max(max_sum,window_sum);
        }
        return max_sum/1.0/k;
    }
}