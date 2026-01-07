# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        mod = 1000000007

        # If we know the sum of a subtree, the answer is max( (total_sum - subtree_sum) * subtree_sum) in each node.

        def dfs(node):
            if not node:
                return 0
            node.val += dfs(node.right) + dfs(node.left)
            return node.val
        total = dfs(root)

        ans = 0
        q = deque([root])
        while q:
            node = q.popleft()
            if not node:
                continue
            current_product = (total-node.val)*node.val
            ans = max(ans,current_product)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

        return ans%mod