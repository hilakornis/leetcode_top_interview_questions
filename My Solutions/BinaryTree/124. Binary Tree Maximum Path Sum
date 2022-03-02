/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    private int maxSum = Integer.MIN_VALUE;
    private int aux(TreeNode root){
        if(root == null){
            return 0;
        }
        int leftMax  = aux(root.left);
        int rightMax = aux(root.right);
        int maxLeftRight = Math.max(leftMax, rightMax);
        int maxNode = Math.max(maxLeftRight + root.val, root.val);
        int maxAll = Math.max(maxNode, leftMax + root.val + rightMax);
        maxSum = Math.max(maxSum, maxAll);
        return maxNode;
    }
    
    public int maxPathSum(TreeNode root) {
        aux(root);
        return maxSum;
    }
    
    
}