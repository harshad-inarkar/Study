class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def buildTree(inorder, postorder):
    """
    Builds a binary tree from inorder and postorder traversal arrays.
    Args:
        inorder (List[int]): Inorder traversal of the tree.
        postorder (List[int]): Postorder traversal of the tree.
    Returns:
        TreeNode: The root of the constructed binary tree.
    """
    if not inorder or not postorder:
        return None

    # Map value to its index in inorder for O(1) lookups
    idx_map = {val: idx for idx, val in enumerate(inorder)}

    def helper(in_left, in_right, post_left, post_right):
        if in_left > in_right or post_left > post_right:
            return None
        # The last element in postorder is the root
        root_val = postorder[post_right]
        root = TreeNode(root_val)
        # Root index in inorder
        in_root_idx = idx_map[root_val]
        # Number of nodes in left subtree
        left_size = in_root_idx - in_left
        # Recursively build left and right subtrees
        root.left = helper(in_left, in_root_idx - 1, post_left, post_left + left_size - 1)
        root.right = helper(in_root_idx + 1, in_right, post_left + left_size, post_right - 1)
        return root

    return helper(0, len(inorder) - 1, 0, len(postorder) - 1)

# Helper function to get inorder traversal from tree
def tree_to_inorder(root):
    if not root:
        return []
    return tree_to_inorder(root.left) + [root.val] + tree_to_inorder(root.right)

# Helper function to get postorder traversal from tree
def tree_to_postorder(root):
    if not root:
        return []
    return tree_to_postorder(root.left) + tree_to_postorder(root.right) + [root.val]

# Tests
def test_buildTree():
    # Test 1: Empty tree
    assert buildTree([], []) == None

    # Test 2: Single node
    root = buildTree([1], [1])
    assert root.val == 1 and root.left is None and root.right is None

    # Test 3: Complete binary tree
    inorder = [9,3,15,20,7]
    postorder = [9,15,7,20,3]
    root = buildTree(inorder, postorder)
    assert tree_to_inorder(root) == inorder
    assert tree_to_postorder(root) == postorder

    # Test 4: Skewed left
    inorder = [3,2,1]
    postorder = [3,2,1]
    root = buildTree(inorder, postorder)
    assert tree_to_inorder(root) == inorder
    assert tree_to_postorder(root) == postorder

    # Test 5: Skewed right
    inorder = [1,2,3]
    postorder = [3,2,1]
    root = buildTree(inorder, postorder)
    assert tree_to_inorder(root) == inorder
    assert tree_to_postorder(root) == postorder

    print("All tests passed!")

test_buildTree()

