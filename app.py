import streamlit as st
import pandas as pd
import joblib
import numpy as np
import sklearn


# load model
with open("model/winequality_pred_model.joblib", 'rb') as model:
    tree_model = joblib.load(model)

cols = ['alcohol', 
		'sulphates', 
		'total sulfur dioxide', 
		'volatile acidity', 
		'pH', 
		'density',
		'fixed acidity',
		'citric acid',
		'residual sugar',
		'chlorides',
		'free sulfur dioxide']


st.title('Wine Quality Predictor')

with st.form(key='my_form'):
	feat1 = st.text_input(label='Alcohol')
	feat2 = st.text_input(label='Sulphates')
	feat3 = st.text_input(label='Total sulfur dioxide')
	feat4 = st.text_input(label='Volatile acidity')
	feat5 = st.text_input(label='pH')
	feat6 = st.text_input(label='Density')
	submit_button = st.form_submit_button(label='Predict')

if submit_button:

	important_features = [feat1, feat2, feat3, feat4, feat5, feat6]
	wine_features = important_features + [0] * 5 # 5 trivial features
	X_new = pd.DataFrame(np.array(wine_features).reshape(-1,1).T, columns=cols)
	prediction = tree_model.predict(X_new).tolist()[0] # make prediction on user input
	pred_label = 'BAD' if prediction == 0 else 'GOOD' 

	st.write(f'Quality: {pred_label}')

