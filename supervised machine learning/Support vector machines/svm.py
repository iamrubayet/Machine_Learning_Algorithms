from sklearn import svm
X = [[0, 0], [1, 1]]  ##training features
y = [0, 1] ##training labels

clf.fit(X, y)
clf.predict([[2., 2.]])
