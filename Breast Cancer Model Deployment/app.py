# -*- coding: utf-8 -*-
"""
Created on Sun May 17 22:08:07 2020

@author: PiyushSin
"""
import numpy as np
import pandas as pd
from flask import Flask, request, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('breast_cancer_model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    input_values = [float(x) for x in request.form.values()]
    value = [np.array(input_values)]
    
    features_name = ['mean radius', 'mean texture', 'mean perimeter', 'mean area',
       'mean smoothness', 'mean compactness', 'mean concavity',
       'mean concave points', 'mean symmetry', 'mean fractal dimension',
       'radius error', 'texture error', 'perimeter error', 'area error',
       'smoothness error', 'compactness error', 'concavity error',
       'concave points error', 'symmetry error', 'fractal dimension error',
       'worst radius', 'worst texture', 'worst perimeter', 'worst area',
       'worst smoothness', 'worst compactness', 'worst concavity',
       'worst concave points', 'worst symmetry', 'worst fractal dimension']
    
    df = pd.DataFrame(value, columns=features_name)
    output = model.predict(df)
        
    if output == 0:
        res_val = "Breast cancer"
    else:
        res_val = "No Breast cancer"
        
    return render_template('index.html', prediction= res_val)

if __name__ == "__main__":
    app.run()
