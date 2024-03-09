from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
import pickle
import os

os.chdir(os.path.dirname(__file__))


iris = load_iris()
X = iris.data
y = iris.target

# Dividir los datos en conjunto de entrenamiento y conjunto de prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Dividir el conjunto de entrenamiento en conjunto de entrenamiento y conjunto de validación
X_train, X_val, y_train, y_val = train_test_split(X_train, y_train, test_size=0.25, random_state=42)  # 0.25 * 0.8 = 0.2

# Inicializar el clasificador KNeighbors
model = KNeighborsClassifier()

# Entrenar el modelo con el conjunto de entrenamiento
model.fit(X_train, y_train)

# Hacer predicciones en el conjunto de validación
y_pred_val = model.predict(X_val)

# Calcular la precisión en el conjunto de validación
accuracy_val = accuracy_score(y_val, y_pred_val)
print("Accuracy en datos de validación:", accuracy_val)

# Hacer predicciones en el conjunto de prueba
y_pred_test = model.predict(X_test)

# Calcular la precisión en el conjunto de prueba
accuracy_test = accuracy_score(y_test, y_pred_test)
print("Accuracy en datos de prueba:", accuracy_test)

with open('model.pkl', 'wb') as f:
    pickle.dump(model, f)