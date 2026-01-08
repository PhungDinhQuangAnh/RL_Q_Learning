<h1 align="center">RL_Q_Learning</h1>

Dự án này triển khai **thuật toán Q-Learning** trong **Reinforcement Learning (Học tăng cường)** để huấn luyện agent trong hai môi trường cổ điển của **Gymnasium**:

- 🚕 **Taxi-v3**
- ❄️ **FrozenLake-v1**

---

## Giới thiệu

- **Reinforcement Learning (RL)** là lĩnh vực trong Trí tuệ nhân tạo nơi một agent học cách hành động thông qua việc thử – sai để tối đa hóa phần thưởng nhận được.  
- Trong dự án này, mình áp dụng **thuật toán Q-Learning**, một phương pháp *off-policy* giúp agent học giá trị hành động tối ưu thông qua **Bảng Q (Q-table)**.

---

## Demo

<h3 align="center">🚕 Taxi-v3</h3>
<img src="https://github.com/PhungDinhQuangAnh/RL_Q_Learning/blob/main/Demo/Taxi-v3.gif"> 

<h3 align="center">❄️ FrozenLake-v1</h3>
<img src="https://github.com/PhungDinhQuangAnh/RL_Q_Learning/blob/main/Demo/FrozenLake-v1.gif">

---

## Cấu trúc dự án
<pre>
RL_Q_Learning/
│
├── README.md                     # Tài liệu mô tả dự án
├── LICENSE                       # Giấy phép sử dụng
│
├── Demo/                         # Thư mục chứa video minh họa
│   ├── Taxi-v3.gif               # Video demo agent tự chơi game Taxi
│   └── FrozenLake-v1.gif         # Video demo agent tự chơi game FrozenLake
│
├── Taxi_v3/                      # Môi trường Taxi-v3
│   ├── taxi_train.py             # Huấn luyện agent
│   ├── taxi_test.py              # Đánh giá hiệu quả agent sau huấn luyện
│   ├── taxi_game.py              # Mô phỏng trò chơi
│   └── q_table.npy               # Bảng Q đã lưu
│
└── FrozenLake_v1/                # Môi trường FrozenLake-v1
    ├── frozenlake_train.py       # Huấn luyện agent 
    ├── frozenlake_test.py        # Đánh giá hiệu quả agent sau huấn luyện
    ├── frozenlake_game.py        # Mô phỏng trò chơi
    └── q_table.npy               # Bảng Q đã lưu
</pre>

---
