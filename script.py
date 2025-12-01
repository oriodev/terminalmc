from Game import Game
from Environment import Environment
from Gather import Gather
from Item import Item
from Player import Player
from Crafting import Crafting

# player
player = Player()

# crafting
crafting = Crafting(player)

# environments
plains = Environment(
  'Plains',
  'You are surrounded by grass, trees, and animals.',
  [
    Gather(player, 'Punch a tree', 'You punched a tree and got one log', Item('Log')),
  ]
)

game = Game(player, crafting, [plains])
game.start()
