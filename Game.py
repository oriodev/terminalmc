class Game:
  def __init__(self, player, crafting, environments):
    self.player = player
    self.crafting = crafting
    self.environments = environments
    self.currentEnvironment = self.environments[0]

  def start(self):
    print('##############################')
    print('WELCOME TO TERMINAL MINECRAFT')
    print('##############################')

    print('i to access inventory')
    print('c to access crafting')
    
    self.loop()

  def loop(self):
    while True:
      print('##############')
      self.currentEnvironment.explore()
      choice = input('>>> ')

      self.currentEnvironment.do_something(choice)

      if (choice == 'i'):
        self.player.check_inventory()
      
      if (choice == 'c'):
        self.crafting.menu()

      if (choice == 'q'):
        print('Gameover')
        quit()
