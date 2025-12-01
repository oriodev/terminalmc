class Environment:
  def __init__(self, name, text, actions):
    self.name = name
    self.text = text
    self.actions = actions
  
  def explore(self):
    print(self.text)
    print('Actions: ')
    for index, action in enumerate(self.actions):
      print(str(index + 1) + '. ' + action.title)
  
  def do_something(self, choice):
    if (not choice.isdigit()):
      return;

    # check the choice is within the right bound
    num_of_choices = len(self.actions)
    choices = list(range(1, num_of_choices + 1))

    # pick choice and call it
    if (int(choice) in choices):
      self.actions[int(choice) - 1].get()
