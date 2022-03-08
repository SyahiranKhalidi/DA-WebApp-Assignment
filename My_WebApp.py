import streamlit as st
import pandas as pd
pd.options.mode.chained_assignment = None
import numpy as np
import plotly.express as px

maindf = st.container()
categorydf = st.container()
numericaldf = st.container()

with maindf:
    st.title('Credit Card Users Analysis')
    
    sidetitle1, sidetitle2 = st.sidebar.columns([1, 4])
    sidetitle2.title("Welcome, visitors!!")
    st.sidebar.write("- This Webapp purposes is to explore and visualize the UCI_Credit_Card.csv dataset for easier analysis.")
    st.sidebar.markdown("- The dataset is divided according to our interest label, that is _whether user will default payment next month, true or false_. We can choose which group of users to observe by using the selectbox below : _1 for true, 0 for false_.")
    
    st.cache(suppress_st_warning=True) 
    main_data = pd.read_csv('UCI_Credit_Card.csv')
    del main_data['ID']                

    select_paydefval = st.sidebar.selectbox('Choose data to be analysed :', options = [0,1], index = 1)
    ones_data = main_data[main_data['default.payment.next.month'] == select_paydefval]

    st.sidebar.write("- Afterwards, the summary of the picked group data and its numerical and categorical columns analysis will be shown. We can choose which columns to be featured in the bar chart and pie chart respectively.") 
    st.sidebar.write("- Dataset source : https://www.kaggle.com/uciml/default-of-credit-card-clients-dataset.")
    st.sidebar.text(' ')
    st.sidebar.text(' ')
    st.sidebar.text(' ')
    
    signage1, signage2 = st.sidebar.columns([1, 4])
    signage2.markdown('_Made by : M Syahiran Khalidi_')

with categorydf:
    
    st.subheader('Categorical Columns Summary')
    distinct_data = ones_data[['SEX','EDUCATION','MARRIAGE','PAY_0',
        'PAY_2','PAY_3','PAY_4','PAY_5','PAY_6']]
    distinct_data = distinct_data.astype(str)
    st.table(distinct_data.describe(include = 'all').astype(str))

    set_col, disp_col = st.columns([1, 3])

    set_col.write(" ")
    set_col.write(" ")
    set_col.write(" ")
    set_col.write(" ")

    select_pivalue = set_col.selectbox('Choose data to be displayed in the pie-chart :', options = ['SEX','EDUCATION','MARRIAGE',
        'PAY_0','PAY_2','PAY_3','PAY_4','PAY_5','PAY_6'], index = 0)
    set_col.write('- You can click on the legend beside the pie chart to hide whichever data you want. Click it again to unhide it.')
    df2 = ones_data
    df2['Count']=np.arange(len(ones_data))     
    pie_chart = px.pie(df2,
                    values='Count',
                    names=select_pivalue,color_discrete_sequence=px.colors.sequential.RdBu)
    pie_chart.update_layout(title_text= select_pivalue, title_x=0.5)
    disp_col.plotly_chart(pie_chart)


with numericaldf:
    st.subheader('Numerical Columns Summary')
    continuous_data = ones_data.drop(['SEX','EDUCATION','MARRIAGE','PAY_0','PAY_2','PAY_3',
        'PAY_4','PAY_5','PAY_6','default.payment.next.month'], axis=1)
    st.write(continuous_data.describe())

    set_col1, disp_col1 = st.columns([1, 3])

    set_col1.write(" ")
    set_col1.write(" ")
    set_col1.write(" ")
    set_col1.write(" ")
    set_col1.write(" ")
    set_col1.write(" ")
    set_col1.write(" ")
    set_col1.write(" ")

    select_histovalue = set_col1.selectbox('Choose X-Axis', options = ['LIMIT_BAL','AGE','BILL_AMT1',
        'BILL_AMT2','BILL_AMT3','BILL_AMT4','BILL_AMT5','BILL_AMT6','PAY_AMT1','PAY_AMT2','PAY_AMT3','PAY_AMT4','PAY_AMT5','PAY_AMT6'], index = 0)
    bin_value = set_col1.slider('Number of bins : ', min_value = 5 , max_value = 15, value = 15, step = 5)
    df3 = continuous_data[select_histovalue]
    fig = px.histogram(df3, x= select_histovalue, nbins= bin_value, color_discrete_sequence=['gold'])
    fig.update_layout(bargap=0.05)
    disp_col1.plotly_chart(fig)