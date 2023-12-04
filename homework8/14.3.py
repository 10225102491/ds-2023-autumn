from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.datasets import fetch_20newsgroups
newsgroups_data = fetch_20newsgroups(subset='train')
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(newsgroups_data.data)
print(tfidf_matrix[0].toarray())