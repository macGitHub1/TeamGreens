import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
file1 = "Resources/WT v FREQ - 13.csv"
file2 = "Resources/WT v FREQ - 14.csv"
file3 = "Resources/WT v FREQ - 15.csv"
file4 = "Resources/WT v MJSTAT-13.csv"
file5 = "Resources/WT v MJSTAT-14.csv"
file6 = "Resources/WT v MJSTAT-15.csv"
file7 = "Resources/Distress v Freq - 13.csv"
file8 = "Resources/Distress v Freq - 14.csv"
file9 = "Resources/Distress v Freq-15.csv"
def run ():
    df = pd.read_csv(file1)
    new_df = df[['EASIEST WAY TO TELL US # DAYS USED MARIJUANA/HASH',
             'WEIGHT IN POUNDS - RECODE',
            'Unweighted Count']].copy()
    new_df.reset_index
    new_df['WEIGHT IN POUNDS - RECODE'] = new_df['WEIGHT IN POUNDS - RECODE'].apply(pd.to_numeric)
    new_df['WEIGHT IN POUNDS - RECODE'] = new_df['WEIGHT IN POUNDS - RECODE'].astype(float)
    new_df['Total Weight'] = np.multiply(new_df['WEIGHT IN POUNDS - RECODE'], new_df['Unweighted Count'])
    total_weight = new_df.groupby(['EASIEST WAY TO TELL US # DAYS USED MARIJUANA/HASH'])['Total Weight'].sum()
    total_count = new_df.groupby(['EASIEST WAY TO TELL US # DAYS USED MARIJUANA/HASH'])['Unweighted Count'].sum()
    avg_weight = total_weight/total_count
    status = new_df.groupby(['EASIEST WAY TO TELL US # DAYS USED MARIJUANA/HASH'])
    final_df = pd.DataFrame({"Average Weight": avg_weight}).round(1)
    fig, ax = plt.subplots()
    index = np.arange(len(avg_weight)) 
    bar_width = 0.2
    opacity = 0.4
    error_config = {'ecolor': '0.3'}



    rects1 = ax.bar(index, avg_weight, bar_width,
               alpha=opacity, color='b',
               error_kw=error_config,
               )



    ax.set_ylabel("Average Weight (Pounds)")
    ax.set_title("Avg Weight of Participant v Frequency of Use (2013)")
    ax.set_xticks(index)
    ax.set_xticklabels(('Weekly', 'Monthly','Yearly'), rotation=60,ha='right')

    def autolabelPass(rects1):
        for rect in rects1:
            height = rect.get_height()
            ax.text(rect.get_x() + rect.get_width()/2., 3,
                '%.1f' % float(height),
                ha='center', va='bottom', color="white")

    autolabelPass(rects1)
    plt.savefig("WtvFreq13.png")
    plt.show()
def run2 ():
    df = pd.read_csv(file2)
    new_df = df[['EASIEST WAY TO TELL US # DAYS USED MARIJUANA/HASH',
             'WEIGHT IN POUNDS - RECODE',
            'Unweighted Count']].copy()
    new_df.reset_index
    new_df[['WEIGHT IN POUNDS - RECODE', 'Unweighted Count']] = new_df[['WEIGHT IN POUNDS - RECODE', 'Unweighted Count']].astype(float)
    new_df['Total Weight'] = np.multiply(new_df['WEIGHT IN POUNDS - RECODE'], new_df['Unweighted Count'])
    total_weight = new_df.groupby(['EASIEST WAY TO TELL US # DAYS USED MARIJUANA/HASH'])['Total Weight'].sum()
    total_count = new_df.groupby(['EASIEST WAY TO TELL US # DAYS USED MARIJUANA/HASH'])['Unweighted Count'].sum()
    avg_weight = total_weight/total_count
    status = new_df.groupby(['EASIEST WAY TO TELL US # DAYS USED MARIJUANA/HASH'])
    final_df = pd.DataFrame({"Average Weight": avg_weight}).round(1)
    fig, ax = plt.subplots()
    index = np.arange(len(avg_weight)) 
    bar_width = 0.2
    opacity = 0.4
    error_config = {'ecolor': '0.3'}



    rects1 = ax.bar(index, avg_weight, bar_width,
               alpha=opacity, color='b',
               error_kw=error_config,
               )



    ax.set_ylabel("Average Weight (Pounds)")
    ax.set_title("Avg Weight of Participant v Frequency of Use (2014)")
    ax.set_xticks(index)
    ax.set_xticklabels(('Weekly', 'Monthly','Yearly'), rotation=60,ha='right')

    def autolabelPass(rects1):
        for rect in rects1:
            height = rect.get_height()
            ax.text(rect.get_x() + rect.get_width()/2., 3,
                '%.1f' % float(height),
                ha='center', va='bottom', color="white")

    autolabelPass(rects1)
    plt.savefig("WtvFreq14.png")
    plt.show()
