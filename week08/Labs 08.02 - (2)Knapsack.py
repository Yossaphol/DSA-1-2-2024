class Item:
    def __init__(self, name, price, weight):
        self.name = name
        self.price = price
        self.weight = weight

    def get_name(self):
       return self.name

    def get_price(self):
       return self.price

    def get_weight(self):
       return self.weight

    def get_cost(self):
       return self.price / self.weight
    
def knapsack(amount, itemList):
   itemList.sort(key=lambda item: item.get_cost(), reverse=True)
    
   total_value = 0
   current_weight = 0
   selected_items = []
    
   for item in itemList:
      if current_weight + item.get_weight() <= amount:
         selected_items.append(item)
         current_weight += item.get_weight()
         total_value += item.get_price()
    
   print(f"Knapsack Size: {amount:.1f} kg")
   print("===============================")
   for item in selected_items:
      print(f"{item.get_name()} -> {item.get_weight()} kg -> {item.get_price()} THB")
   print(f"Total: {total_value} THB")

def main():
   import json
   items = []
   num_items = int(input())
   while num_items != 0:
      item_in = json.loads(input())
      items.append(Item(item_in['name'], item_in['price'], item_in['weight']))
      num_items = num_items - 1
   knapsack_capacity = float(input())
   knapsack(knapsack_capacity, items)
main()