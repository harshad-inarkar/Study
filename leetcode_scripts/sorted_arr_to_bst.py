class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def sortedArrayToBST(nums):

    def build(left, right):
        if left > right:
            return None
        mid = (left + right) // 2
        root = TreeNode(nums[mid])
        root.left = build(left, mid-1)
        root.right = build(mid+1, right)
        return root

    return build(0, len(nums)-1)

# Helper function to check if a tree is a valid BST and matches the sorted array
def inorder_traversal(root):
    if not root:
        return []
    return inorder_traversal(root.left) + [root.val] + inorder_traversal(root.right)

# Tests
def test_sortedArrayToBST():
    # Test 1: Empty array
    arr = []
    root = sortedArrayToBST(arr)
    assert root is None

    # Test 2: Single element
    arr = [1]
    root = sortedArrayToBST(arr)
    assert root.val == 1
    assert root.left is None
    assert root.right is None

    # Test 3: Odd number of elements
    arr = [1, 2, 3]
    root = sortedArrayToBST(arr)
    assert inorder_traversal(root) == arr

    # Test 4: Even number of elements
    arr = [1, 2, 3, 4]
    root = sortedArrayToBST(arr)
    assert inorder_traversal(root) == arr

    # Test 5: Larger array
    arr = [-10, -3, 0, 5, 9]
    root = sortedArrayToBST(arr)
    assert inorder_traversal(root) == arr

test_sortedArrayToBST()
