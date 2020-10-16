class BstNode:

    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right


def bst_serialization(root):
    """ BST serialization using pre-order traversal

    :param root: root node
    :return: pre-order array of the BST
    """
    if root is None:
        return []
    left, right = [], []
    if root.left is not None:
        left = bst_serialization(root.left)
    if root.right is not None:
        right = bst_serialization(root.right)

    return [root.value] + left + right


def bst_non_recursive_deserialization(arr):
    """ Non-recursive solution for deserializing BST

    :param arr: pre-order array of BST
    :return: reconstructed BST
    """
    if arr is None or arr is []:
        return None

    root = BstNode(arr[0], None, None)
    stack = [root]
    for val in arr[1:]:
        node = BstNode(val, None, None)

        if stack[-1].value >= val:
            stack[-1].left = node
        else:
            p = stack.pop()
            while len(stack) > 0 and stack[-1].value < val:
                p = stack.pop()
            p.right = node

        stack.append(node)

    return root


def bst_recursive_deserialization(arr):
    """ Recursive solution for deserializing BST

    :param arr: pre-order array of BST
    :return: reconstructed BST
    """
    root, right = bst_rec_des_helper(0, float('inf'), arr)
    return root


def bst_rec_des_helper(start_index, end_value, arr):
    """ Given subtree root index, the helper function reconstruct the subtree, return the root and index of the root of
    the next subtree.

    :param start_index: inclusive start index of the subtree in the array
    :param end_value: exclusive end value of the subtree. We use value index of index because the index is unknown
    :param arr: deserialized array
    :return: root of the subtree and starting index of the right subtree
    """
    if start_index >= len(arr) or arr[start_index] >= end_value:
        return None, start_index

    # recursively reconstruct the left subtree
    left_root, next_start_index = bst_rec_des_helper(start_index+1, arr[start_index], arr)
    # recursively reconstruct the right subtree
    right_root = None
    if next_start_index < len(arr) and arr[next_start_index] < end_value:
        # the right subtree is not empty
        right_root, next_start_index = bst_rec_des_helper(next_start_index, end_value, arr)

    return BstNode(arr[start_index], left_root, right_root), next_start_index


def print_tree(root):
    if root is not None:
        if root.left is not None:
            print(root.value, "-left->", root.left.value)
            print_tree(root.left)
        if root.right is not None:
            print(root.value, "-right->", root.right.value)
            print_tree(root.right)


n1 = BstNode(1, None, None)
n3 = BstNode(3, None, None)
n2 = BstNode(2, n1, n3)
n4 = BstNode(4, n2, None)
n7 = BstNode(7, None, None)
n10 = BstNode(10, None, None)
n9 = BstNode(9, None, n10)
n8 = BstNode(8, n7, n9)
n5 = BstNode(5, n4, n8)


array = bst_serialization(n5)
print("--original BST--")
print_tree(n5)
print("--serialized BST--")
print(array)
bst = bst_recursive_deserialization(array)
print("--BST from recursive deserialization--")
print_tree(bst)
print("--BST  from non-recursive deserialization--")
bst = bst_non_recursive_deserialization(array)
print_tree(bst)
