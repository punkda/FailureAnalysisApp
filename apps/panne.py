import streamlit as st
import numpy as np
import pandas as pd
from sklearn import datasets
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.graph_objects as go

def app():
    Hist_Pannes=pd.read_excel("data.xlsx") 
    
    surjet=Hist_Pannes[Hist_Pannes['Machine'] == 'surjet']
    zigzag=Hist_Pannes[Hist_Pannes['Machine'] == 'zig-zag']
    recouvrement=Hist_Pannes[Hist_Pannes['Machine'] == 'recouvrement']
    piqeuse=Hist_Pannes[Hist_Pannes['Machine'] == 'piqueuse']
    brideuse=Hist_Pannes[Hist_Pannes['Machine'] == 'brideuse']
    doubleaiguille=Hist_Pannes[Hist_Pannes['Machine'] == 'double aiguille'] 
    
    surjet_count  = surjet['naturedepanne'].value_counts()
    zigzag_count= zigzag['naturedepanne'].value_counts()
    doubleaiguille_count= doubleaiguille['naturedepanne'].value_counts()
    recouvrement_count=recouvrement['naturedepanne'].value_counts()
    piqueuse_count= piqeuse['naturedepanne'].value_counts()
    brideuse_count=brideuse['naturedepanne'].value_counts()
    
    fig = plt.figure(figsize=(10,5))
    sns.barplot(surjet_count.index, surjet_count.values, alpha=0.8)

    plt.title('Count Failure for "surjet" machine')
    plt.ylabel('Number of Failures', fontsize=12)
    plt.xlabel('Failure type', fontsize=12)
    plt.xticks(rotation = 45)
    plt.xticks(fontsize=8)

    
    st.pyplot(fig)
    
    
    fig2 = plt.figure(figsize=(10,5))
    sns.barplot(zigzag_count.index, zigzag_count.values, alpha=0.8)

    plt.title('Count Failure for "zigzag" machine')
    plt.ylabel('Number of Failures', fontsize=12)
    plt.xlabel('Failure type', fontsize=12)
    plt.xticks(rotation = 45)
    plt.xticks(fontsize=8)

    
    st.pyplot(fig2)
    
    fig4 = plt.figure(figsize=(10,5))
    sns.barplot(recouvrement_count.index, recouvrement_count.values, alpha=0.8)

    plt.title('Count Failure for "recouvrement" machine')
    plt.ylabel('Number of Failures', fontsize=12)
    plt.xlabel('Failure type', fontsize=12)
    plt.xticks(rotation = 45)
    plt.xticks(fontsize=8)

    
    st.pyplot(fig4)
    
    fig4= plt.figure(figsize=(10,5))
    sns.barplot(piqueuse_count.index, piqueuse_count.values, alpha=0.8)

    plt.title('Count Failure for "piqueuse" machine')
    plt.ylabel('Number of Failures', fontsize=12)
    plt.xlabel('Failure type', fontsize=12)
    plt.xticks(rotation = 45)
    plt.xticks(fontsize=8)

    
    st.pyplot(fig4)
    
    
    fig5= plt.figure(figsize=(10,5))
    sns.barplot(brideuse_count.index, brideuse_count.values, alpha=0.8)

    plt.title('Count Failure for "briseuse" machine')
    plt.ylabel('Number of Failures', fontsize=12)
    plt.xlabel('Failure type', fontsize=12)
    plt.xticks(rotation = 45)
    plt.xticks(fontsize=8)

    
    st.pyplot(fig5)
    
    
    
    
    
    
    fig3 = plt.figure(figsize=(10,5))
    sns.barplot(doubleaiguille_count.index, doubleaiguille_count.values, alpha=0.8)

    plt.title('Count Failure for "double aiguille" machine')
    plt.ylabel('Number of Failures', fontsize=12)
    plt.xlabel('Failure type', fontsize=12)
    plt.xticks(rotation = 45)
    plt.xticks(fontsize=8)

    
    st.pyplot(fig3)
    
    
    
    
    
    
    
    
    
    fig1 = plt.figure(figsize=(10,5))
    sns.barplot(brideuse_count.index, brideuse_count.values, alpha=0.8)

    plt.title('Count Failure for "brideuse" machine')
    plt.ylabel('Number of Failures', fontsize=12)
    plt.xlabel('Failure type', fontsize=12)
    plt.xticks(rotation = 45)
    plt.xticks(fontsize=8)

    
    st.pyplot(fig1)
    
    

    

 

 



