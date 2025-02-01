class BSTNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = BSTNode(data)
        else:
            current = self.root
            while True:
                if data < current.data:
                    if current.left is None:
                        current.left = BSTNode(data)
                        break
                    current = current.left
                else:
                    if current.right is None:
                        current.right = BSTNode(data)
                        break
                    current = current.right

    def preorder(self, root = 'start'):
        if root == 'start':
            self.preorder(self.root)
            return
        if root:
            print(' ->', root.data, end='')
            self.preorder(root.left)
            self.preorder(root.right)
    def inorder(self, root = 'start'):
        if root == 'start':
            self.inorder(self.root)
            return
        if root:
            self.inorder(root.left)
            print(' ->', root.data, end='')
            self.inorder(root.right)
    def postorder(self, root = 'start'):
        if root == 'start':
            self.postorder(self.root)
            return
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            print(' ->', root.data, end='')
def main():
    my_bst = BST()
    for i in range(int(input())):
        my_bst.insert(int(input()))

    print("Preorder:", end="")
    my_bst.preorder()

main()
