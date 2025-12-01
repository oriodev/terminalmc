class Gather:
  def __init__(self, player, title, text, item):
    self.player = player
    self.title = title
    self.text = text
    self.item = item
  
  def get(self):
    print(self.text)
    self.player.add_to_inventory(self.item)
