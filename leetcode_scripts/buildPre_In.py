class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def buildTree(preorder, inorder):
    """
    Builds a binary tree from preorder and inorder traversal arrays.
    Args:
        preorder (List[int]): Preorder traversal of the tree.
        inorder (List[int]): Inorder traversal of the tree.
    Returns:
        TreeNode: The root of the constructed binary tree.
    """
    if not preorder or not inorder:
        return None

    # Map value to its index in inorder for O(1) lookups
    idx_map = {val: idx for idx, val in enumerate(inorder)}

    def helper(pre_left, pre_right, in_left, in_right):
        if pre_left > pre_right or in_left > in_right:
            return None
        # The first element in preorder is the root
        root_val = preorder[pre_left]
        root = TreeNode(root_val)
        # Root index in inorder
        in_root_idx = idx_map[root_val]
        # Number of nodes in left subtree
        left_size = in_root_idx - in_left
        # Recursively build left and right subtrees
        root.left = helper(pre_left + 1, pre_left + left_size, in_left, in_root_idx - 1)
        root.right = helper(pre_left + left_size +1, pre_right, in_root_idx + 1, in_right)
        return root

    return helper(0, len(preorder) - 1, 0, len(inorder) - 1)

# Helper function to get inorder traversal from tree
def tree_to_inorder(root):
    if not root:
        return []
    return tree_to_inorder(root.left) + [root.val] + tree_to_inorder(root.right)

# Helper function to get preorder traversal from tree
def tree_to_preorder(root):
    if not root:
        return []
    return [root.val] + tree_to_preorder(root.left) + tree_to_preorder(root.right)

# Tests
def test_buildTree():
    # Test 1: Empty tree
    assert buildTree([], []) == None

    # Test 2: Single node
    root = buildTree([1], [1])
    assert root.val == 1 and root.left is None and root.right is None

    # Test 3: Complete binary tree
    preorder = [3,9,20,15,7]
    inorder = [9,3,15,20,7]
    root = buildTree(preorder, inorder)
    assert tree_to_preorder(root) == preorder
    assert tree_to_inorder(root) == inorder

    # Test 4: Skewed left
    preorder = [1,2,3]
    inorder = [3,2,1]
    root = buildTree(preorder, inorder)
    assert tree_to_preorder(root) == preorder
    assert tree_to_inorder(root) == inorder

    # Test 5: Skewed right
    preorder = [1,2,3]
    inorder = [1,2,3]
    root = buildTree(preorder, inorder)
    assert tree_to_preorder(root) == preorder
    assert tree_to_inorder(root) == inorder

    # Test 6: Larger tree
    preorder = [1,2,4,5,3,6,7]
    inorder = [4,2,5,1,6,3,7]
    root = buildTree(preorder, inorder)
    assert tree_to_preorder(root) == preorder
    assert tree_to_inorder(root) == inorder

    print("All tests passed!")

test_buildTree()
