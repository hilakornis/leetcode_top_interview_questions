# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def aux(left : int, right :int ) -> Optional[TreeNode]:
            nonlocal preorder_index
            nonlocal map_inorder
            if left > right:
                return None
            
            root_val = preorder[preorder_index]
            preorder_index += 1
            root = TreeNode(root_val)
            root.left = aux(left, map_inorder[root_val] - 1)
            root.right = aux(map_inorder[root_val] + 1, right)
            
            return root
        
        preorder_index = 0
        map_inorder = {}
        for i, val in enumerate(inorder):
            map_inorder[val] = i
        
        return aux(0, len(inorder) - 1)
            
        