def run3 ():
    df = pd.read_csv(file3)
    new_df = df[['EASIEST WAY TO TELL US # DAYS USED MARIJUANA/HASH',
             'WEIGHT IN POUNDS - RECODE',
            'Unweighted Count']].copy()
    new_df.reset_index
    new_df[['WEIGHT IN POUNDS - RECODE', 'Unweighted Count']] = new_df[['WEIGHT IN POUNDS - RECODE', 'Unweighted Count']].astype(float)
    new_df['Total Weight'] = np.multiply(new_df['WEIGHT IN POUNDS - RECODE'], new_df['Unweighted Count'])
    total_weight = new_df.groupby(['EASIEST WAY TO TELL US # DAYS USED MARIJUANA/HASH'])['Total Weight'].sum()
    total_count = new_df.groupby(['EASIEST WAY TO TELL US # DAYS USED MARIJUANA/HASH'])['Unweighted Count'].sum()
    avg_weight = total_weight/total_count
    status = new_df.groupby(['EASIEST WAY TO TELL US # DAYS USED MARIJUANA/HASH'])
    final_df = pd.DataFrame({"Average Weight": avg_weight}).round(1)
    fig, ax = plt.subplots()
    index = np.arange(len(avg_weight)) 
    bar_width = 0.2
    opacity = 0.4
    error_config = {'ecolor': '0.3'}



    rects1 = ax.bar(index, avg_weight, bar_width,
               alpha=opacity, color='b',
               error_kw=error_config,
               )



    ax.set_ylabel("Average Weight (Pounds)")
    ax.set_title("Avg Weight of Participant v Frequency of Use (2015)")
    ax.set_xticks(index)
    ax.set_xticklabels(('Weekly', 'Monthly','Yearly'), rotation=60,ha='right')

    def autolabelPass(rects1):
        for rect in rects1:
            height = rect.get_height()
            ax.text(rect.get_x() + rect.get_width()/2., 3,
                '%.1f' % float(height),
                ha='center', va='bottom', color="white")

    autolabelPass(rects1)
    plt.savefig("WtvFreq15.png")
    plt.show()

