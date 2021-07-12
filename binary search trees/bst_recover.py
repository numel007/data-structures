class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    previous_node = None
    pointer1 = None
    pointer2 = None

    def iot(self, root):
        if root == None:
            return
        else:
            self.iot(root.left)
            print(root.val)
            self.iot(root.right)

    def inOrder(self, current):

        if current == None:
            return
        else:
            self.inOrder(current.left)
            if self.previous_node == None:
                self.previous_node = current
            else:
                if current.val <= self.previous_node.val:

                    if self.pointer1 == None:
                        self.pointer1 = self.previous_node
                    self.pointer2 = current

                self.previous_node = current

            self.inOrder(current.right)

    def recoverTree(self, root):
        self.inOrder(root)
        self.pointer1.val, self.pointer2.val = self.pointer2.val, self.pointer1.val
        return root


def test_recover():
    node_10 = TreeNode(10)
    node_5 = TreeNode(5)
    node_8 = TreeNode(8)
    node_2 = TreeNode(2)
    node_20 = TreeNode(20)

    node_10.left = node_5
    node_10.right = node_8
    node_5.left = node_2
    node_5.right = node_20
    node_2.left = None
    node_2.right = None
    node_20.left = None
    node_20.right = None
    node_8.left = None
    node_8.right = None

    print('---BEFORE---')
    print(Solution().iot(node_10))

    # Recover tree
    solution_recover = Solution()
    solution_recover.recover(node_10)

    print('---AFTER---')
    print(solution_recover.iot(node_10))


test_recover()
