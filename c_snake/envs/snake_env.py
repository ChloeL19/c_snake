import gym
from gym import error, spaces, utils
from gym.utils import seeding
from c_snake.envs.snake import Controller, Discrete

# import dependencies
try:
    import matplotlib.pyplot as plt
    import matplotlib
except ImportError as e:
    raise error.DependencyNotInstalled("{}. (HINT: see matplotlib documentation for installation https://matplotlib.org/faq/installing_faq.html#installation".format(e))

class SnakeEnv(gym.Env):
  """
  Description:
    The classic snake game.
    Food is randomly distributed throughout the screen. Actions are left, right, or forward.
    Snake moves a unit in previous direction if no action selected (so default action is 
    the previous action). Reward is +1 if snake eats unit of food. Snake also grows
    by one unit if snake eats unit of food. Reward is -1 (game over) if snake hits wall 
    or itself. 

    Observation:
      Type: ??
      Num     Observation       Description            Min       Max
              food_num          number of food pieces
              touching_food     bool, if touching food
              food_pos
              snake_length
              snake_hd_pos

    Actions:
      Type: Discrete(3)
      Num       Action
      0         Turn left
      1         Turn right
      2         Go forward

    Reward:
      Reward is +1 for every piece of food eaten

    Starting state:
      Food piece assigned random position
      Snake head assigned random position
      * both within the playing field


  # I ended up just mainly using this code: https://github.com/grantsrb/Gym-Snake/blob/master/gym_snake/envs/snake/grid.py


  """
  metadata = {'render.modes': ['human']}

  def __init__(self):
    # set board specs
    self.grid_size = [15, 15]
    self.unit_size = 10 # what does this mean?
    self.unit_gap = 1 # what does this mean?
    self.snake_size = 3
    self.n_snakes = 1 # restrict to single snake
    self.n_foods = 1
    self.viewer = None
    self.action_space = Discrete(4)
    self.random_init = True

  def step(self, action):
    self.last_obs, rewards, done, info = self.controller.step(action)
    return self.last_obs, rewards, done, info
    
  def reset(self):
    pass
  def render(self, mode='human'):
    # consider using openai classic control rendering script?
    # https://github.com/openai/gym/blob/master/gym/envs/classic_control/rendering.py
    print("hey")
  def close(self):
    pass