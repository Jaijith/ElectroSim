import gym
from gym import spaces
import numpy as np
import simulate

class AluminumElectrolysisEnv(gym.Env):
    def __init__(self, time_step=1, alumina_interval=30, alumina_amount=3):
        super(AluminumElectrolysisEnv, self).__init__()

        self.time_step = time_step
        self.alumina_interval = alumina_interval
        self.alumina_amount = alumina_amount

        self.action_space = spaces.Box(low=0, high=1, shape=(5,), dtype=np.float32)
        self.observation_space = spaces.Box(low=-np.inf, high=np.inf, shape=(8,), dtype=np.float32)

        self.states = []
        self.actions = []
        self.desired_temperature_range = [935, 970]

    def step(self, action):
        t, x = simulate.simulate(self.time_step, action, self.alumina_interval, self.alumina_amount)
        self.states.append(x[-1, :])
        denormalized_action = simulate.denormalize_action(action)
        self.actions.append(denormalized_action)

        reward = self.calculate_reward(x[-1, :])
        done = self.is_done(x[-1, :])

        return x[-1, :], reward, done, {}

    def reset(self):
        self.states = []
        self.actions = []
        return np.zeros((8,))
    
    def render(self, mode='human'):
        # Render the environment to the screen (optional)
        print(f"State: {self.state}")
        print(f"Action: {self.actions}")

    def calculate_reward(self, state):
        temperature = state[5]
        if self.desired_temperature_range[0] <= temperature <= self.desired_temperature_range[1]:
            return 1.0
        else:
            return -1.0

    def is_done(self, state):
        if state[5] < 935 or state[5] > 970:
            return True
        else:
            return False
