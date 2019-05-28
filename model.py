#!/usr/bin/env python
# coding: utf-8

# In[2]:


from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression


# In[3]:


def train_model_svc(train_data, test_data, selected_features):

    train_features = train_data[selected_features]
    train_labels = [1 if x=="recurrence" else 0 for x in train_data['Recurrence']] 

    classifier = SVC(kernel='linear', class_weight='balanced', probability=True).fit(train_features, train_labels)

    test_features = test_data[selected_features]
    test_labels = [1 if x=="recurrence" else 0 for x in test_data['Recurrence']] 

    predicted_labels = classifier.predict(test_features)

    true_count = 0
    for indx in range(len(predicted_labels)):
        if predicted_labels[indx] == test_labels[indx]:
            true_count+=1
    accuracy = true_count / len(predicted_labels)
    
    print(predicted_labels, test_labels)
    print("accuracy =", accuracy)


# In[4]:


def train_model_logistic(train_data, test_data, selected_features):

    train_features = train_data[selected_features]
    train_labels = [1 if x=="recurrence" else 0 for x in train_data['Recurrence']] 

    classifier = LogisticRegression(random_state=0, solver='liblinear').fit(train_features, train_labels)

    test_features = test_data[selected_features]
    test_labels = [1 if x=="recurrence" else 0 for x in test_data['Recurrence']] 

    predicted_labels = classifier.predict(test_features)

    true_count = 0
    for indx in range(len(predicted_labels)):
        if predicted_labels[indx] == test_labels[indx]:
            true_count+=1
    accuracy = true_count / len(predicted_labels)
    
    print(predicted_labels, test_labels)
    print("accuracy =", accuracy)


# In[1]:


get_ipython().system('ipython nbconvert featureSelection.ipynb --to script')


# In[ ]:




