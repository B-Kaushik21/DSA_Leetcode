class Solution {
    public long maximumSubarraySum(int[] nums, int k) {
        HashMap<Integer,Integer> mapp=new HashMap<>();
        long mx=0, sum=0;
        for (int i=0; i<nums.length;i++){
            sum+=nums[i];
            mapp.put(nums[i],mapp.getOrDefault(nums[i],0)+1);
            if (i>=k-1){
                if(mapp.size()==k) mx=Math.max(mx,sum);
                sum-=nums[i-k+1];
                mapp.put(nums[i-k+1],mapp.get(nums[i-k+1])-1);
                if(mapp.get(nums[i-k+1])==0) mapp.remove(nums[i-k+1]);
            }
        }
        return mx;    
    }
}