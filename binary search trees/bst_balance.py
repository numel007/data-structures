class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def get_array(self, root, array=None):
        if array == None:
            array = []

        if root == None:
            return

        self.get_array(root.left, array)
        array.append(root)
        self.get_array(root.right, array)
        return array

    def createBST(self, startIndex, endIndex, array):
        if startIndex > endIndex:
            return None

        middleIndex = (endIndex + startIndex) // 2
        middleNode = array[middleIndex]

        middleNode.left = self.createBST(startIndex, middleIndex-1, array)
        middleNode.right = self.createBST(middleIndex+1, endIndex, array)

        return middleNode

    def balanceBST(self, root: TreeNode) -> TreeNode:
        sorted_array = self.get_array(root)

        return self.createBST(0, len(sorted_array)-1, sorted_array)


# TESTING
node_10 = TreeNode(10)
node_10.left = TreeNode(8)
node_10.left.left = TreeNode(7)
node_10.left.left.left = TreeNode(6)
node_10.left.left.left.left = TreeNode(5)
testing = Solution()
testing.balanceBST(node_10)
testing.preOrder(node_10)
