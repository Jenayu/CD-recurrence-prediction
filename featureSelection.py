#!/usr/bin/env python
# coding: utf-8

# In[29]:


from sklearn.feature_selection import chi2
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import RFE
from sklearn.svm import SVR


# In[30]:


# feature selection (kbest)

def featureSel_kbest(train_data, num_features):
    
    train_data_nonconst = train_data.loc[:, (train_data!= train_data.iloc[0]).any()] 
    
    train_features = train_data_nonconst.drop(columns=['Patient','Recurrence'],axis=1)
    train_feature_names = train_features.columns
    train_labels = [1 if x=="recurrence" else 0 for x in train_data['Recurrence']] 

    bestfeatures = SelectKBest(score_func=chi2, k=num_features)
    selector = bestfeatures.fit(train_features, train_labels)

    selected_feature_names_kbest = train_feature_names[selector.get_support()]

    return list(selected_feature_names_kbest)


# In[31]:


# feature selection (rfe)

def featureSel_rfe(train_data, num_features):
    
    train_data_nonconst = train_data.loc[:, (train_data!= train_data.iloc[0]).any()] 

    estimator = SVR(kernel="linear")
    selector = RFE(estimator, num_features, step=1)

    train_features = train_data_nonconst.drop(columns=['Patient','Recurrence'],axis=1)
    train_feature_names = train_features.columns
    train_labels = [1 if x=="recurrence" else 0 for x in train_data['Recurrence']] 
    
    feat_selector = selector.fit(train_features, train_labels)

    selected_feature_names_rfe = train_feature_names[selector.support_]
    
    return list(selected_feature_names_rfe)


# In[32]:


# feature selection (rfecv)

def featureSel_rfecv(train_data, num_folds):
    
    train_data_nonconst = train_data.loc[:, (train_data!= train_data.iloc[0]).any()] 

    estimator = SVR(kernel="linear")
    selector = RFECV(estimator, step=1, cv=num_folds)

    train_features = train_data_nonconst.drop(columns=['Patient','Recurrence'],axis=1)
    train_feature_names = train_features.columns
    train_labels = [1 if x=="recurrence" else 0 for x in train_data['Recurrence']] 
    
    feat_selector = selector.fit(train_features, train_labels)

    selected_feature_names_rfecv = train_feature_names[selector.support_]
    
    return list(selected_feature_names_rfecv)


# In[1]:


get_ipython().system('ipython nbconvert featureSelection.ipynb --to script')


# In[ ]:




