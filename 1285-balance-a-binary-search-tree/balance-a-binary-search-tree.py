# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        inorder = []

        def inorder1(root,inorder):
            if not root:
                return
            inorder1(root.left,inorder)
            inorder.append(root.val)
            inorder1(root.right,inorder)

        inorder1(root,inorder)

        def balance_bst(inorder,start,end):
            if start>end:
                return None

            mid = (start+end )//2
            left = balance_bst(inorder,start,mid-1)
            right = balance_bst(inorder,mid+1,end)
            node = TreeNode(inorder[mid],left,right)
            return node


        return balance_bst(inorder,0,len(inorder)-1)    