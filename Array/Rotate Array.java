class Solution {
    public void rotate(int[] nums, int k) {
        int n = nums.length;
        k = k % n ; 
        if (nums == null || k == 0) {
            return;
        }
       this.reverse(nums, 0, n-1) ;
       this.reverse(nums, 0, k-1) ;
       this.reverse(nums, k, n-1);
        
    }
    public void reverse(int[] nums,int start, int end){        
        int temp = 0;
        while(start < end){
            temp = nums[end];
            nums[end] = nums[start];
            nums[start] = temp;
            start ++;
            end --;
        }
        
    }
}