
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
plt.style.use('seaborn')
import time

# Load the data
data = pd.read_csv('data.csv')


# ### Separate Target from Features

# In[3]:


data.head()


# In[4]:


col = data.columns      
print(col)


# In[5]:


y = data.diagnosis                           
drop_cols = ['Unnamed: 32','id','diagnosis']
x = data.drop(drop_cols,axis = 1 )
x.head()


# ### Plot Diagnosis Distributions

# In[41]:


ax = sns.countplot(y,label="Count")
B, M = y.value_counts()
print('Number of Benign: ',B)
print('Number of Malignant : ',M)


# In[42]:


x.describe()


# ### Visualizing Standardized Data with Seaborn

# In[43]:


data_dia = y
data = x
data_n_2 = (data - data.mean()) / (data.std())              
data = pd.concat([y,data_n_2.iloc[:,0:10]],axis=1)
data = pd.melt(data,id_vars="diagnosis",var_name="features",value_name='value')
plt.figure(figsize=(10,10))
sns.violinplot(x="features", y="value", hue="diagnosis", data=data,split=True, inner="quart")
plt.xticks(rotation=45)


# ### Violin Plots and Box Plots

# In[9]:


data = pd.concat([y,data_n_2.iloc[:,10:20]],axis=1)
data = pd.melt(data,id_vars="diagnosis",
                    var_name="features",
                    value_name='value')
plt.figure(figsize=(10,10))
sns.violinplot(x="features", y="value", hue="diagnosis", data=data,split=True, inner="quart")
plt.xticks(rotation=45)


# In[10]:


data = pd.concat([y,data_n_2.iloc[:,20:31]],axis=1)
data = pd.melt(data,id_vars="diagnosis",
                    var_name="features",
                    value_name='value')
plt.figure(figsize=(10,10))
sns.violinplot(x="features", y="value", hue="diagnosis", data=data,split=True, inner="quart")
plt.xticks(rotation=45)


# In[11]:


plt.figure(figsize=(10,10))
sns.boxplot(x="features", y="value", hue="diagnosis", data=data)
plt.xticks(rotation=45)


# ### Using Joint Plots for Feature Comparison

# In[46]:


sns.jointplot(x.loc[:,'concavity_worst'],
              x.loc[:,'concave points_worst'],
              kind="reg",
              color="#ce1414")


# ###  Observing the Distribution of Values and their Variance with Swarm Plots

# In[52]:


#sns.set(style="whitegrid", palette="muted")
data_dia = y
data = x
data_n_2 = (data - data.mean()) / (data.std())  
data = pd.concat([y,data_n_2.iloc[:,0:10]],axis=1)
data = pd.melt(data,id_vars="diagnosis",
                    var_name="features",
                    value_name='value')
plt.figure(figsize=(12,14))
sns.swarmplot(x="features", y="value", hue="diagnosis", data=data)
plt.xticks(rotation=45)


# In[53]:


data = pd.concat([y,data_n_2.iloc[:,10:20]],axis=1)
data = pd.melt(data,id_vars="diagnosis",
                    var_name="features",
                    value_name='value')
plt.figure(figsize=(10,10))
sns.swarmplot(x="features", y="value", hue="diagnosis", data=data)
plt.xticks(rotation=45)


# In[84]:


data = pd.concat([y,data_n_2.iloc[:,20:31]],axis=1)
data = pd.melt(data,id_vars="diagnosis",
                    var_name="features",
                    value_name='value')
plt.figure(figsize=(12,14))
sns.swarmplot(x="features", y="value", hue="diagnosis", data=data)
plt.xticks(rotation=45)


# ### Observing all Pair-wise Correlations

# In[55]:


#correlation map
f,ax = plt.subplots(figsize=(18, 18))
sns.heatmap(x.corr(), annot=True, linewidths=.5, fmt= '.1f',ax=ax)


