import numpy as np
import gymnasium as gym
import time
import random

# Tải bảng Q đã huấn luyện
q_table = np.load("q_table.npy")

# Tạo môi trường với render_mode='human'
env = gym.make("FrozenLake-v1", map_name="4x4", is_slippery=False, render_mode="human")

# Số episode để hiển thị
num_test_episodes = 30
max_steps = 100

for episode in range(num_test_episodes):
    state = env.reset()[0]
    print(f"Episode {episode + 1}")
    time.sleep(1)

    for step in range(max_steps):
        # Lấy danh sách các hành động tốt nhất
        max_q = np.max(q_table[state])
        best_actions = [a for a, q in enumerate(q_table[state]) if q == max_q]
        action = random.choice(best_actions)

        next_state, reward, done, truncated, info = env.step(action)
        state = next_state

        if done:
            if reward == 1:
                print("✅ Thắng rồi!")
            else:
                print("💥 Rơi xuống hố.")
            break

env.close()

