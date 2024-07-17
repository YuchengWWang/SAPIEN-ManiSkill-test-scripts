# Import required packages
import gymnasium as gym
import mani_skill.envs
import time
env = gym.make("PegInsertionSide-v1")
obs, _ = env.reset(seed=0)
env.unwrapped.print_sim_details() # print verbose details about the configuration
done = False
start_time = time.time()
while not done:
    obs, rew, terminated, truncated, info = env.step(env.action_space.sample())
    done = terminated or truncated
N = info["elapsed_steps"].item()
dt = time.time() - start_time
FPS = N / (dt)
print(f"Frames Per Second = {N} / {dt} = {FPS}")


from mani_skill.utils.wrappers.gymnasium import ManiSkillCPUGymWrapper
env = gym.make("PegInsertionSide-v1")
env = ManiSkillCPUGymWrapper(env)  #####
obs, _ = env.reset() # obs is numpy and unbatched
print(type(obs), obs.shape)


import matplotlib.pyplot as plt
env = gym.make("PegInsertionSide-v1", render_mode="sensors") # sensors打开传感器视角，rgb_array打开观察者相机视角，human打开交互界面
env.reset()
plt.imshow(env.render()[0].numpy())
plt.show()
