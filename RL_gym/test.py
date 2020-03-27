
import gym

env = gym.make("Taxi-v3").env

# env.render()

# env.reset() # Reset the environment

# env.render ()

# print("Action Space:", env.action_space)

# print("State pace:", env.observation_space)

# state = env.encode(4,2,2,1) # (taxi row, taxi column, passenger index, destination index)

# print("State:", state)

# env.s = state
# env.render()

env.s = 449
env.render()

for i,n in env.P[449].items():
    print(i,n)

# {action: [(probability, nextstate, reward, done)]}

# action --> south, north, east, west, pickup, dropoff










