# Given the root of a binary tree, return the length of the diameter of the tree.
# The diameter of a binary tree is the length of the longest path between any two nodes in a tree.
# Initialize an integer variable: diameter; keep track of the longest path so far
# Implement a recursive function longestPath which takes a tree node as input.
# It checks Left and Right and sum - whichever is the longest
# Finally return longer one

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        diameter = 0
        def l_path(node):
            if node is None:
                return 0
            nonlocal diameter

            # recursively find the longest path in both left child and right child

            left_path = l_path(node.left) # returns max of (l, r) +1
            right_path = l_path(node.right)

            # update the diameter if left_path plus right_path is larger
            diameter = max(diameter, left_path + right_path)

            # return the longest one between left_path and right_path;
            # remember to add 1 for the path connecting the node and its parent
            return max(left_path, right_path) + 1

        l_path(root)
        return diameter
    
# You are given the root of a binary search tree (BST) and an integer val. 
# Find the node in the BST that the node's value equals val and return the subtree rooted with that node. 
# If such a node does not exist, return null.    
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        # while traversalNode is true, if found? return node. else if node.val < VAL then set trav nide to node.Left
        trav = root
        while trav:
            if trav.val == val:
                return trav
            elif trav.val < val:
                trav = trav.right
            else:
                trav = trav.left



# Return the same tree where every subtree (of the given tree) not containing a 1 has been removed.
# Prune children of the tree recursively. The only decisions at each node are whether to prune the left child or the right child.
# We'll use a function containsOne(node) that does two things: it tells us whether the subtree at this node contains a 1, and it also prunes all subtrees not containing 1.
# If for example, node.left does not contain a one, then we should prune it via node.left = null.
# Also, the parent needs to be checked. If for example the tree is a single node 0, the answer is an empty tree.


 def pruneTree(self, root):
        def containsOne(node):
            if not node: 
              return False
            a1 = containsOne(node.left)
            a2 = containsOne(node.right)
            if not a1: 
              node.left = None
            if not a2: 
              node.right = None
            return node.val == 1 or a1 or a2

        return root if containsOne(root) else None
        
        
        
        
# Tilt
# Sum of left - Sum of right = root
# Post-Order DFS Traversal
# The overall idea is that we traverse each node, and calculate the tilt value for each node. 
# At the end, we sum up all the tilt values, which is the desired result of the problem.
# et us first implement the function valueSum(node) which returns the sum of values for all nodes starting from the given node, which can be summarized with the following recursive formula:
#\text{valueSum(node)} = \text{node.val} + \text{valueSum(node.left)} + \text{valueSum(node.right)}valueSum(node)=node.val+valueSum(node.left)+valueSum(node.right)
#Furthermore, the tilt value of a node also depends on the value sum of its left and right subtrees, as follows:
#\text{tilt(node)} = |\text{valueSum(node.left)} - \text{valueSum(node.right)}|tilt(node)=∣valueSum(node.left)−valueSum(node.right)∣


def findTilt(self, root: TreeNode) -> int:
  total_tilt = 0
  def valueSum(node)
     if not node:
      return 0
     leftSum = valueSum(node.left)
     rightsum =  valueSum(node.right)
     tilt = abs(left_sum - right_sum)
     total_tilt += tilt
     return leftSum + rightSum + node.val
   valueSum(root)
   return total_tilt
     
  
class Solution:
    def invertTree(self, root):
        if root is None:
            return None
        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root

    
    
    
    
 class Solution:
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        def construct(l, r):
            if l > r:
                return
            elif l == r:
                return TreeNode(nums[l])
            maximum = -float('inf')
            for i in range(l, r+1):
                if maximum < nums[i]:
                    maximum = nums[i]
                    max_index = i
            left = construct(l, max_index-1)
            right = construct(max_index+1,r)
            root = TreeNode(maximum)
            root.left = left
            root.right = right
            return root
        return construct(0, len(nums)-1)
    
    
    
    
    
    
    
    #Inorder
    
def inorderTraversal1(self, root):
    res = []
    self.helper(root, res) #Call the recursive helper
    return res
    
def helper(self, root, res):
    if root:
        self.helper(root.left, res) # Till left exists keep going - get L
        res.append(root.val) # Append root
        self.helper(root.right, res) #Roots right
 
# iteratively       
def inorderTraversal(self, root):
    res, stack = [], []
    while True:
        while root:
            stack.append(root)
            root = root.left # Till left exists keep going left and append to stack *for every node*
        if not stack:
            return res # If nothing in stack- no tree
        node = stack.pop() # pop from stack - left most child
        res.append(node.val) # append node's value
        root = node.right # go to right

