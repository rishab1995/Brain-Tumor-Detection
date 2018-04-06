import numpy as np
import csv
#from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
from sklearn.externals import joblib
from sklearn import tree
#from sklearn import ensemble
#from sklearn.svm import SVC
from sklearn.model_selection import train_test_split

lines = csv.reader(open("features.csv", "r"))
#testdata = csv.reader(open("R:\data.csv", "r"))
dataset = list(lines)
#test_data = np.array(list(testdata)).astype(np.float)
data = np.array(dataset)
x = data[1:, 1:8]
x = x.astype(np.float)
y = data[1:,8]
y = y.astype(np.float)
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.33, random_state=45)

#clf = SVC()
#clf = GaussianNB()
#clf = ensemble.RandomForestClassifier()
clf = tree.DecisionTreeClassifier()

clf.fit(X_train, y_train) 
y_pred = clf.predict(X_test)
print(X_test)
print(y_pred)
print(accuracy_score(y_test, y_pred))
joblib.dump(clf, 'DTClassifier.pkl') 

