from datetime import datetime
import pickle

import gym
from gym import spaces
from gym.wrappers import FlattenObservation, RecordVideo, RescaleAction, TimeLimit
import imageio
from IPython import display
import matplotlib.pyplot as plt
from moviepy.editor import VideoFileClip
import numpy as np
import pandas as pd
from stable_baselines3 import PPO, TD3
from stable_baselines3.common.env_util import unwrap_wrapper

from .ea_train import make_env, read_from_yaml
from .utils import NotVecNormalize


# ----- Notebook utilities ----------------------------------------------------

def evaluate_ares_ea_agent(run_name, n=200, include_position=False):
    loaded_model = PPO.load("utils/rl/ares_ea/models/ml_workshop/model")
    loaded_config = read_from_yaml("utils/rl/ares_ea/models/ml_workshop/config")

    env = make_env(loaded_config)
    env = NotVecNormalize(env, "utils/rl/ares_ea/models/ml_workshop/normalizer")

    maes = []
    for _ in range(n):
        done = False
        observation = env.reset()
        while not done:
            action, _ = loaded_model.predict(observation)
            observation, reward, done, info = env.step(action)
        maes.append(info["mae_all"] if include_position else info["mae_focus"])
    env.close()

    score = np.mean(maes)
    print(f"==> Achieved a score of {score} ({n} evaluations)")


def make_ares_ea_training_videos():
    recdir = "utils/rl/ares_ea/recordings/ml_workshop"
    imgdir = "img"

    for eval_episode in [0, 27, 343]:
        filename = f"rl-video-episode-{eval_episode}"
        clip = VideoFileClip(f"{recdir}/{filename}.mp4")
        clip.write_gif(f"{imgdir}/ares-ea-{filename}.gif", logger=None)


def make_lunar_lander_gif(model_path, gif_path):
    env = gym.make("LunarLander-v2")
    model = PPO.load(model_path)

    images = []
    obs = env.reset()
    img = env.render(mode="rgb_array")
    done = False
    while not done:
        images.append(img)
        action, _ = model.predict(obs)
        obs, _, done ,_ = env.step(action)
        img = env.render(mode="rgb_array")

    imageio.mimsave(f"{gif_path}.gif", [np.array(img) for i, img in enumerate(images) if i % 2 == 0], fps=29)
    env.close()

    
def make_lunar_lander_training_gifs():
    for steps in [1e5, 3e5, 1e6]:
        make_lunar_lander_gif(
            model_path=f"utils/rl/lunar_lander/checkpoints/rl_model_{int(steps)}_steps",
            gif_path=f"img/lunar_lander_trainig_{int(steps)}_steps",
        )


def plot_ares_ea_training_history(run_name):
    monitor = pd.read_csv(f"utils/rl/ares_ea/monitors/{run_name}/0.monitor.csv", index_col=False, skiprows=1)

    plt.figure(figsize=(13,4))
    plt.subplot(121)
    plt.title("Episode Rewards")
    plt.plot(monitor["t"]/60, monitor["r"])
    plt.xlabel("Wall time (min)")
    plt.ylabel("Reward")
    plt.grid()
    plt.subplot(122)
    plt.title("Episode Lengths")
    plt.plot(monitor["t"]/60, monitor["l"], c="tab:orange")
    plt.xlabel("Wall time (min)")
    plt.ylabel("Steps")
    plt.grid()
    plt.tight_layout()
    plt.show()


def plot_lunar_lander_training_history():
    monitor = pd.read_csv("utils/rl/lunar_lander/monitors/0.monitor.csv", index_col=False, skiprows=1)

    plt.figure(figsize=(13,4))
    plt.subplot(121)
    plt.title("Episode Rewards")
    plt.axhline(-100, color="tab:red", ls="--")
    plt.axhspan(-1000, -100, color="tab:red", alpha=0.2)
    plt.text(120/60, -700, "Crashing", color="tab:red")
    plt.axhline(140, color="tab:green", ls="--")
    plt.axhspan(140, 400, color="tab:green", alpha=0.2)
    plt.text(15/60, 250, "Landing", color="tab:green")
    plt.plot(monitor["t"]/60, monitor["r"])
    plt.ylim(-950, 350)
    plt.xlabel("Wall time (min)")
    plt.ylabel("Reward")
    plt.grid()
    plt.subplot(122)
    plt.title("Episode Lengths")
    plt.plot(monitor["t"]/60, monitor["l"], c="tab:orange")
    plt.xlabel("Wall time (min)")
    plt.ylabel("Steps")
    plt.grid()
    plt.tight_layout()
    plt.show()


def record_video(env):
    return RecordVideo(
        env,
        video_folder="utils/rl/lunar_lander_recordings",
        episode_trigger=lambda i: (i % 60) == 0
    )


def show_video(filename):
    return display.Video(filename)
    """Wrapper for recording epsiode data such as observations, rewards, infos and actions."""

    def __init__(self, env):
        super().__init__(env)
        
        self.has_previously_run = False

    def reset(self):
        if self.has_previously_run:
            self.previous_observations = self.observations
            self.previous_rewards = self.rewards
            self.previous_infos = self.infos
            self.previous_actions = self.actions
            self.previous_t_start = self.t_start
            self.previous_t_end = datetime.now()
            self.previous_steps_taken = self.steps_taken

        observation = self.env.reset()

        self.observations = [observation]
        self.rewards = []
        self.infos = []
        self.actions = []
        self.t_start = datetime.now()
        self.t_end = None
        self.steps_taken = 0

        self.has_previously_run = True

        return observation

    def step(self, action):
        observation, reward, done, info = self.env.step(action)

        self.observations.append(observation)
        self.rewards.append(reward)
        self.infos.append(info)
        self.actions.append(action)
        self.steps_taken += 1

        return observation, reward, done, info
