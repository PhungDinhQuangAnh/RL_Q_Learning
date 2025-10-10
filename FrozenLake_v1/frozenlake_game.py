import gymnasium as gym
import pygame

# Tạo môi trường FrozenLake
env = gym.make("FrozenLake-v1", map_name="4x4", is_slippery=False, render_mode="human")
state, _ = env.reset()

# Khởi tạo pygame để bắt sự kiện phím
pygame.init()
pygame.display.set_caption("FrozenLake-v1 Game")

# Mappings từ phím sang hành động:
# 0: left, 1: down, 2: right, 3: up
key_action = {
    pygame.K_LEFT: 0,
    pygame.K_DOWN: 1,
    pygame.K_RIGHT: 2,
    pygame.K_UP: 3
}

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key in key_action:
                action = key_action[event.key]
                next_state, reward, terminated, truncated, _ = env.step(action)
                state = next_state
                if terminated or truncated:
                    if reward == 1:
                        print("✅ Chiến thắng!")
                    else:
                        print("💥 Thua rồi!")
                    state, _ = env.reset()
    # env.render() --> render_mode="human" tự hiển thị mỗi bước, không cần render thủ công

env.close()
pygame.quit()
