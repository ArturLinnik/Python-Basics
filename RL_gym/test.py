
import gym

env = gym.make("Taxi-v3").env

env.render()

env.reset() # Reset the environment

env.render ()

print("Action Space:", env.action_space)

print("State pace:", env.observation_space)










