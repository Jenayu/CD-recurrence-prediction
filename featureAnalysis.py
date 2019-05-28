#!/usr/bin/env python
# coding: utf-8

# In[6]:


import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np 
import pandas as pd
from sklearn.decomposition import PCA


# In[2]:


def PCAanalysis_2D(train_data, outcome):
    
    train_data_nonconst = train_data.loc[:, (train_data!= train_data.iloc[0]).any()]    
    train_features = train_data_nonconst.drop(columns=['Patient','Recurrence'],axis=1)
    train_feature_names = train_features.columns
    
    pca = PCA().fit(train_features)
    plt.figure()
    plt.plot(np.cumsum(pca.explained_variance_ratio_))
    plt.xlabel('Number of Components')
    plt.ylabel('Variance (%)') #for each component
    plt.title('Number of components vs. Explained Variance')
    plt.show()
    
    pca = PCA(n_components=2)
    principalComponents = pca.fit_transform(train_features)
    principalDf = pd.DataFrame(data = principalComponents, columns = ['principal component 1', 'principal component 2'])
    finalDf = pd.concat([principalDf, train_data[[outcome]]], axis = 1)
    
    fig = plt.figure(figsize = (5,5))
    ax = fig.add_subplot(1,1,1) 
    ax.set_xlabel('Principal Component 1', fontsize = 15)
    ax.set_ylabel('Principal Component 2', fontsize = 15)
    ax.set_title('2 component PCA', fontsize = 20)
    targets = set(train_data[outcome])
    colors_list = ['r', 'g','b']
    colors = colors_list[:len(targets)]
    for target, color in zip(targets,colors):
        indicesToKeep = finalDf[outcome] == target
        ax.scatter(finalDf.loc[indicesToKeep, 'principal component 1'], finalDf.loc[indicesToKeep, 'principal component 2'], c = color, s = 50)
    ax.legend(targets)
    ax.grid()
    
    print('Explained variance by component:', pca.explained_variance_ratio_)


# In[10]:


def PCAanalysis_3D(train_data, outcome):
    
    train_data_nonconst = train_data.loc[:, (train_data!= train_data.iloc[0]).any()]    
    train_features = train_data_nonconst.drop(columns=['Patient','Recurrence'],axis=1)
    train_feature_names = train_features.columns
    train_labels = train_data_nonconst['Recurrence']
    
    pca = PCA(n_components=3)
    principalComponents = pca.fit_transform(train_features)
    
    fig = plt.figure(1, figsize=(5, 4))
    plt.clf()
    ax = Axes3D(fig, rect=[0, 0, .95, 1], elev=48, azim=134)
    
    #for name in ['recurrence', 'no recurrence']:
        #ax.text3D(principalComponents[train_labels == name, 0].mean(), 
                  #principalComponents[train_labels == name, 1].mean(), 
                  #principalComponents[train_labels == name, 2].mean(), 
                  #name,  horizontalalignment='center',
            #bbox=dict(alpha=.5, edgecolor='w', facecolor='w'))
        
    new_y = [1 if y == 'recurrence' else 0 for y in train_labels]
    new_y = np.choose(new_y, [0, 1]).astype(np.float)
    ax.scatter(principalComponents[:, 0], principalComponents[:, 1], principalComponents[:, 2], c=new_y, cmap=plt.cm.nipy_spectral, edgecolor='k')

    ax.w_xaxis.set_ticklabels([])
    ax.w_yaxis.set_ticklabels([])
    ax.w_zaxis.set_ticklabels([])

    print('Explained variance by component:', pca.explained_variance_ratio_)


# In[5]:


def PCAanalysis(train_data, outcome, num_pc):
    
    train_data_nonconst = train_data.loc[:, (train_data!= train_data.iloc[0]).any()]    
    train_features = train_data_nonconst.drop(columns=['Patient','Recurrence'],axis=1)
    train_feature_names = train_features.columns
    
    pca = PCA(n_components=num_pc)
    principalComponents = pca.fit_transform(train_features)

    scores = pca.score_samples(train_features)
    
    print('Sample scores:', scores)
    print('Explained variance by component:', pca.explained_variance_ratio_)


# In[11]:


get_ipython().system('ipython nbconvert featureSelection.ipynb --to script')


# In[ ]:




