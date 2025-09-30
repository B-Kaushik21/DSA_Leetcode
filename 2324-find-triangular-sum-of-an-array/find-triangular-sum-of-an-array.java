class Solution {
    public int triangularSum(int[] nums) {
        int ans=0;
        int k=nums.length;
        while(k!=1){
            for(int i=0;i<k-1;i++){
                nums[i]=(nums[i]+nums[i+1])%10;
            }
            k-=1;
        }
        return nums[0];
    }
}