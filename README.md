<h1 align="center">🤖 RL_Q_Learning</h1>

Dự án này triển khai **thuật toán Q-Learning** trong **Reinforcement Learning (Học tăng cường)** để huấn luyện agent trong hai môi trường cổ điển của **Gymnasium**:

- 🚕 **Taxi-v3**
- ❄️ **FrozenLake-v1**

---

## 📘 Giới thiệu

**Reinforcement Learning (RL)** là lĩnh vực trong Trí tuệ nhân tạo nơi một agent học cách hành động thông qua việc thử – sai để tối đa hóa phần thưởng nhận được.  
Trong dự án này, mình áp dụng **thuật toán Q-Learning**, một phương pháp *off-policy* giúp agent học giá trị hành động tối ưu thông qua **Bảng Q (Q-table)**.

---

## 🧠 Demo

| Taxi-v3               | FrozenLake-v1           |
|||
---
## 🎮 Môi trường sử dụng

### 🚕 Taxi-v3
- **Mô tả:**  
  Một chiếc taxi di chuyển trên lưới 5×5, nhiệm vụ là **đón và thả hành khách** đúng vị trí.  
  Mỗi hành động đúng được thưởng điểm dương, mỗi bước sai hoặc đón/thả sai sẽ bị trừ điểm.  
- **Mục tiêu:** học cách hoàn thành nhiệm vụ trong **ít bước nhất** và đạt **phần thưởng cao nhất**.
- **Loại môi trường:** *Discrete (rời rạc)*

---

### ❄️ FrozenLake-v1
- **Mô tả:**  
  Một tấm bản đồ băng tuyết 4×4, agent phải **di chuyển từ điểm Start (S)** đến **đích Goal (G)** mà không rơi xuống **hố Hole (H)**.  
  Ô trơn (F) khiến agent trượt theo hướng đi dự kiến, làm tăng tính ngẫu nhiên trong việc học.
- **Mục tiêu:** tìm được **đường đi an toàn nhất** đến đích với phần thưởng tối đa.
- **Loại môi trường:** *Discrete (rời rạc)*

---

## 📂 Cấu trúc thư mục

