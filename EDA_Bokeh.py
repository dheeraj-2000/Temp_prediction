#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy as np
import pandas as pd
import pandas_bokeh
pandas_bokeh.output_notebook()
pd.set_option('plotting.backend', 'pandas_bokeh')
# Create Bokeh-Table with DataFrame:
from bokeh.models.widgets import DataTable, TableColumn
from bokeh.models import ColumnDataSource


# In[5]:


df = pd.read_csv('/home/dheeraj/my_projects/my_project_env/practice/EDA_and_prediction/dataset_tk.csv')
df_long = pd.read_csv('/home/dheeraj/my_projects/my_project_env/practice/EDA_and_prediction/long_data_.csv')


# In[6]:


df


# In[7]:


df["Date"]=df["Unnamed: 0"]
df['Date'] = pd.to_datetime(df.Date, dayfirst=True)
df = df.drop(["Unnamed: 0"], axis = 1)


# In[10]:


df.info()


# In[12]:


df['NR'] = df['Punjab']+ df['Haryana']+ df['Rajasthan']+ df['Delhi']+df['UP']+df['Uttarakhand']+df['HP']+df['J&K']+df['Chandigarh']
df['WR'] = df['Chhattisgarh']+df['Gujarat']+df['MP']+df['Maharashtra']+df['Goa']+df['DNH']
df['SR'] = df['Andhra Pradesh']+df['Telangana']+df['Karnataka']+df['Kerala']+df['Tamil Nadu']+df['Pondy']
df['ER'] = df['Bihar']+df['Jharkhand']+ df['Odisha']+df['West Bengal']+df['Sikkim']
df['NER'] =df['Arunachal Pradesh']+df['Assam']+df['Manipur']+df['Meghalaya']+df['Mizoram']+df['Nagaland']+df['Tripura']


# In[13]:


df_line = pd.DataFrame({"Northern Region": df["NR"].values,
                        "Southern Region": df["SR"].values,
                        "Eastern Region": df["ER"].values,
                        "Western Region": df["WR"].values,
                        "North Eastern Region": df["NER"].values},index=df.Date)


# In[14]:


df_line


# In[29]:


df_line.plot_bokeh(kind="line",title ="India - Power Consumption Regionwise",
                   figsize =(12,12),
                   xlabel = "Date",
                   ylabel="MU(millions of units)")
                   


# In[27]:


df_line.plot_bokeh(kind="bar",title ="India - Power Consumption Regionwise",figsize =(1000,800),xlabel = "Date",ylabel="MU(millions of units)")


# In[ ]:





# In[ ]:




