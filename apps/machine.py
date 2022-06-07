import streamlit as st
import numpy as np
import pandas as pd
from sklearn import datasets
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns


def app():
   

    st.subheader("Number of failure per type of machine")
    st.markdown("""                 """)
    st.markdown("""                 """)
    st.markdown("""                 """)

    df = pd.read_excel("data.xlsx")
    val_count  = df['Machine'].value_counts()
    fig = plt.figure(figsize=(10,5))
    sns.barplot(val_count.index, val_count.values, alpha=0.8)
    plt.title('Count Failure Per Machine')
    plt.ylabel('Number of Failures', fontsize=12)
    plt.xlabel('Machine', fontsize=12)
    plt.xticks(rotation = 45)
    plt.xticks(fontsize=8)

 # Add figure in streamlit app
    st.pyplot(fig)
    
    
    
    
    
