import gym
from gym import error, spaces, utils
from gym.utils import seeding

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


  """
  metadata = {'render.modes': ['human']}

  def __init__(self):
    pass
  def step(self, action):
    pass
  def reset(self):
    pass
  def render(self, mode='human'):
    # consider using openai classic control rendering script?
    # https://github.com/openai/gym/blob/master/gym/envs/classic_control/rendering.py
    print("hey")
  def close(self):
    pass