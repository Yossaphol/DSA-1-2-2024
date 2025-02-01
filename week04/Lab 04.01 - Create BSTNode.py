class BSTNode:
    def __init__(self, data: int=None):
        """ > w < """
        self.data = data
        self.left = None
        self.right = None

def main(data):
    p = BSTNode(data)
    print(p)
    print(p.data)
    print(p.left)
    print(p.right)
main(int(input()))