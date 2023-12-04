from sklearn import datasets
from sklearn.model_selection import train_test_split
iris = datasets.load_iris()
x,y= iris.data,iris.target
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2)