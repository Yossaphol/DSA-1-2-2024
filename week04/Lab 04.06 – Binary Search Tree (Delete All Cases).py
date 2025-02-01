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
    def is_empty(self):
        if self.root is None:
            return True
        return False
    def traverse(self):
        if self.root is None:
            print("This is an empty binary search tree.")
        else:
            print("Preorder:", end="")
            self.preorder()
            print("\nInorder:", end="")
            self.inorder()
            print("\nPostorder:", end="")
            self.postorder()
    def find_min(self):
        if self.root is None:
            return None
        else:
            current = self.root
            while (current.left):
                current = current.left
            return current.data
            
    def find_max(self, root = 'start'):
        if root == 'start':
            current = self.root
        else:
            current = root
        if self.root is None:
            return None
        else:
            while (current.right):
                current = current.right
            
            return current.data
    
    def delete(self, data):
        prev = BSTNode(None)
        start = self.root
        if start.data == data:
            if start.left and start.right is None:
                self.root = start.left
            if start.left is None and start.right:
                self.root = start.right
            if start.left is None and start.right is None:
                self.root = None
        if start is None:
                print("Delete Error, %s is not found in Binary Search Tree." %(data))
                return
        while (start.data != data):
            if start.data < data: 
                prev = start
                start = start.right
            else:
                prev = start
                start = start.left
            if start is None:
                print("Delete Error, %s is not found in Binary Search Tree." %(data))
                return
        if start.left is None and start.right is None:
            if prev.left == start:
                prev.left = None
            if prev.right == start:
                prev.right = None
        if start.left and start.right is None:
            if prev.left == start:
                prev.left = start.left
            if prev.right == start:
                prev.right = start.left
        if start.left is None and start.right :
            if prev.left == start:
                prev.left = start.right
            if prev.right == start:
                prev.right = start.right
        if start.left and start.right:
            num = self.delete(self.find_max(start.left))
            start.data = num
        return data
def main():
  my_bst = BST()
  while 1:
    text = input()
    if text == "Done":
      break
    condition, data = text.split(": ")
    if condition == "I":
      my_bst.insert(int(data))
    elif condition == "D":
      my_bst.delete(int(data))
    else:
      print("Invalid Condition")
  my_bst.traverse()

main()
