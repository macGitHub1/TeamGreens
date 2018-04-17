import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns



def run():
    #Get source data
    data_source = pd.read_csv('Data_em.csv')
    # Show the results of a linear regression within each dataset
    fig = sns.lmplot(data=data_source,
           x='Marijuana',
           y='Alcohol',
           hue='State',
           fit_reg=False)
    fig.savefig('US.png')

def runState(state = "Total U.S.", drug = "Alcohol" ):
    #Get source data
    data_source = pd.read_csv('Data_em.csv')
    #get state data and sort
    state_df = data_source.set_index("State")
    sorted_state_df = state_df .loc[state].sort_values("Year",ascending=False)    
    fig = plt.figure()
    ax = plt.axes()   
    ax.plot(sorted_state_df["Year"],sorted_state_df[drug])
    outputPng = state + drug +".png"
    plt.savefig(outputPng)

    
def runBothState(state = "Total U.S."):
    #Get source data
    data_source = pd.read_csv('Data_em.csv')
    #get state data and sort
    state_df = data_source.set_index("State")
    sorted_state_df = state_df .loc[state].sort_values("Year",ascending=False)    
    fig = plt.figure()
    ax1 = plt.axes()
    ax2 = plt.axes()
    ax1.plot(sorted_state_df["Year"],sorted_state_df["Alcohol"])
    ax1.plot(sorted_state_df["Year"],sorted_state_df["Marijuana"])

