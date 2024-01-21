import matplotlib.pyplot as plot
import matplotlib.cm as cm

from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score



data = make_blobs(n_samples=1000, n_features=2, centers=4, cluster_std=1.0, random_state=101)


real_assigments = data[1]
data = data[0]



data_x = data[:, 0]
data_y = data[:, 1]


figure3, axe3 = plot.subplots()

axe3.scatter(data_x, data_y)
axe3.set_title('cloud of points')

plot.draw()



sse = []
sil_score = []

for k in range(2, 10):

    kmeans = KMeans(n_clusters=k)
    cluster = kmeans.fit_predict(data)

    s = silhouette_score(data, cluster)

    sse.append(kmeans.inertia_)
    sil_score.append(s)

print(sse)
print(sil_score)

figure, axe = plot.subplots()

axe.plot(range(2, 10), sse)
axe.set_title('SSE')

plot.draw()

figure2, axe2 = plot.subplots()

axe2.plot(range(2, 10), sil_score)
axe2.set_title('Silhouette score')

plot.draw()

plot.show()
