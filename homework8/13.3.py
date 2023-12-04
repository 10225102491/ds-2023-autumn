from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

# 加载Iris数据集
iris = load_iris()
X = iris.data
y = iris.target

# 划分训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# 创建KNN分类器实例（这里选择K=3）
knn = KNeighborsClassifier(n_neighbors=3)

# 使用训练数据拟合模型
knn.fit(X_train, y_train)

# 对训练集进行预测并计算准确度
y_train_pred = knn.predict(X_train)
train_accuracy = accuracy_score(y_train, y_train_pred)
print("训练集准确度:", train_accuracy)

# 对测试集进行预测并计算准确度
y_test_pred = knn.predict(X_test)
test_accuracy = accuracy_score(y_test, y_test_pred)
print("测试集准确度:", test_accuracy)