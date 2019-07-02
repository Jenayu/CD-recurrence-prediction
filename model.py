import numpy as np
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression

# train and test model (SVC balanced) on the same data set 
# using leave-one-out cross validation
def train_model_svc_cv(data, selected_kernel, selected_features):
    
    predicted_labels = []
    test_labels = []
    accuracy_list = []
    dec_func = []
    
    # leave-one-out cross validation
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
        dec_func.append(round(float(classifier.decision_function(X)), 2))
    
    # concatenate the patient (the test case in each run of cross validation), 
    # its decision function, predicted label, and actual label
    df = pd.DataFrame(list(zip(data.index, dec_func, predicted_labels, test_labels)), columns =['Patient ID','Decision value', 'Predicted label', 'True label'])
    
    # return accuracy
    accuracy = np.count_nonzero(accuracy_list)/len(accuracy_list)
    print("accuracy:", accuracy)
    return(df)
    
 
# train and test model (SVC balanced) on two different set
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
    dec_func = np.around(classifier.decision_function(test_features), 2)
    
    # concatenate the decision function, predicted label, and actual label
    # of the patients in the test set
    df = pd.DataFrame(list(zip(dec_func, predicted_labels, test_labels)), columns =['Decision value', 'Predicted label', 'True label'])
    
    # return accuracy
    print("accuracy:", accuracy)
    return(df)






