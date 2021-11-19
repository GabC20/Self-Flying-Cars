import rlgym
from time import time

env = rlgym.make()

"""
    obs_space: [ball.position,
                ball.linear_velocity,
                ball.angular_velocity,
                player_car.position,
                player_car.linear_velocity,
                player_car.angular_velocity,
                player.boost_amount,
                player.has_flip,
                player.on_ground,
                car_data.position,
                car_data.linear_velocity,
                car_data.angular_velocity
    ]
"""

obs_space_high = [1.7808, 2.2260, 0.8886,
                  2.6086, 2.6086, 2.6086,
                  1.9098, 1.9098, 1.9098,
                  1.7808, 2.2260, 0.8886,
                  2.6086, 2.6086, 2.6086,
                  1.7507, 1.7507, 1.7507,
                  1.0, 1.0, 1.0,
                  1.7808, 2.2260, 0.8886,
                  2.6086, 2.6086, 2.6086,
                  1.7507, 1.7507, 1.7507]

obs_space_low = [-1.7808, -2.2260, 0.0,
                  -2.6086, -2.6086, -2.6086,
                  -1.9098, -1.9098, -1.9098,
                  -1.7808, -2.2260, 0.0,
                  -2.6086, -2.6086, -2.6086,
                  -1.7507, -1.7507, -1.7507,
                  0.0, 0.0, 0.0,
                  -1.7808, -2.2260, 0.0,
                  -2.6086, -2.6086, -2.6086,
                  -1.7507, -1.7507, -1.7507]







while True:
    obs = env.reset()
    done = False
    start_time = time()
    while not done:
      #Here we sample a random action. If you have an agent, you would get an action from it here.
      action = env.action_space.sample() 
      print(f'obs: {obs[18]}')
    #   print(f'action: {action}')
      
      next_obs, reward, done, gameinfo = env.step(action)
      
      obs = next_obs
    end_time = time()
    print(f'Duration: {end_time - start_time}')
    break
env.close()
      