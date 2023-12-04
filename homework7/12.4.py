import torch
from torch import nn
from torch.utils.data import DataLoader, TensorDataset
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# 加载数据集
iris = datasets.load_iris()
X = iris.data
y = iris.target

# 数据预处理：分割训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=23)

# 数据标准化
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# 创建PyTorch数据集
train_data = TensorDataset(torch.FloatTensor(X_train), torch.LongTensor(y_train))
test_data = TensorDataset(torch.FloatTensor(X_test), torch.LongTensor(y_test))
train_loader = DataLoader(train_data, batch_size=16, shuffle=True)
test_loader = DataLoader(test_data, batch_size=16)


# 定义模型
class LogisticRegressionModel(nn.Module):
    def __init__(self, input_dim, output_dim):
        super(LogisticRegressionModel, self).__init__()
        self.linear = nn.Linear(input_dim, output_dim)

    def forward(self, x):
        out = self.linear(x)
        return out


input_dim = X_train.shape[1]
output_dim = 3  # 分类数
model = LogisticRegressionModel(input_dim, output_dim)

# 定义损失函数和优化器
criterion = nn.CrossEntropyLoss()
optimizer = torch.optim.SGD(model.parameters(), lr=0.01)

# 训练模型
num_epochs = 50
for epoch in range(num_epochs):
    for i, (inputs, labels) in enumerate(train_loader):
        model.train()  # 设定为训练模式
        optimizer.zero_grad()  # 清空梯度
        outputs = model(inputs)  # 前向传播计算输出值
        loss = criterion(outputs, labels)  # 计算损失值
        loss.backward()  # 反向传播计算梯度值
        optimizer.step()  # 更新权重参数值（只更新权重，偏置项在下次迭代更新）
    print("Epoch [{}/{}], Loss: {:.4f}".format(epoch + 1, num_epochs, loss.item()))  # 每轮输出损失值