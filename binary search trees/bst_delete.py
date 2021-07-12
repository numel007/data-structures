class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def iot(self, root):
        if root is not None:
            self.iot(root.left)
            print(root.val)
            self.iot(root.right)

        return None

    def find_leftmost_node(self, root):
        if root.left == None:
            return root
        else:
            self.find_leftmost_node(root.left)

    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if root == None:
            return root

        if root.val == key:
            if root.left is None and root.right is None:
                print('Deleting leaf node')
                # Leaf node
                return None
            elif (root.left == None and root.right != None) or (root.left != None and root.right == None):
                print('Deleting node with 1 child')
                # Has 1 child
                if root.left is None:
                    return root.right
                else:
                    return root.left
            else:
                print('Deleting node with 2 children')
                # Has 2 children
                # Go to node's right subtree's leftmost node, swap nodes
                temp_node = self.find_leftmost_node(root.right)
                root.val = temp_node.val
                root.right = self.deleteNode(root.right, temp_node.val)
        else:
            if key < root.val:
                root.left = self.deleteNode(root.left, key)
            else:
                root.right = self.deleteNode(root.right, key)

        return root


def test_delete():
    node_5 = TreeNode(5)
    node_3 = TreeNode(3)
    node_2 = TreeNode(2)
    node_4 = TreeNode(4)
    node_6 = TreeNode(6)
    node_7 = TreeNode(7)

    node_5.left = node_3
    node_5.right = node_6
    node_3.left = node_2
    node_3.right = node_4
    node_2.left = None
    node_2.right = None
    node_4.left = None
    node_4.right = None
    node_6.left = None
    node_6.right = node_7
    node_7.left = None
    node_7.right = None

    print('---BEFORE---')
    solution_iot_before = Solution()
    solution_iot_before.iot(node_5)

    # Delete leaf
    solution_delete_node = Solution()
    solution_delete_node.deleteNode(node_5, 3)

    print('---AFTER---')
    solution_delete_node.iot(node_5)


test_delete()
