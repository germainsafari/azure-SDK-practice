
from sklearn import svm
import joblib
import numpy as np 

#customer ages

x_train = np.array([50, 17,35, 25,46,47,33,42,92])
x_train = x_train.reshape(-1,1)

y_train = ["yes", "no", "no","yes","yes","yes","yes","yes", "no"]

clf = svm.SVC(gamma=0.001, C=100)
clf.fit(x_train, y_train)
print(clf)
joblib.dump(value=clf, filename="churn.pkl")