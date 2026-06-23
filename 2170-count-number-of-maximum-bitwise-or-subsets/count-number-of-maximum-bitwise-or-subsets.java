class Solution {
    public int countMaxOrSubsets(int[] nums) {
        int maxi=0, dp[]=new int[1 << 17 ];
        dp[0]=1;
        for (int n: nums){
            for (int i=maxi; i>=0;--i){
                dp[i | n] += dp[i];
            }
            maxi |=n;
        }
        return dp[maxi];
    }
}