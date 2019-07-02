import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def plot_feature_recurrence(data, features):
    
    # keep the recurrence patients
    rec_data = data
    for idx in data.index:
        if data['Recurrence'].loc[idx] == 'no recurrence':
            rec_data = rec_data.drop(index=idx)
    
    df = rec_data[features]

    # set the positions and width for the bars
    pos = list(range(len(df))) 
    width = 0.15
    
    # plot the bars
    fig, ax = plt.subplots(figsize=(7.5,5))
    
    colors = ['#FF0000','#FF8000', '#FFFF00', '#80FF00', '#0080FF', '#00FF80']
    for idx in range(len(features)):
        plt.bar([p + width*idx for p in pos], df[features[idx]], width, alpha=0.5, color=colors[idx], label=df.index) 

    # set the axis
    ax.set_ylabel('Bacteria abundance')
    ax.set_title('Abundance of the selected features in patients (recurrence)')

    ax.set_xticks([p + len(features)/2*width for p in pos])
    ax.set_xticklabels(df_unc.index)
    
    plt.ylim([0, 1] )

    # add the legend and show the plot
    plt.legend(df, loc='upper left')
    plt.grid()
    plt.show()


def plot_feature_norecurrence(data, features):
    
    # keep the non-recurrence patients
    norec_data = data
    for idx in data.index:
        if data['Recurrence'].loc[idx] == 'recurrence':
            norec_data = norec_data.drop(index=idx)
    
    df = norec_data[features]

    # set the positions and width for the bars
    pos = list(range(len(df))) 
    width = 0.15
    
    # plot the bars
    fig, ax = plt.subplots(figsize=(15,5))
    
    colors = ['#FF0000','#FF8000', '#FFFF00', '#80FF00', '#0080FF', '#00FF80']
    for idx in range(len(features)):
        plt.bar([p + width*idx for p in pos], df[features[idx]], width, alpha=0.5, color=colors[idx], label=df.index) 


        
    # Set the y axis label
    ax.set_ylabel('Bacteria abundance')

    # Set the chart's title
    ax.set_title('Abundance of the selected features in patients (no recurrence)')

    # Set the position of the x ticks
    ax.set_xticks([p + len(features)/2*width for p in pos])

    # Set the labels for the x ticks
    ax.set_xticklabels(df_unc.index)
    
    # Set y limits
    plt.ylim([0, 1] )

    # Adding the legend and showing the plot
    plt.legend(df, loc='upper left')
    plt.grid()
    plt.show()


