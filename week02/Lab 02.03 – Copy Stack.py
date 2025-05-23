class ArrayStack :
    def __init__(self):
        self.size = 0
        self.data = list()

    def push(self, input_data):
        """push"""
        try:
            if input_data.isdigit():
                input_data = int(input_data)
            elif input_data.replace(".", "", 1).isdigit():
                input_data = float(input_data)
        except (TypeError, ValueError, ArithmeticError, AttributeError):
            pass
        finally:
            self.data.append(input_data)
            self.size += 1

    def get_stack_top(self):
        """get_stack_top"""
        if self.get_size() != 0 :
            tmp_data = self.pop()
            self.data.append(tmp_data)
            return tmp_data
        else :
            print("Underflow: Cannot get stack top from an empty list")
            return None

    def pop(self):
        """pop"""
        if self.get_size() != 0 :
            pop_data = self.data.pop()
            self.size -= 1
            return pop_data
        else :
            print("Underflow: Cannot pop data from an empty list")
            return None
    
    def get_size(self):
        """get_size"""
        return self.size
    
    def is_empty(self):
        """is_empty"""
        return True if self.get_size() == 0 else False
    
    def print_stack(self):
        """print_stack"""
        print(self.data)

def print_status():
  """Print all stacks"""
  print("This is stack 1 (%d): " % STACK1_.get_size(), end='')
  STACK1_.print_stack()
  print("This is stack 2 (%d): " % STACK2_.get_size(), end='')
  STACK2_.print_stack()
  print("This is stack 3 (%d): " % STACK3_.get_size(), end='')
  STACK3_.print_stack()
  print("This is stack 4 (%d): " % STACK4_.get_size(), end='')
  STACK4_.print_stack()
  print()

def copy_stack(stack1, stack2):
    temp_stack = ArrayStack()
    while not stack2.is_empty():
        stack2.pop()

    while not stack1.is_empty():
        temp_stack.push(stack1.pop())

    while not temp_stack.is_empty():
        element = temp_stack.pop()
        stack1.push(element)
        stack2.push(element)


STACK1_ = ArrayStack()
STACK2_ = ArrayStack()

STACK3_ = ArrayStack()
STACK4_ = ArrayStack()

# เพิ่มข้อมูลใน Stack1
for _ in range(int(input())):
  STACK1_.push(input())

# เพิ่มข้อมูลใน Stack2
for _ in range(int(input())):
  STACK2_.push(input())

TEMP1_, TEMP2_, TEMP3_, TEMP4_ = id(STACK1_), id(STACK2_), id(STACK3_), id(STACK4_)

print("Copy Stack 2 to Stack 4")
copy_stack(STACK2_, STACK4_)
print_status()

print("Copy Stack 1 to Stack 3")
copy_stack(STACK1_, STACK3_)
STACK1_.push("A")
print_status()

print("Copy Stack 2 to Stack 1")
copy_stack(STACK2_, STACK1_)
STACK2_.push("B")
print_status()

print("Copy Stack 3 to Stack 2")
copy_stack(STACK3_, STACK2_)
STACK3_.push("C")
print("Copy Stack 1 to Stack 3")
copy_stack(STACK1_, STACK3_)
STACK1_.push("D")
print("Copy Stack 2 to Stack 4")
copy_stack(STACK2_, STACK4_)
STACK2_.push("E")
print_status()

print(TEMP1_ == id(STACK1_), TEMP2_ == id(STACK2_), TEMP3_ == id(STACK3_), TEMP4_ == id(STACK4_))