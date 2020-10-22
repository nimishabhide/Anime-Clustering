import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
X = pd.read_csv('dataanime.csv')
list_drop = ['anime_id','name']
X.drop(list_drop, axis=1, inplace=True)
X.dropna(inplace= True)
X['genre']=X['genre'].apply(lambda x:x.strip())
X['type']=X['type'].apply(lambda x:x.strip())
from sklearn.preprocessing import LabelEncoder
le=LabelEncoder()
X['genre']=le.fit_transform(X['genre'])
X['type']=le.fit_transform(X['type'])
from sklearn.cluster import KMeans
wcss = []
for i in range(1, 11):
    kmeans = KMeans(n_clusters = i, init = 'k-means++', random_state = 42)
    kmeans.fit(X)
    wcss.append(kmeans.inertia_)
plt.plot(range(1, 11), wcss)
plt.title('The Elbow Method')
plt.xlabel('Number of clusters')
plt.ylabel('WCSS')
plt.show()
kmeans = KMeans(n_clusters = 4, init = 'k-means++', random_state = 42)
y_kmeans = le.inverse_transform(kmeans.fit_predict(X))
print(y_kmeans)
