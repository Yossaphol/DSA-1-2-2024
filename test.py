# class Dog:
#   def __init__(self, name, owner):
#     self.name = name 
#     self.__owner = owner #owner ถูกห่อหุ้ม
#   def getOwnwer(self): #getter ของ owner เรียกใช้เพื่อ เรียกใช้ค่า owner ของ object
#     return self.__owner
#   def setOwner(self, owner):#setter ของ owner เรียกใช้เพื่อ กำหนดค่าowner ของ object
#     self.__owner = owner
# pup = Dog("Pluto", "Mickey")
# print(pup.getOwner()) #การเรียกใช้ getter
# pup.setOwner("Donald") #การเรียกใช้ setter
# print(pup.getOwnwer())

l1st = []
for i in range(int(input())):
    l1st.append("")

print(l1st)

l1st2 = [None]
print(l1st2*int(input()))