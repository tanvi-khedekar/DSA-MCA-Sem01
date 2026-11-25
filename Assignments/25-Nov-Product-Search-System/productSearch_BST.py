# Q. 1 E-Commerce Product Search System
# An e-commerce company maintains product IDs in a BST to enable efficient product searching.
# Tasks:
# 1. Create a BST using product IDs.
#    Insert the following product IDs:
#    150, 100, 200, 75, 125, 175, 250, 60, 90, 110.
# 2. Display product IDs in ascending order.
# 3. Search for product ID 175 exists.
# 4. Delete product ID 100.
# 5. Display the BST using inorder, preorder, and postorder traversals.
# 6. Find the minimum and maximum product IDs.

class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def isempty(self):
        return self.root == None

    def insert(self, val):
        nn = Node(val)

        if self.isempty():
            self.root = nn
            return

        temp = self.root
        while True:
            if val < temp.data:
                if temp.left == None:
                    temp.left = nn
                    break
                temp = temp.left
            elif val > temp.data:
                if temp.right == None:
                    temp.right = nn
                    break
                temp = temp.right
            else:
                break

    def search(self, val):
        temp = self.root
        while temp:
            if val == temp.data:
                return True
            elif val < temp.data:
                temp = temp.left
            else:
                temp = temp.right
        return False

    def find_min(self):
        if self.isempty():
            return None
        temp = self.root
        while temp.left:
            temp = temp.left
        return temp.data

    def find_max(self):
        if self.isempty():
            return None
        temp = self.root
        while temp.right:
            temp = temp.right
        return temp.data

    def delete(self, val):
        self.root = self._delete_rec(self.root, val)

    def _delete_rec(self, curr, val):
        if curr == None:
            return curr

        if val < curr.data:
            curr.left = self._delete_rec(curr.left, val)
        elif val > curr.data:
            curr.right = self._delete_rec(curr.right, val)
        else:
            # Node with 0 or 1 child
            if curr.left == None:
                return curr.right
            elif curr.right == None:
                return curr.left

            # Node with 2 children: get inorder successor (min in right subtree)
            temp = curr.right
            while temp.left:
                temp = temp.left

            curr.data = temp.data
            curr.right = self._delete_rec(curr.right, temp.data)

        return curr

    def inorder(self, curr):
        if curr:
            self.inorder(curr.left)
            print(curr.data, end=" ")
            self.inorder(curr.right)

    def preorder(self, curr):
        if curr:
            print(curr.data, end=" ")
            self.preorder(curr.left)
            self.preorder(curr.right)

    def postorder(self, curr):
        if curr:
            self.postorder(curr.left)
            self.postorder(curr.right)
            print(curr.data, end=" ")


# Main program
bst = BST()

# 1. Insert the given product IDs
product_ids = [150, 100, 200, 75, 125, 175, 250, 60, 90, 110]
for pid in product_ids:
    bst.insert(pid)

# 2. Display product IDs in ascending order (Inorder traversal)
print("Product IDs in ascending order:")
bst.inorder(bst.root)
print()

# 3. Search if product ID 175 exists
print("\nSearching for product ID 175:")
if bst.search(175):
    print("Product ID 175 exists.")
else:
    print("Product ID 175 does not exist.")

# 4. Delete product ID 100
print("\nDeleting product ID 100...")
bst.delete(100)

# 5. Display the BST using inorder, preorder, and postorder traversals
print("\nInorder traversal:")
bst.inorder(bst.root)
print()

print("Preorder traversal:")
bst.preorder(bst.root)
print()

print("Postorder traversal:")
bst.postorder(bst.root)
print()

# 6. Find the minimum and maximum product IDs
print("\nMinimum product ID:", bst.find_min())
print("Maximum product ID:", bst.find_max())


