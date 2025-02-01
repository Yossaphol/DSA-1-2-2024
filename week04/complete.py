class BSTNode:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None
        self.result = ""  
        self.inresult = "" 
        self.postresult = "" 

    def insert(self, data):
        if self.root is None: 
            self.root = BSTNode(data)
        else:
            self.insertion(self.root, data)

    def insertion(self, node:BSTNode, data):
        if data >= node.data:
            if node.right is None:
                node.right = BSTNode(data)
            else:
                self.insertion(node.right, data)
        elif data < node.data:
            if node.left is None:
                node.left = BSTNode(data)
            else:
                self.insertion(node.left, data)

    #Preorder traverse
    def preorder(self):
        self.result = ""
        self.pretraverse(self.root)
        print(self.result)

    def pretraverse(self, node:BSTNode):
        if node:
            self.store_data(node.data)
            self.pretraverse(node.left)
            self.pretraverse(node.right)

    def store_data(self, data):
        self.result += "-> " + str(data) + " "
    
    def store_indata(self, data):
        self.inresult += "-> " + str(data) + " "

    #Inorder
    def inorder(self):
        self.inresult = ""
        self.inordertra(self.root)
        print(self.inresult)
        
    def inordertra(self, node:BSTNode):
        if node:
            self.inordertra(node.left)
            self.store_indata(node.data)
            self.inordertra(node.right)
            
    def postorder(self):
        self.postresult = ""
        self.posttraverse(self.root)
        print(self.postresult)
        
    def posttraverse(self, node:BSTNode):
        if node:
            self.posttraverse(node.left)
            self.posttraverse(node.right)
            self.storepostdata(node.data)
    
    def storepostdata(self, data):
        self.postresult+="-> "+str(data)+" "
        
        

    def traverse(self):
        if self.is_empty(self.root):
            print("This is an empty binary search tree.") 
        else:
            print("Preorder: ", end="")
            self.preorder()
            print("Inorder: ", end="")
            self.inorder()
            print("Postorder: ", end="")
            self.postorder()
        
    def is_empty(self, node:BSTNode):
        return node is None
    
    def find_max(self, node: BSTNode):
        current = node
        while current.right:
            current = current.right
        return current

        
    def find_min(self):
        if self.root is None:
            return None
        current = self.root
        while current.left:
            current = current.left
        return current.data
    
    
        
        
    def delete(self, data):
        self.root = self._delete_recursive(self.root, data)

    def _delete_recursive(self, node: BSTNode, data):
        if node is None:
            print("Delete Error, "+str(data)+" is not found in Binary Search Tree.")
            return None

        if data < node.data:
            node.left = self._delete_recursive(node.left, data)
        elif data > node.data:
            node.right = self._delete_recursive(node.right, data)
        else:
            # Case 1 No child
            '''
            if node.left is None and node.right is None:
                return None
            '''
            # Case 2 One child
            if node.left is None:
                return node.right
            if node.right is None:
                return node.left
            # Case 3 Two child
            max_in_left = self.find_max(node.left)
            node.data = max_in_left.data
            node.left = self._delete_recursive(node.left,node.data)


        return node


        
            

def main():
  my_bst = BST()
  for i in range(int(input())):
    my_bst.insert(int(input()))
    
  print("Preorder: ", end="")
  my_bst.preorder()

main()