def run4 ():
    df = pd.read_csv(file4)
    new_df = df[['STATE MEDICAL MJ LAW STATUS AT TIME OF INTERVIEW',
             'WEIGHT IN POUNDS - RECODE',
            'Unweighted Count']]
    new_df.reset_index
    drop_df = new_df.drop(new_df.index[442:667])
    drop_df.reset_index
    drop_df[['WEIGHT IN POUNDS - RECODE', 'Unweighted Count']] = drop_df[['WEIGHT IN POUNDS - RECODE', 'Unweighted Count']].astype(float)
    drop_df['Total Weight'] = np.multiply(drop_df['WEIGHT IN POUNDS - RECODE'], drop_df['Unweighted Count'])
    total_weight = drop_df.groupby(['STATE MEDICAL MJ LAW STATUS AT TIME OF INTERVIEW'])['Total Weight'].sum()
    total_count = drop_df.groupby(['STATE MEDICAL MJ LAW STATUS AT TIME OF INTERVIEW'])['Unweighted Count'].sum()
    avg_weight = np.round(total_weight/total_count,decimals=1)
    status = drop_df.groupby(['STATE MEDICAL MJ LAW STATUS AT TIME OF INTERVIEW'])
    final_df = pd.DataFrame({"Average Weight": avg_weight}).round(1)
    fig, ax = plt.subplots()
    index = np.arange(len(avg_weight)) 
    bar_width = 0.2
    opacity = 0.4
    error_config = {'ecolor': '0.3'}



    rects1 = ax.bar(index, avg_weight, bar_width,
               alpha=opacity, color='b',
               error_kw=error_config,
               )



    ax.set_ylabel("Average Weight (Pounds)")
    ax.set_title("Avg Weight of Participant v State Approval of Marijuana (2013)")
    ax.set_xticks(index)
    ax.set_xticklabels(('State Approves Med. Marijuana', 'State Does Not Approve Med. Marijuana'), rotation=60,ha='right')

    def autolabelPass(rects1):
        for rect in rects1:
            height = rect.get_height()
            ax.text(rect.get_x() + rect.get_width()/2., 3,
                '%.1f' % float(height),
                ha='center', va='bottom', color="white")

    autolabelPass(rects1)
    plt.savefig("WtvApprov13.png")
    plt.show()
def run5 ():
    df = pd.read_csv(file5)
    new_df = df[['STATE MEDICAL MJ LAW STATUS AT TIME OF INTERVIEW',
             'WEIGHT IN POUNDS - RECODE',
            'Unweighted Count']]
    new_df.reset_index
    drop_df = new_df.drop(new_df.index[442:667])
    drop_df.reset_index
    drop_df[['WEIGHT IN POUNDS - RECODE', 'Unweighted Count']] = drop_df[['WEIGHT IN POUNDS - RECODE', 'Unweighted Count']].astype(float)
    drop_df['Total Weight'] = np.multiply(drop_df['WEIGHT IN POUNDS - RECODE'], drop_df['Unweighted Count'])
    total_weight = drop_df.groupby(['STATE MEDICAL MJ LAW STATUS AT TIME OF INTERVIEW'])['Total Weight'].sum()
    total_count = drop_df.groupby(['STATE MEDICAL MJ LAW STATUS AT TIME OF INTERVIEW'])['Unweighted Count'].sum()
    avg_weight = total_weight/total_count
    status = drop_df.groupby(['STATE MEDICAL MJ LAW STATUS AT TIME OF INTERVIEW'])
    final_df = pd.DataFrame({"Average Weight": avg_weight}).round(1)
    fig, ax = plt.subplots()
    index = np.arange(len(avg_weight)) 
    bar_width = 0.2
    opacity = 0.4
    error_config = {'ecolor': '0.3'}



    rects1 = ax.bar(index, avg_weight, bar_width,
               alpha=opacity, color='b',
               error_kw=error_config,
               )



    ax.set_ylabel("Average Weight (Pounds)")
    ax.set_title("Avg Weight of Participant v State Approval of Marijuana (2014)")
    ax.set_xticks(index)
    ax.set_xticklabels(('State Approves Med. Marijuana', 'State Does Not Approve Med. Marijuana'), rotation=60,ha='right')

    def autolabelPass(rects1):
        for rect in rects1:
            height = rect.get_height()
            ax.text(rect.get_x() + rect.get_width()/2., 3,
                '%.1f' % float(height),
                ha='center', va='bottom', color="white")

    autolabelPass(rects1)
    plt.savefig("WtvApprov14.png")
    plt.show()
