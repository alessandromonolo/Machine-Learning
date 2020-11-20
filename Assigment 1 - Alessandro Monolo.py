#!/usr/bin/env python
# coding: utf-8

# ### Assigment 1 - Alessandro Monolo

# In[301]:


# Import commands for data cleaning and data visualization:

# Data cleaning:
import pandas as pd
# Data visualization - Method N°1:
import seaborn as sns
# Data visualization - Method N°2:
import matplotlib.pyplot as plt
# Code to improve matplotlib.pyplot:
get_ipython().run_line_magic('matplotlib', 'inline')


# ### Import Data Sets:

# In[302]:


# Import data sets (comma separated):

# Data Set N°1:
df_steps = pd.read_csv("steps.csv", sep=";")
# Data Set N°2:
df_survey = pd.read_csv('survey.csv')


# ### Reading Data. First we need to see what the data looks like (variables) by using .head()

# In[303]:


df_steps.head()


# In[304]:


df_survey.head()


# ### Show a quantitative variable: Weight
# 
# Here I show the weight distribution as quantitative variable:

# In[305]:


# Let's create a histogram which shows the weight distribution over the partecipants:

# kde = With False I am not showing any overlying density on my histogram.
sns.distplot(df_survey["weight"], kde=False)
# Title of the histogram.
plt.title("Weight distribution of participants")
# Name of X Axes.
plt.xlabel("Weight")
# Name of Y axes.
plt.ylabel("Count")
# Code to show my histogram.
plt.show()


# In[306]:


# Let's create a density plot which shows the weight proportion over the partecipants:

# kde=True - Showing the density overlying on my diagram 
# hist=False - Not showing the histogram diagram
sns.distplot(df_survey["weight"], hist=False, kde=True)
plt.title("Weight density distribution of participants")
plt.xlabel("Weight")
plt.ylabel("Proportion")
plt.show()


# ### Getting Uncleaned statistics:

# In[307]:


#statistical calculations: mean, median, mode, and variance

print("median: " + str(float(df_survey[["weight"]].median())))
print("mode: " + str(df_survey[["weight"]].mode()["weight"][0]))
print("mean: " + str(float(df_survey[["weight"]].mean())))
print("variance: " + str(float(df_survey[["weight"]].var())))


# In[308]:


# From these data visualizations we can see we have data outliers which compromise our data sets.
# Thus, we will perform data pre processing.


# ### Data Pre Processing 1

# In[309]:


# I create here functions which neutralize values under 20.0 (kg):

def under_20(x):
    if(x < 21.0): 
        return float('NaN')
    else: 
        return x


# In[310]:


# I create here functions which neutralize values above 200.0 (kg):

def above_200(x):
    if(x > 200.0): 
        return float('NaN')
    else: 
        return x


# In[311]:


# Here I apply the above two functions on my df_survey to the weight colomn:

df_survey["weight"]=df_survey["weight"].apply(above_200)
df_survey["weight"]=df_survey["weight"].apply(under_20)


# ### Visualization Cleaned Data 1

# In[312]:


# After data pre processing I can see the previous outliers have been neutralized:

sns.boxplot(x=df_survey["weight"])


# In[313]:


# Double check is always better than one:

# Diagram visualization proportion
fig, ax = plt.subplots(figsize=(16,8))
# Axis X and Axis Y values:
ax.scatter(df_survey['weight'], df_survey['height'])
# Title Axis Y:
ax.set_ylabel('Height per Participant')
# Title Axis X:
ax.set_xlabel('Weight per Participant')
plt.show()


# ### Data Pre Processing 2

# In[314]:


def above_12500(x):
    if(x > 8000.0): 
        return float('NaN')
    else: 
        return x


# In[315]:


def under_1000(x):
    if(x < 1000): 
        return float('NaN')
    else: 
        return x


# In[316]:


# Substitute Na values with "0" and apply the previou functions to my df_steps data set:

df_steps = df_steps.fillna(0)
df_steps["daily_mean_steps"]=df_steps.mean(axis=1)
df_steps["daily_mean_steps"]=df_steps["daily_mean_steps"].apply(int)
df_steps["daily_mean_steps"]=df_steps["daily_mean_steps"].apply(above_12500)
df_steps["daily_mean_steps"]=df_steps["daily_mean_steps"].apply(under_1000)
df_steps


# ## Time Series on Daily Mean Steps

# In[317]:


# We are visualizzing all the time series:
# .loc - to get the data time line: 
mean_steps = df_steps.loc[:,"20-6-2013":"13-5-2014"].mean()
mean_steps.index


# In[318]:


plt.figure(figsize=(25, 6))
plot = sns.lineplot(x=mean_steps.index, y=mean_steps)
for x, label in enumerate(plot.get_xticklabels()):
    if x % 20 == 0:  # every 10th label is kept
        label.set_visible(True)
    else:
        label.set_visible(False)

plt.title("Mean steps per date over all participants") 
plt.xlabel("Date") #set the x-label
plt.ylabel("Mean steps") #set the y-label
plt.show()


# ### Merge cleaned Data Sets:

# In[319]:


# Merge the two Data Sets into one by "id" Value:

df = df_survey.merge(df_steps, on = "id")
df.head()


# ### Getting new and cleaned statistics conclusions:

# In[321]:


#statistical calculations: mean, median, mode, and variance

print("median: " + str(float(df[["weight"]].median())))
print("mode: " + str(df[["weight"]].mode()["weight"][0]))
print("mean: " + str(float(df[["weight"]].mean())))
print("variance: " + str(float(df[["weight"]].var())))


# ###  What can we conclude from this?
# 
# * The weight distribution over the partecipiants is modal. It has only one pick point.
# * The center of the distribution is around 71.0 and 72.0.
# * There is no right or left skew. The distribution is reasonably symmetrical.

# In[ ]:




