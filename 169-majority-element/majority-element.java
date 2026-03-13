class Solution {
    public int majorityElement(int[] nums) {
        int n=nums.length;
        HashMap<Integer,Integer> store= new HashMap<>();
        for (int num:nums){
            if (!store.containsKey(num)){
                store.put(num,1);
            }else{
                store.put(num,store.get(num)+1);
                
            }
        }
        for(Map.Entry<Integer,Integer> entry: store.entrySet()){
            if (entry.getValue()>n/2){
                return entry.getKey();
            }
        }
        return -1;
    }
}