import gym
import numpy as np
from stable_baselines3 import SAC
from stable_baselines3.common.vec_env import DummyVecEnv
from stable_baselines3.common.evaluation import evaluate_policy
from rl_environment import AluminumElectrolysisEnv

def train_model(env, timesteps=50000):
    model = SAC("MlpPolicy", env, verbose=1)
    model.learn(total_timesteps=timesteps)
    model.save("sac_aluminum")

def evaluate_model(env, model, num_episodes=100):
    mean_reward, std_reward = evaluate_policy(model, env, n_eval_episodes=num_episodes)
    print(f"Mean reward: {mean_reward} +/- {std_reward}")

def load_model(env):
    model = SAC.load("sac_aluminum", env=env)
    return model

def run_model(env, model):
    obs = env.reset()
    for _ in range(1000):
        action, _states = model.predict(obs)
        obs, reward, done, info = env.step(action)
        env.render()
        if done:
          obs = env.reset()

if __name__ == "__main__":
    env = DummyVecEnv([lambda: AluminumElectrolysisEnv()])

    # Train the model
    train_model(env)

    # Load the trained model
    model = load_model(env)

    # Evaluate the trained model
    evaluate_model(env, model)

    # Run the trained model
    run_model(env, model)
