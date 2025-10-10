import numpy as np
import gymnasium as gym
import matplotlib.pyplot as plt

# Initialize environment
env = gym.make("Taxi-v3")

# Initialize Q-table with size [num_state x num_action]
q_table = np.zeros((env.observation_space.n, env.action_space.n))

# Hyperparameters
alpha = 0.5      # learning rate (cân bằng giữa kinh nghiệm cũ và mới)
gamma = 0.99        # discount factor (cân bằng giữa mục tiêu ngắn hạn và dài hạn)
epsilon = 1.0       # exploration rate (khám phá)
epsilon_decay = 0.99     # Khám phá chuyển dần sang khai thác
epsilon_min = 0.01
num_episodes = 10000
total_reward = 0
rewards = []  # lưu tổng reward mỗi episode

# Train
for episode in range(num_episodes):
    state, info = env.reset()
    terminated = False
    truncated = False
    total_reward = 0

    while not (truncated or terminated):
        # Epsilon-greedy strategy
        if np.random.rand() < epsilon:
            action = env.action_space.sample()
        else:
            action = np.argmax(q_table[state])

        next_state, reward, terminated, truncated, info = env.step(action)
        total_reward += reward

        # Q-learning update
        q_table[state, action] += alpha * (reward + gamma * np.max(q_table[next_state]) - q_table[state, action])
        state = next_state

        # Break when terminated
        if terminated:
            print(f'Episode: {episode}')
            print("OK")

    # Reduce epsilon to explore more
    if epsilon > epsilon_min:
        epsilon *= epsilon_decay

    rewards.append(total_reward)

# Trung bình trượt (ví dụ lấy trung bình 20 episode gần nhất)
window_size = 20
moving_avg = np.convolve(rewards, np.ones(window_size)/window_size, mode='valid')

# Vẽ biểu đồ
plt.figure(figsize=(12,6))
plt.plot(rewards, label='Reward mỗi episode', alpha=0.4)
plt.plot(moving_avg, label=f'Trung bình trượt ({window_size} episodes)', color='red')
plt.xlabel('Episode')
plt.ylabel('Reward')
plt.title('Biến động Reward theo Episode')
plt.legend()
plt.grid(True)
plt.show()

# Lưu bảng Q
np.save("q_table.npy", q_table)
