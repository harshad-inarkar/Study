class QuadTreeNode:
    def __init__(self, value, isLeaf=False, topleft=None, topright=None, bottomleft=None, bottomright=None):
        self.value = value  
        self.isLeaf =  isLeaf
        self.topleft = topleft
        self.topright = topright
        self.bottomleft = bottomleft
        self.bottomright = bottomright

def construct_quad_tree(grid, x=0, y=0, size=None):

    
    if size is None:
        size = len(grid)
    # Check if all values in this region are the same
    first_val = grid[y][x]
    all_same = True
    for i in range(y, y+size):
        for j in range(x, x+size):
            if grid[i][j] != first_val:
                all_same = False
                break
        if not all_same:
            break
    if all_same:
        return QuadTreeNode(x, y, size, value=first_val)
    else:
        node = QuadTreeNode(x, y, size)
        half = size // 2
        node.children = [
            construct_quad_tree(grid, x, y, half),  # top-left
            construct_quad_tree(grid, x+half, y, half),  # top-right
            construct_quad_tree(grid, x, y+half, half),  # bottom-left
            construct_quad_tree(grid, x+half, y+half, half)  # bottom-right
        ]
        return node

def quad_tree_to_grid(node):
    grid = [[0 for _ in range(node.size)] for _ in range(node.size)]
    def fill(n):
        if n.is_leaf():
            for i in range(n.y, n.y+n.size):
                for j in range(n.x, n.x+n.size):
                    grid[i][j] = n.value
        else:
            for child in n.children:
                fill(child)
    fill(node)
    return grid

def print_quad_tree(node, indent=0):
    prefix = "  " * indent
    if node.is_leaf():
        print(f"{prefix}Leaf(x={node.x}, y={node.y}, size={node.size}, value={node.value})")
    else:
        print(f"{prefix}Node(x={node.x}, y={node.y}, size={node.size})")
        for child in node.children:
            print_quad_tree(child, indent+1)

# TESTS
def test_quad_tree():
    # Test 1: All 0s
    grid1 = [
        [0,0],
        [0,0]
    ]
    qt1 = construct_quad_tree(grid1)
    assert qt1.is_leaf() and qt1.value == 0

    # Test 2: All 1s
    grid2 = [
        [1,1],
        [1,1]
    ]
    qt2 = construct_quad_tree(grid2)
    assert qt2.is_leaf() and qt2.value == 1

    # Test 3: Mixed 2x2
    grid3 = [
        [1,0],
        [0,1]
    ]
    qt3 = construct_quad_tree(grid3)
    assert not qt3.is_leaf()
    assert all(child.is_leaf() for child in qt3.children)
    vals = [child.value for child in qt3.children]
    assert vals == [1,0,0,1]

    # Test 4: 4x4 with a quadrant of 1s
    grid4 = [
        [1,1,0,0],
        [1,1,0,0],
        [0,0,0,0],
        [0,0,0,0]
    ]
    qt4 = construct_quad_tree(grid4)
    # Top-left should be a leaf of 1s
    assert qt4.children[0].is_leaf() and qt4.children[0].value == 1
    # Top-right, bottom-left, bottom-right should be 0s
    assert all(child.is_leaf() and child.value == 0 for child in qt4.children[1:])

    # Test 5: Reconstruct grid from quad tree
    grid5 = [
        [1,1,0,0],
        [1,1,0,0],
        [0,0,1,1],
        [0,0,1,1]
    ]
    qt5 = construct_quad_tree(grid5)
    recon = quad_tree_to_grid(qt5)
    assert recon == grid5

    print("All tests passed.")

if __name__ == "__main__":
    test_quad_tree()
