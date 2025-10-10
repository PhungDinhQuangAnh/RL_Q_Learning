import gymnasium as gym
import pygame

# Tạo môi trường Taxi
env = gym.make("Taxi-v3", render_mode="human")
state, info = env.reset()

pygame.init()
pygame.display.set_caption("Taxi-v3 Game")

# Ánh xạ phím sang hành động
KEY_TO_ACTION = {
    pygame.K_s: 0,  # South
    pygame.K_w: 1,  # North
    pygame.K_d: 2,  # East
    pygame.K_a: 3,  # West
    pygame.K_e: 4,  # Pickup
    pygame.K_q: 5   # Dropoff
}
print("=== HƯỚNG DẪN ===")
print("W: Lên | S: Xuống | A: Trái | D: Phải")
print("E: Đón khách | Q: Trả khách")

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
                    print("🚕 Hành trình hoàn tất! Reset lại game.")
                    state, info = env.reset()

env.close()
pygame.quit()