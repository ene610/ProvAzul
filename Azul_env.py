import gym
import gym.spaces as spaces
import Game

class CustomEnv(gym.Env):
    def __init__(self):
        self.pygame = Game.Pygame2D()
        self.action_space = spaces.Discrete(180)

        rows_player_obs = [5] * 15
        penality_player_obs = [1] * 7
        board_player_obs = [1] * 25
        normal_pit_obs = [4] * 5 * 5
        #al massimo ci possono essere 3*5 tessere nel discard pit per una singola tessera
        discard_pit_obs = [3*5] * 5
        one_player_obs = rows_player_obs + penality_player_obs + board_player_obs + \
                         normal_pit_obs + discard_pit_obs

        self.observation_space = spaces.MultiDiscrete(one_player_obs)

    def reset(self):
        del self.pygame
        self.pygame = Game.Pygame2D()
        obs = self.pygame.observe()
        return obs

    def step(self, action):
        self.pygame.action(action)
        obs = self.pygame.observe()
        reward = self.pygame.evaluete()
        done = self.pygame.is_done()

        return obs,reward,done,{}

    def render(self, mode='human'):
        print(self.pygame.view())