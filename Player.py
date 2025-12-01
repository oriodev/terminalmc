class Player:
  def __init__(self):
    self.inventory = {}
  
  def add_to_inventory(self, item):
      if item not in self.inventory:
          self.inventory[item] = 0 
      self.inventory[item] += 1 
  
  def remove_from_inventory(self, item):
      if item in self.inventory and self.inventory[item] > 0:
          self.inventory[item] -= 1 
          if self.inventory[item] == 0:
              del self.inventory[item]
  
  def check_inventory(self):
    print('Inventory:')
    if len(self.inventory.items()) == 0:
       print('...')
    else:
      for item, amount in self.inventory.items():
        print(item.title + ' [' + str(amount) + ']')
    
    input('x to close')