#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd

# import the dataset

bacteria_all = pd.read_csv("~/UNC_WashU_CD_NI_ileum_all_level.csv")
bacteria_all = bacteria_all.set_index('SampleID').drop(columns = ['Disease', 'Tissue', 'Region', 'Pathology', 'Subtype',
                                                                  'Location', 'Behavior', 'SmokingStatus', 'X5_ASA', 'Steroids', 
                                                                  'Immunomodulators', 'TNF'])

bacteria_unc = bacteria_all[bacteria_all['Cohort'] == 'UNC']
bacteria_unc =  bacteria_unc.drop(bacteria_unc[bacteria_unc.Recurrence == ' '].index)

bacteria_washu = bacteria_all[bacteria_all['Cohort'] == 'WashU']
bacteria_washu =  bacteria_washu.drop(bacteria_washu[bacteria_washu.Recurrence == ' '].index)


# In[ ]:


get_ipython().system('ipython nbconvert featureSelection.ipynb --to script')

