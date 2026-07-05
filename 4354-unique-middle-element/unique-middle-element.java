class Solution {
    public boolean isMiddleElementUnique(int[] nums) {
        int n=nums.length;
        int mid=nums[n/2];
        //System.out.println(mid);
        
        for(int i=0; i<n/2;i++){
            if(nums[i]==mid || nums[i+(n/2)+1]==mid){
                return false;
            }
        }
        return true;
    }
}