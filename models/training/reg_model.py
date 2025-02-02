import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
import os
import joblib
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import time
path=Path(r"/mnt/c/Users/ranad/Desktop/noline/data/Backpack-Prediction-Challenge")

data_pd=pd.read_csv(path/"train.csv")

data_pd=data_pd.rename(columns={'Weight Capacity (kg)':'Weight-Capacity'})
modified_columns=list(map(lambda x:x.replace(' ','-').lower(),data_pd.columns))
data_pd.columns=modified_columns

data_pd=data_pd.dropna(subset=['weight-capacity'])
og_categorical_columns=['brand','material','color','laptop-compartment','size','style','waterproof']
label_encode_cols=['laptop-compartment','waterproof','size']
one_hot_encode_cols=set(og_categorical_columns)-set(label_encode_cols)

data_pd=pd.get_dummies(data_pd, columns=list(og_categorical_columns), drop_first=True)

X=data_pd.drop(columns=['price'])
y=data_pd['price']


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = RandomForestRegressor(n_estimators=100, random_state=42)

t1=time.time()
model.fit(X_train, y_train)
t2=time.time()
print("time taken : ",t2-t1)

joblib.dump(model, "random_forest_v1.pkl")
