import matplotlib.pyplot as plot
import matplotlib.cm as cm

from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

#This script serves as visualizing an K-means method implementation following multiple steps:

#   1- Generating a function that can plot our dataset
#   2- Generating/ Downloading our dataset (internet, or using make_blobs())
#   3- Applying the K-means algorithm on our dataset
#   4- Using both the Elbow and Silhouette criteria to find the optimal K- cluster number


data = make_blobs(n_samples=500, n_features=2, centers=7, cluster_std=1.5,random_state=101)

#extracting only the data and not the assigments
data_x = data[0][:, 0]
data_y = data[0][:, 1]



#   cluster_std -> 0 the pointss are clearly far from each other, -> 10, 100, ... points are closer to another
#   centers -> number of clusters we want to have



#  --------------- 3- Applying the K-means algorithm on our dataset  --------------- #

def Kmeans_algo(data, n):

    sse = [] #Sum of squarred errors
    sil_score = [] #Silhouette score
    i, j = 0, 1
    
    data_x = data[0][:, 0]
    data_y = data[0][:, 1]

    fig, axs = plot.subplots(2, 2, figsize = (16, 8))

    axs[0, 0].scatter(data_x, data_y, s = 6)

    axs[0, 0].set_ylabel('Data Y')
    axs[0, 0].set_title('Initial Data cloud')

    axs[0, 0].grid(linestyle = '--')
    plot.draw()


    for k in range(2, n):
        kmeans = KMeans(init = "k-means++", n_clusters = k, n_init =25, max_iter = 100, random_state=50)
        cluster_labels = kmeans.fit_predict(data[0]) #Assinging the points to each cluster

        #plotting the figure displaying the evolution of the number of cluters
        if k in [int(n/4), int(n/2), int(n-1)]:


            colors = cm.nipy_spectral(cluster_labels.astype(float) / (k+2)) #This is used to color our cloud
        

            
            axs[i, j].scatter(data_x, data_y, s = 6, c = colors )
            axs[i, j].set_ylabel('Data Y')
            axs[i, j].set_title('K-means clustering result with k = {}'.format(k))

            axs[i, j].grid(linestyle = '--')
            plot.draw()


            if i == 0 and j == 1:
                j = 0
                i = 1

            elif i == 1 and j == 0:
                j = 1
                i = 1
                       


        sse.append(kmeans.inertia_) #Summed squarred error
        sil_score.append(silhouette_score(data[0], cluster_labels, metric = "euclidean")) #Silhouette score

    
    return sse, sil_score

n = 20 #Max cluster number K we want to increment

sse, sil_score = Kmeans_algo(data, n)


#determining the elbow point
rate_array = []
for i in range(0, len(sse)-1):
    rate = (sse[i]-sse[i+1])/sse[i]
    rate_array.append(rate)

    if rate < 0.25:
        elbow_point = i
        break

print("The optimal value of K, using the Elbow criteria, with a tolerance of 25% is: {}".format(elbow_point+2))



#determining the optimal number k with Silhouette criteria

opt_k = sil_score.index(max(sil_score))
print("The optimal value of K, using the silhouette criteria is: {}".format(opt_k+2))




figure, axis = plot.subplots(2,2, figsize = (16, 8))



#rerunning the algorithm for the optimal K for both elbow and silhouette method with a display
kmeans = KMeans(init = "k-means++", n_clusters = elbow_point+2, n_init = 50, max_iter = 300, random_state=50)
cluster_labels = kmeans.fit_predict(data[0])



#Plotting the Sumed squarred error with the number of clusters
axis[0, 0].plot(range(2, n), sse)
axis[0, 0].plot(elbow_point+2, sse[elbow_point], "x", markersize = 7)

#Setting the labels on our figure

axis[0, 0].set_ylabel('Sum Squared Error')
axis[0, 0].set_title('Evolution  of the SSE with number K')
axis[0, 0].grid(linestyle = '--')
axis[0, 0].set_xticks(range(2, n))
plot.draw()



colors = cm.nipy_spectral(cluster_labels.astype(float) / (elbow_point+2))
axis[0, 1].scatter(data_x, data_y, s = 6, c = colors )

#Setting the labels on our figure

axis[0, 1].set_ylabel('Data y')
axis[0, 1].set_title('K-means Clustering with optimal K = {}- Elbow criteria'.format(elbow_point+2))
axis[0, 1].grid(linestyle = '--')
plot.draw()







# Rerunning the algorithm for the silhouette method
kmeans2 = KMeans(init = "k-means++", n_clusters = opt_k+2, n_init = 50, max_iter = 300, random_state=50)
cluster_labels1 = kmeans2.fit_predict(data[0])






axis[1, 0].plot(range(2, n), sil_score)
axis[1, 0].plot(opt_k+2, sil_score[opt_k], "x", markersize = 7)

#Setting the labels on our figure
axis[1, 0].set_xlabel('Number of Clusters')
axis[1, 0].set_ylabel('Silhouette score')
axis[1, 0].set_title('Evolution of the silhouette score with number K')
axis[1, 0].grid(linestyle = '--')
axis[1, 0].set_xticks(range(2, n))
plot.draw()




colors2 = cm.nipy_spectral(cluster_labels1.astype(float) / (opt_k+2))
#print(cluster_labels1.astype(float))

axis[1, 1].scatter(data_x, data_y, s = 6, c = colors2 )

#Setting the labels on our figure
axis[1, 1].set_xlabel('Data X')
axis[1, 1].set_ylabel('Data Y')
axis[1, 1].set_title('K-means Clustering with optimal K = {} - Silhouette criteria'.format(opt_k+2))
axis[1, 1].grid(linestyle = '--')
plot.draw()




plot.show()


####