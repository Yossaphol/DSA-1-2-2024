class Elevator:
  def __init__(self, max_floor):
    self.current_floor = 1
    self.max_floor = max_floor

  def go_to_floor(self, floor):
     ...

  def report_current_floor(self):
    print(...)

def main(floor):
  a = Elevator()
  a.go_to_floor(floor)
  loop_floor = int(input())
  while (loop_floor != "Done"):
    
main(int(input()))