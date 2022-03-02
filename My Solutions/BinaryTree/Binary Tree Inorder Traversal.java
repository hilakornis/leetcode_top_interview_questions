class Solution {
    public List<Integer> inorderTraversal(TreeNode root) {
        List<Integer> ls = new ArrayList<Integer>();        
        aux(root, ls);
        return ls;    
    }
    
    
    private void aux(TreeNode root, List<Integer> ls){
        if(root == null)
            return;
        aux(root.left, ls);
        ls.add(root.val);        
        aux(root.right, ls)    ;    
    }
    
    

    
}

