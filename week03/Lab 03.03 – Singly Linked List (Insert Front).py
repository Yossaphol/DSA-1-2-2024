class DataNode:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.count = 0
        self.head = None
    def traverse(self):
        if self.head == None:
            print("This is an empty list.")
        else:
            temp = self.head
            while temp:
                print(temp.data, end=' -> ' if temp.next else '\n')
                temp = temp.next
    def insert_last(self, data):
      a = DataNode(data)
      if self.head is None:
        self.head = a
        self.count += 1
      else :
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = a
    def insert_front(self, data):
        a = DataNode(data)
        if self.head is None:
           self.head = a
           self.count += 1
        else:
           a.next = self.head
           self.head = a
           self.count += 1
    # def insert_before(self, node, data):

    # def delete(self, data):


def main():
  mylist = SinglyLinkedList()
  for _ in range(int(input())):
    text = input()
    condition, data = text.split(": ")
    if condition == "F":
      mylist.insert_front(data)
    elif condition == "L":
      mylist.insert_last(data)
    # elif condition == "B":
    #     mylist.insert_before(*data.split(", "))
    # elif condition == "D":
    #     mylist.delete(data)
    else:
      print("Invalid Condition!")
  mylist.traverse()

main()