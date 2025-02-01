class StudentGroup:
    def __init__(self):
        self.student = list()

    def push(self,input_data):
        self.student.append(input_data)

    def pop(self):
        self.student.pop()

    def get_stack_top(self):
        x = self.student.pop()
        self.student.append(x)
        return x
    
def main():
    studentg = StudentGroup()
    group = int(input())
    for _ in range(int(input())):
        studentg.push(input())
    
main()