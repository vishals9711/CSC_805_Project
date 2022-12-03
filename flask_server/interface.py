import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib
import time
import io
from sklearn.model_selection import train_test_split
import xgboost as xgb
from sklearn.metrics import f1_score,confusion_matrix
from sklearn.metrics import accuracy_score

# Load the data
plt.style.use('seaborn')
matplotlib.pyplot.switch_backend('Agg') 


class BreastCancerInterface:
    data_with_dropped_cols = None
    y_axis = None
    def __init__(self):
        data = pd.read_csv('data.csv')
        y = data.diagnosis
        data.head()
        drop_cols = ['Unnamed: 32','id','diagnosis']
        self.data_with_dropped_cols = data.drop(drop_cols,axis = 1 )
        self.data_with_dropped_cols.head()
        # dc = ['perimeter_mean','radius_mean','compactness_mean',
        #       'concave points_mean','radius_se','perimeter_se',
        #       'radius_worst','perimeter_worst','compactness_worst',
        #       'concave points_worst','compactness_se','concave points_se',
        #       'texture_worst','area_worst']
        # df = self.data_with_dropped_cols.drop(dc, axis=1)
        # df.head()
        # self.y_axis = data.diagnosis
        # x_train, x_test, y_train, y_test = train_test_split(df, y, test_size=0.3, random_state = 42)
        # print(x_test)
        # print(y_test)

        # clf1 = xgb.XGBClassifier(random_state = 42)
        # self.clf1 = clf1.fit(x_train, y_train)
    
    def returnIndexofHeader(self,headers):
        returnArr = []
        for header in headers:
            returnArr.append(self.data_with_dropped_cols.columns.get_loc(header))
        return returnArr

    def get_violion_plot(self,headers):
        df = self.data_with_dropped_cols
        graph_data = self.data_with_dropped_cols[df.columns[df.columns.isin(headers)]]
        data = pd.concat([self.y_axis,graph_data],axis=1)
        data = pd.melt(data,id_vars="diagnosis",
                            var_name="features",
                            value_name='value')
        ax = plt.figure(figsize=(8,8))
        sns.violinplot(x="features", y="value", hue="diagnosis", data=data,split=True, inner="quart")
        plt.xticks(rotation=45)
        bytes_image = io.BytesIO()
        plt.savefig(bytes_image, format='png')
        bytes_image.seek(0)
        return bytes_image

    def get_box_plot(self,headers):
        df = self.data_with_dropped_cols
        graph_data = self.data_with_dropped_cols[df.columns[df.columns.isin(headers)]]
        data = pd.concat([self.y_axis,graph_data],axis=1)
        data = pd.melt(data,id_vars="diagnosis",
                            var_name="features",
                            value_name='value')
        ax = plt.figure(figsize=(10,10))
        sns.boxplot(x="features", y="value", hue="diagnosis", data=data)
        plt.xticks(rotation=45)
        bytes_image = io.BytesIO()
        plt.savefig(bytes_image, format='png')
        bytes_image.seek(0)
        return bytes_image
    
    ## Need to Fix this
    def get_joint_plot(self,headers):
        df = self.data_with_dropped_cols
        graph_data = self.data_with_dropped_cols[df.columns[df.columns.isin(headers)]]
        # data = pd.concat([self.y_axis,graph_data],axis=1)
        # data = pd.melt(data,id_vars="diagnosis",var_name="features",value_name='value')
        ax = plt.figure(figsize=(10,10))
        # Get first 5 headers
        print(headers[5:])
        sns.jointplot(data = graph_data,x=headers[:5],y=headers[5:])
        plt.xticks(rotation=45)
        bytes_image = io.BytesIO()
        plt.savefig(bytes_image, format='png') 
        bytes_image.seek(0)
        return bytes_image
    
    ## Need to Fix this
    def get_swarm_plot(self,headers):
        df = self.data_with_dropped_cols
        graph_data = self.data_with_dropped_cols[df.columns[df.columns.isin(headers)]]
        data = pd.concat([self.y_axis,graph_data],axis=1)
        data = pd.melt(data,id_vars="diagnosis",
                            var_name="features",
                            value_name='value')
        ax = plt.figure(figsize=(12,12))
        sns.stripplot(x="features", y="value", hue="diagnosis", data=data,s = 1)
        plt.xticks(rotation=45)
        bytes_image = io.BytesIO()
        plt.savefig(bytes_image, format='png')
        bytes_image.seek(0)
        return bytes_image

    def get_heat_map_plot(self,headers):
        df = self.data_with_dropped_cols
        graph_data = self.data_with_dropped_cols[df.columns[df.columns.isin(headers)]]
        data = pd.concat([self.y_axis,graph_data],axis=1)
        data = pd.melt(data,id_vars="diagnosis",
                            var_name="features",
                            value_name='value')
        f,ax = plt.subplots(figsize=(18, 18))
        sns.heatmap(graph_data.corr(), annot=True, linewidths=.5, fmt= '.1f',ax=ax)
        plt.xticks(rotation=45)
        bytes_image = io.BytesIO()
        plt.savefig(bytes_image, format='png')
        bytes_image.seek(0)
        return bytes_image

    def get_prediction(data):
        # accuracy_score(data, clf1.predict(x_test))
        return 'M'