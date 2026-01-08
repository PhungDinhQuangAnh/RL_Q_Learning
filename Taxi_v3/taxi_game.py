import gymnasium as gym
import pygame

# Tạo môi trường Taxi
env = gym.make("Taxi-v3", render_mode="human")
state, info = env.reset()

pygame.init()
pygame.display.set_caption("Taxi-v3 Game")

# Chuyển phím sang hành động
KEY_TO_ACTION = {
    pygame.K_s: 0,  # Xuống
    pygame.K_w: 1,  # Lên
    pygame.K_d: 2,  # Đông
    pygame.K_a: 3,  # Tây
    pygame.K_e: 4,  # Đón khách
    pygame.K_q: 5   # Trả khách
}
print("=== HƯỚNG DẪN ===")
print("w: Lên | s: Xuống | a: Trái | d: Phải")
print("e: Đón khách | q: Trả khách")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key in KEY_TO_ACTION:
                action = KEY_TO_ACTION[event.key]
                next_state, reward, terminated, truncated, info = env.step(action)
                state = next_state
                print(f"Action: {action}, Reward: {reward}")
                if terminated:
                    print("Hành trình hoàn tất! Reset lại game.")
                    state, info = env.reset()

env.close()
pygame.quit()
