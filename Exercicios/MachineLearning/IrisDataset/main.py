# [sempre] retorna um resultado diferente porque <- KNN é determinístico

from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn import metrics

# Carrega o iris dataset
iris = load_iris()
x = iris.data
y = iris.target

# Divide os dados em conjuntos de treinamento e testes
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.25)

performance_value = {}

# Enquanto k que vale 1 não chegar em 26 k repete
for k in range(1, 26):
    knn = KNeighborsClassifier(n_neighbors=k) # n_neighbours Número de neighbours a serem usados ​​por padrão para neighbor queries
    knn.fit(X_train, y_train)
    predictions = knn.predict(X_test)
    accuracy = metrics.accuracy_score(y_test, predictions)
    performance_value[k] = accuracy
    print(f"k={k}, accuracy={accuracy * 100:.2f}%")