# ### Task 2: Dropping Correlated Columns from Feature Matrix
# ***
# Note: If you are starting the notebook from this task, you can run cells from all the previous tasks in the kernel by going to the top menu and Kernel > Restart and Run All\n",
# ***

# In[56]:


dc = ['perimeter_mean','radius_mean','compactness_mean',
              'concave points_mean','radius_se','perimeter_se',
              'radius_worst','perimeter_worst','compactness_worst',
              'concave points_worst','compactness_se','concave points_se',
              'texture_worst','area_worst']

df = x.drop(dc, axis=1)
df.head()


# In[57]:


f, ax = plt.subplots(figsize=(14,14))
sns.heatmap(df.corr(), annot=True, linewidth=0.5, ax=ax)


# ### Task 3: Classification using XGBoost (minimal feature selection)

# In[58]:


from sklearn.model_selection import train_test_split
import xgboost as xgb
from sklearn.metrics import f1_score,confusion_matrix
from sklearn.metrics import accuracy_score


# In[59]:


y_testBinary = y.replace(to_replace = dict(B = 0, M = 1))

x_train, x_test, y_train, y_test = train_test_split(df, y_testBinary, test_size=0.3, random_state = 42)

clf1 = xgb.XGBClassifier(random_state = 42)
clf1 = clf1.fit(x_train, y_train)


# In[60]:


print('Accuracy:', accuracy_score(y_test, clf1.predict(x_test)))
cm = confusion_matrix(y_test, clf1.predict(x_test))
sns.heatmap(cm, annot=True, fmt = 'd')


# ### Task 4: Univariate Feature Selection and XGBoost

# In[61]:


from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2


# In[62]:


selected = SelectKBest(chi2, k=10).fit(x_train, y_train)

print('Score List:', selected.scores_)
print('Feature List', x_train.columns)


# In[63]:


x_train2 = selected.transform(x_train)
x_test2 = selected.transform(x_test)

clf2 = xgb.XGBClassifier().fit(x_train2, y_train)

print('Accuracy:', accuracy_score(y_test, clf2.predict(x_test2)))
cm2 = confusion_matrix(y_test, clf2.predict(x_test2))
sns.heatmap(cm2, annot=True, fmt='d')


# ### Task 5: Recursive Feature Elimination with Cross-Validation

# In[64]:


from sklearn.feature_selection import RFECV

clf3 = xgb.XGBClassifier()
rfecv = RFECV(estimator = clf3, step=1, cv=5, scoring = 'accuracy', n_jobs=-1).fit(x_train, y_train)

print('Optimal No. of Features:', rfecv.n_features_)
print('Best Features:', x_train.columns[rfecv.support_])


# In[65]:


print('Accuracy:', accuracy_score(y_test, rfecv.predict(x_test)))


# In[78]:


numFeatures = [i for i in range(1, len(rfecv.cv_results_['mean_test_score']) + 1)]
cvScores = rfecv.cv_results_['mean_test_score']

ax = sns.lineplot(x=numFeatures, y=cvScores)
ax.set(xlabel = 'No. of Selected Features', ylabel='CV Scores')


# In[77]:


numFeatures = [i for i in range(1, len(rfecv.cv_results_['std_test_score']) + 1)]
cvScores = rfecv.cv_results_['std_test_score']

ax = sns.lineplot(x=numFeatures, y=cvScores)
ax.set(xlabel = 'No. of Selected Features', ylabel='CV Scores')


# ### Task 6: Feature Extraction using Principal Component Analysis

# In[79]:


x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=42)

x_train_norm = (x_train - x_train.mean())/(x_train.max()-x_train.min())
x_test_norm = (x_train - x_test.mean())/(x_test.max()-x_test.min())


# In[80]:


from sklearn.decomposition import PCA

pca = PCA()
pca.fit(x_train_norm)

plt.figure(1, figsize=(10,8))
sns.lineplot(data = np.cumsum(pca.explained_variance_ratio_))
plt.xlabel('No. of components')
plt.ylabel('Cum XVariance')


# In[ ]:



