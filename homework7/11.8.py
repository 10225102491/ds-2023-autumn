import numpy as np
from sklearn.datasets import load_iris
iris = load_iris()
x = iris.data
y = iris.target
classes = np.unique(y)
centers = {}
for c in classes:
    t = x[y == c]
    center_c = np.mean(t,axis=0)
    centers[c] = center_c
for i in classes:
    print(f"类别 {i}的中心: {centers[i]}")
print("数据点到中心点的欧式距离:")
distances = [np.linalg.norm(i - center) for center in centers for i in x]  # 计算欧式距离
print(distances)




