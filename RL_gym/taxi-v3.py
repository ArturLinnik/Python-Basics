
import random
import numpy
import os
from time import sleep
import gym

env = gym.make("Taxi-v3").env

env.s = 449
env.render()

for i,n in env.P[449].items():
    print(i,n)

### Training the agent ###

q_table = numpy.zeros([env.observation_space.n, env.action_space.n]) # .n represents the size 

# Hyperparameters

alpha = 0.1
gamma = 0.6
epsilon = 0.1

# For plotting metrics

all_timesteps = []
all_penalties = []

def clear():
    os.system('clear')

for i in range(1,100001):
    state = env.reset()

    timesteps, penalties, reward = 0, 0, 0
    done = False

    while not done:
        if random.uniform(0,1) < epsilon:
            action = env.action_space.sample() # Explore action space
        else:
            action = numpy.argmax(q_table[state]) # Exploit learned values

        next_state, reward, done, info = env.step(action)

        old_value = q_table[state, action]
        next_max = numpy.max(q_table[next_state])

        new_value = (1 - alpha) * old_value + alpha * (reward + gamma * next_max)
        q_table[state, action] = new_value

        if reward == -10:
            penalties += 1

        state = next_state
        timesteps += 1

    if i % 100 == 0:
        clear()
        print("Episode:", i)

print("Training finished. \n")

print(q_table[449])




















