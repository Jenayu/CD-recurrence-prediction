#!/usr/bin/env python
# coding: utf-8


import numpy as np
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression


def train_model_svc_cv(data, selected_kernel, selected_features):
    
    predicted_labels = []
    test_labels = []
    accuracy_list = []
    
    for i in data.index.values:
        
        test_data = data.loc[i]
        train_data = data.drop(index=i)

        train_features = train_data[selected_features]
        train_labels = [1 if x=="recurrence" else 0 for x in train_data['Recurrence']] 

        test_features = test_data[selected_features]
        if test_data['Recurrence'] == 'recurrence':
            test_label = 1
        else:
            test_label = 0
            
        classifier = SVC(kernel=selected_kernel, class_weight='balanced', probability=True).fit(train_features, train_labels)

        X = list()
        X.append(test_features)
        X = np.array(X)
        y = classifier.predict(X)
        
        predicted_labels.append(int(y))
        test_labels.append(test_label)
        accuracy_list.append(bool(y==test_label))
    
    accuracy = np.count_nonzero(accuracy_list)/len(accuracy_list)
    print(predicted_labels, test_labels)
    print("accuracy:", accuracy)
    
    
 def train_model_logistic_cv(data, selected_features):

    predicted_labels = []
    test_labels = []
    accuracy_list = []
    
    for i in data.index.values:
        
        test_data = data.loc[i]
        train_data = data.drop(index=i)
        
        train_features = train_data[selected_features]
        train_labels = [1 if x=="recurrence" else 0 for x in train_data['Recurrence']] 

        test_features = test_data[selected_features]
        if test_data['Recurrence'] == 'recurrence':
            test_label = 1
        else:
            test_label = 0

        classifier = LogisticRegression(random_state=0, solver='liblinear').fit(train_features, train_labels)
        
        X = list()
        X.append(test_features)
        X = np.array(X)
        y = classifier.predict(X)
        
        predicted_labels.append(int(y))
        test_labels.append(test_label)
        accuracy_list.append(bool(y==test_label))
    
    accuracy = np.count_nonzero(accuracy_list)/len(accuracy_list)
    print(predicted_labels, test_labels)
    print("accuracy:", accuracy)
    
    
def train_model_svc(train_data, test_data, selected_kernel, selected_features):
    
    train_features = train_data[selected_features]
    train_labels = [1 if x=="recurrence" else 0 for x in train_data['Recurrence']] 
    
    test_features = test_data[selected_features]
    test_labels = [1 if x=="recurrence" else 0 for x in test_data['Recurrence']] 
        
    classifier = SVC(kernel=selected_kernel, class_weight='balanced', probability=True).fit(train_features, train_labels)

    predicted_labels = classifier.predict(test_features)

    true_count = 0
    for indx in range(len(predicted_labels)):
        if predicted_labels[indx] == test_labels[indx]:
            true_count+=1
    accuracy = true_count / len(predicted_labels)
    
    print(predicted_labels, test_labels)
    print("accuracy =", accuracy)


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





