private void aux(TreeNode root, List<Integer> ls){
        if(root == null)
            return;
        ls.add(root.val);
        aux(root.left, ls);
        aux(root.right, ls)    ;    
    }
    public List<Integer> preorderTraversal(TreeNode root) {        
        List<Integer> ls = new ArrayList<Integer>();
        
        aux(root, ls);
        return ls;
    }
	public List<Integer> preorderTraversal(TreeNode root){
        Stack<TreeNode> stack = new Stack<TreeNode>();
        List<Integer> ls = new ArrayList<Integer>();
        if (root == null)
            return ls;
        stack.push(root);
        while(!stack.isEmpty()){
            TreeNode node = stack.pop();
            ls.add(node.val);
            if(node.right != null){
                stack.push(node.right);
            }
            if(node.left != null){
                stack.push(node.left);
            }
        }
        return ls;
    }