def run6 ():
    df = pd.read_csv(file6)
    new_df = df[['STATE MEDICAL MJ LAW STATUS AT TIME OF INTERVIEW',
             'WEIGHT IN POUNDS - RECODE',
            'Unweighted Count']]
    new_df.reset_index
    drop_df = new_df.drop(new_df.index[442:667])
    drop_df.reset_index
    drop_df[['WEIGHT IN POUNDS - RECODE', 'Unweighted Count']] = drop_df[['WEIGHT IN POUNDS - RECODE', 'Unweighted Count']].astype(float)
    drop_df['Total Weight'] = np.multiply(drop_df['WEIGHT IN POUNDS - RECODE'], drop_df['Unweighted Count'])
    total_weight = drop_df.groupby(['STATE MEDICAL MJ LAW STATUS AT TIME OF INTERVIEW'])['Total Weight'].sum()
    total_count = drop_df.groupby(['STATE MEDICAL MJ LAW STATUS AT TIME OF INTERVIEW'])['Unweighted Count'].sum()
    avg_weight = total_weight/total_count
    status = drop_df.groupby(['STATE MEDICAL MJ LAW STATUS AT TIME OF INTERVIEW'])
    final_df = pd.DataFrame({"Average Weight": avg_weight}).round(1)
    fig, ax = plt.subplots()
    index = np.arange(len(avg_weight)) 
    bar_width = 0.2
    opacity = 0.4
    error_config = {'ecolor': '0.3'}



    rects1 = ax.bar(index, avg_weight, bar_width,
               alpha=opacity, color='b',
               error_kw=error_config,
               )



    ax.set_ylabel("Average Weight (Pounds)")
    ax.set_title("Avg Weight of Participant v State Approval of Marijuana (2015)")
    ax.set_xticks(index)
    ax.set_xticklabels(('State Approves Med. Marijuana', 'State Does Not Approve Med. Marijuana'), rotation=60,ha='right')

    def autolabelPass(rects1):
        for rect in rects1:
            height = rect.get_height()
            ax.text(rect.get_x() + rect.get_width()/2., 3,
                '%.1f' % float(height),
                ha='center', va='bottom', color="white")

    autolabelPass(rects1)
    plt.savefig("WtvApprov15.png")
    plt.show()
def run7 ():
    df = pd.read_csv(file7)
    new_df = df[['EASIEST WAY TO TELL US # DAYS USED MARIJUANA/HASH',
             'EMOT DISTRSS SO SEVERE NOTHING COULD CHEER YOU UP',
            'Unweighted Count']]
    new_df.reset_index()
    new_df.pivot(index='EASIEST WAY TO TELL US # DAYS USED MARIJUANA/HASH', columns='EMOT DISTRSS SO SEVERE NOTHING COULD CHEER YOU UP', values='Unweighted Count').plot(kind='bar')
    plt.ylabel('Respondant Count')
    plt.xlabel('')
    plt.title('Frequency of Marijuana Use vs Emotional Distress (2013)')
    plt.savefig("DistressvFreq13.png")
    plt.show()
def run8 ():
    df = pd.read_csv(file8)
    new_df = df[['EASIEST WAY TO TELL US # DAYS USED MARIJUANA/HASH',
             'EMOT DISTRSS SO SEVERE NOTHING COULD CHEER YOU UP',
            'Unweighted Count']]
    new_df.reset_index()
    new_df.pivot(index='EASIEST WAY TO TELL US # DAYS USED MARIJUANA/HASH', columns='EMOT DISTRSS SO SEVERE NOTHING COULD CHEER YOU UP', values='Unweighted Count').plot(kind='bar')
    plt.ylabel('Respondant Count')
    plt.xlabel('')
    plt.title('Frequency of Marijuana Use vs Emotional Distress (2014)')
    plt.savefig("DistressvFreq14.png")
    plt.show()
def run9 ():
    df = pd.read_csv(file9)
    new_df = df[['EASIEST WAY TO TELL US # DAYS USED MARIJUANA/HASH',
             'EMOT DISTRSS SO SEVERE NOTHING COULD CHEER YOU UP',
            'Unweighted Count']]
    new_df.reset_index()
    new_df.pivot(index='EASIEST WAY TO TELL US # DAYS USED MARIJUANA/HASH', columns='EMOT DISTRSS SO SEVERE NOTHING COULD CHEER YOU UP', values='Unweighted Count').plot(kind='bar')
    plt.ylabel('Respondant Count')
    plt.xlabel('')
    plt.title('Frequency of Marijuana Use vs Emotional Distress (2015)')
    plt.savefig("DistressvFreq14.png")
    plt.show()
    