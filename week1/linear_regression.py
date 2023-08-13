import torch
import matplotlib.pypolt as plt
torch.manual_seed(10)

lr = 0.05

# 创建训练数据
x = torch.randn(20, 1) * 10     # x data (tensor) , shape = (20, 1)
# torch.randn(20, 1)    # 用于添加噪声
y = 2*x + (5 + torch.randn(20, 1))      # y data (tensor) , shape = (20, 1)

# 构建线性回归参数
w = torch.randn((1), requires_grad=True)
b = torch.zeros((1), requires_grad=True)

# 迭代训练1000次
for iteration in range(1000):

    # 前向传播，计算预测值
    wx = torch.mul(w, x)
    y_pred = torch.add(wx, b)

    # 计算MSE loss
    loss = (0.5 * (y - y_pred) ** 2).mean()

    # 反向传播
    loss.backward()


