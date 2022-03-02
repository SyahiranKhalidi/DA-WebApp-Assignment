#streamlit run DAFP.py

import streamlit as st
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error,mean_absolute_error,r2_score
import time

header = st.container()
dataset = st.container()
features = st.container()
modeTraining = st.container()

with header:
    st.title("Welcome to my webapp")
    st.text("Description Text")

with dataset:
    st.header("Dataset")
    st.text("Description Text")

    chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])
    st.line_chart(chart_data)

    map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])
    st.map(map_data)

    churn_data = pd.read_csv('churn.csv')
    df = pd.DataFrame(churn_data)
    df = df.dtypes
    st.write(churn_data)
    st.write(df.astype(str))

    st.subheader("Bar chart for states")
    state_count = pd.DataFrame(churn_data['st'].value_counts())
    st.bar_chart(state_count)

with features:
    st.sidebar.header("Features")
    st.text("Description Text")

    st.markdown('_details_') #stylized print : bold, italic, etc

    st.write('Before you continue, please read the [terms and conditions](https://www.gnu.org/licenses/gpl-3.0.en.html)')
    show = st.checkbox('I agree the terms and conditions')
    if show:
        st.write(pd.DataFrame({
        'Intplan': ['yes', 'yes', 'yes', 'no'],
        'Churn Status': [0, 0, 0, 1]
    }))

with modeTraining:
    st.header("modeTraining")
    st.text("Description Text")

    sel_col, disp_col = st.columns(2)
    slider_value = st.slider('Slider example', min_value = 10 , max_value = 100, value = 20, step = 10)
    select_value = st.selectbox('Choices for user', options = [1,2,3], index = 0) #dropdown menu, index is default value
    user_input = st.text_input('Please input text','ncsc')

    'Starting a long computation...'

    latest_iteration = st.empty()
    bar = st.progress(0)

    for i in range(100):
   
        latest_iteration.text(f'Iteration {i+1}')
        bar.progress(i + 1)
        time.sleep(0.1)

    '...and now we\'re done!'

'''
    regr = RandomForestRegressor(max_depth = slider_value, n_estimators = select_value)
    X = churn_data[[user_input]]
    #st.write(X.astype(float))

    y = churn_data[['label']]
    regr.fit(X,y)
    prediction = regr.predict(y)

    disp_col.subheader('Mean Absolute Error :')
    disp_col.write(mean_absolute_error(y,prediction))

    disp_col.subheader('Mean Squared Error:')
    disp_col.write(mean_squared_error(y,prediction))

    disp_col.subheader('R Squared Error:')
    disp_col.write(r2_score(y,prediction))
'''