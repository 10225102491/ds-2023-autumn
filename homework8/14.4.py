from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.datasets import fetch_20newsgroups

# 加载数据集
newsgroups_data = fetch_20newsgroups(subset='train')

# 初始化TfidfVectorizer
vectorizer = TfidfVectorizer()

# 对文本数据进行向量化
X_train_vectorized = vectorizer.fit_transform(newsgroups_data.data)
X_test_vectorized = vectorizer.transform(newsgroups_data.data)

# 初始化MultinomialNB分类器
classifier = MultinomialNB()

# 训练分类器
classifier.fit(X_train_vectorized, newsgroups_data.target)

# 对测试集进行预测并计算分类准确度
y_pred = classifier.predict(X_test_vectorized)
accuracy = accuracy_score(newsgroups_data.target, y_pred)
print("Accuracy on test set:", accuracy)