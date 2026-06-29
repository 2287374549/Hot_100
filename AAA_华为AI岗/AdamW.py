import numpy as np

# ACM 输入
n = int(input())                # 先输入有多少行，每一行都是样本（x1，x2，y）—— y 是 y_true
X = np.zeros((n,2))             # 注意是 (n,2)，n 行指的是有 n 行输入
Y = np.zeros(n)
for i in range(n):
    parts = input().split()     # parts 就是一行一行读 n 的意思
    X[i, 0], X[i, 1], Y[i] = float(parts[0]), float(parts[1]), float(parts[2])

# 参数初始化
theta = np.zeros(3)             # 要更新的是 w1，w2，b，初始化为 w1=w2=b=0
m = np.zeros(3)                 # 一阶动量为 m_w1 = m_W2 = m_b = 0
v = np.zeros(3)                 # 二阶动量
beta1 = 0.9
beta2 = 0.999
lam = 0.01                      # 权重衰减系数
alpha = 0.001                   # 学习率
eps = 1e-8                      # 数值稳定性常熟

# AdamW 更新流程 ------------------------
for t_idx in range(n):
    x_aug = np.array(X[t_idx, 0], X[t_idx, 1], 1.0)
    y_pred = theta @ x_aug              # y_pred = w1*x1 + w2*x2 + b*1 —— 这里直接向量相乘，b 因为要乘以 1 所以采用 x_aug 加上一个 1

    # 先梯度的计算 —— Loss = (y_pred - y_true)**2 —— 更新参数为 w1，w2，b，则梯度就是用 Loss 对三者分别求导
    err = y_pred - Y[t_idx]
    g = 2 * err * x_aug                 # dL/dw1 = 2*(y_p - y_t)*(dy_p/dw1) = 2*err*X_w1，这里就是 x1=dy_p/dw1, x2同理，1 则是 dy/db

    # 再根据梯度更新其他参数
    m = beta1 * m + (1 - beta1) * g
    v = beta2 * v + (1 - beta2) * g**2
    t = t_idx                           # t 为迭代次数，t_idx 从 0 开始，t 从 1 开始
    m_hat = m / (1 - beta1**t)
    v_hat = v / (1 - beta2**t)

    theta = theta - alpha*(m_hat / (np.sqrt(v_hat)+eps) + lam * theta)


# 输出为六位小数且为银行家舍入
# from decimal import Decimal, ROUND_HALF_EVEN
# def fmt(x):
#     # return format( Decimal(str(x)).quantize(Decimal("0.000001")), rounding = ROUND_HALF_EVEN, 'f')
# print(f"{fmt(theta[0])} {fmt(theta[1])} {fmt(theta[2])}", end = '')

