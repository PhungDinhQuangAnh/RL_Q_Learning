import numpy as np
import gymnasium as gym

# Tạo môi trường FrozenLake 4x4 (non-slippery để học hiệu quả hơn)
env = gym.make("FrozenLake-v1", map_name="4x4", is_slippery=False)

# Khởi tạo Q-table với kích thước [số trạng thái x số hành động]
q_table = np.zeros((env.observation_space.n, env.action_space.n))

# Hyperparameters
alpha = 0.8         # learning rate (Tốc độ học)
gamma = 0.95        # discount factor (Tầm nhìn)
epsilon = 1.0       # exploration rate (Khám phá)
epsilon_decay = 0.995      # Khám phá chuyển dần sang khai thác
epsilon_min = 0.01
num_episodes = 5000

# Huấn luyện
for episode in range(num_episodes):
    state = env.reset()[0]
    terminated = False
    truncated = False

    while not truncated:
        # Epsilon-greedy strategy
        if np.random.rand() < epsilon:
            action = env.action_space.sample()
        else:
            action = np.argmax(q_table[state])

        next_state, reward, terminated, truncated, info = env.step(action)

        # =====================
        # Cập nhật reward shaping
        if terminated:
            if reward == 1.0:
                reward = 1      # Goal
                print(f'Episode:{episode} Step:{i} --> OK')
            else:
                reward = -1     # Hole
        else:
            reward = -0.01      # Bước thường
        # =====================

        # Q-learning update
        q_table[state, action] += alpha * (reward + gamma * np.max(q_table[next_state]) - q_table[state, action])

        state = next_state

        if terminated:
            break

    # Giảm epsilon theo thời gian để khai thác nhiều hơn
    if epsilon > epsilon_min:
        epsilon *= epsilon_decay

# Hiển thị bảng Q
np.set_printoptions(precision=2, suppress=True)
print("Q-Table sau huấn luyện:")
print(q_table)

# Lưu bảng Q
np.save("q_table.npy", q_table)