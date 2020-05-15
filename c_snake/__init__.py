from gym.envs.registration import register

register(
    id='c_snake-v0',
    entry_point='c_snake.envs:SnakeEnv',
)
register(
    id='c_snake-extrahard-v0',
    entry_point='c_snake.envs:SnakeExtraHardEnv',
)