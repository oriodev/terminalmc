class Crafting:
  def __init__(self, player):
    self.recipes = {
      'plank': ['log'],
      'stick': ['log', 'log']
    }
    
  def menu(self):
    print('Crafting options: ')
    for index, recipe in enumerate(self.recipes):
      ingredients = ', '.join(self.recipes[recipe])
      print(f"{index + 1}. {recipe}: {ingredients}")
    
    input('x to close ')

  
  def craft(self, item):
    # check if got ingredients in inventory

    print('Crafted ' + item + '!')
    self.player.add_to_inventory(item)