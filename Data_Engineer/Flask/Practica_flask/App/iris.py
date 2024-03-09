# Crear un modelo de ML KNN con los datos de Iris sin gridsearch

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, classification_report
import pickle
import os

os.chdir(os.path.dirname(__file__))

iris = load_iris()

dic_target = {i: name for i, name in enumerate(iris['target_names'])}

# X = iris.data
# y = iris.target


# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=42)

# KNN = KNeighborsClassifier()

# KNN.fit(X_train, y_train)

# y_train_pred = KNN.predict(X_train)

# y_test_pred = KNN.predict(X_test)

# print(classification_report(y_train, y_train_pred)) 97%
# print('---'*200)
# print(classification_report(y_test, y_test_pred)) 100%


# with open('model.pkl', 'wb') as f:
#     pickle.dump(KNN, f)

# INFERENCIA

model = pickle.load(open('model.pkl', 'rb'))

muestra = [4,8,5,3]

print(dic_target[model.predict([muestra])[0]])