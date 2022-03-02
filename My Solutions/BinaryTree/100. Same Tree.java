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
    public boolean isSameTree2(TreeNode p, TreeNode q) {
        if(p == null && q == null)
            return true;
        if( p == null || q == null || p.val != q.val)
            return false;
        
        return isSameTree(p.left, q.left) && isSameTree(p.right, q.right);
            
    }
    private boolean check(TreeNode p, TreeNode q){
        if(p == null && q == null)
            return true;
        if( p == null || q == null || p.val != q.val)
            return false;
        return true;
    }
    public boolean isSameTree(TreeNode p, TreeNode q){
        if(!check(p,q))
            return false;
        Queue<TreeNode> queue = new LinkedList<TreeNode>();
        queue.offer(p);
        queue.offer(q);
        while(!queue.isEmpty()){
            p = queue.poll();
            q = queue.poll();
            if(!check(p,q))
                return false;
            if(p != null && q != null){
                queue.offer(p.left);
                queue.offer(q.left);    
                queue.offer(p.right);
                queue.offer(q.right);            
            }
            
            
            
        }
        return true;
    }
}