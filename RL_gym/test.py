
import os
# from IPython.display import clear_output ### IPython doesn't work for me
from time import sleep
import gym

env = gym.make("Taxi-v3").env

env.s = 449
env.render()

for i,n in env.P[449].items():
    print(i,n)

# {action: [(probability, nextstate, reward, done)]}

# action --> south, north, east, west, pickup, dropoff

epochs = 0
penalties, reward = 0,0

frames = [] # for animation

done = False

while not done:
    action = env.action_space.sample() # Randomly executes an action
    state, reward, done, info = env.step(action)

    if reward == -10:
        penalties += 1


    # Put each rendered frame into dict for animation

    frames.append(
        {
        'frame': env.render(mode='ansi'),
        'state': state,
        'action': action,
        'reward': reward
        }
    )

    epochs += 1

print("Timesteps taken", epochs)
print("Penalties taken", penalties)

def clear():
    os.system('clear')

def print_frames(frames):
    for i, frame in enumerate(frames):
        clear()
        # clear_output(wait=True) ### IPython doesn't work for me
        print(frame.get('frame'))
        print(f"Timestep: {i + 1}")
        print(f"State: {frame['state']}")
        print(f"Action: {frame['action']}")
        print(f"Reward: {frame['reward']}")
        sleep(.1)

print_frames(frames)










