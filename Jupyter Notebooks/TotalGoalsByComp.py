import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import textwrap

import ipywidgets as widgets
from ipywidgets import interact, interact_manual
import IPython.display
from IPython.display import display, clear_output

import plotly.graph_objects as go

df = pd.read_csv("data.csv", encoding = "ISO-8859-1", sep=";")

df.insert(2,"RealGoals", round(df['90s']*df['Goals']))
df.insert(3,'RealShots', round(df['90s']*df['Shots']))

df_GoalsbyComps = df.groupby('Comp', as_index=False).sum()
df_GoalsbyCompsTemp = df_GoalsbyComps[['Comp','RealGoals']]

courses = list(df_GoalsbyCompsTemp['Comp'])
values = list(df_GoalsbyCompsTemp['RealGoals'])

fig = plt.figure(figsize = (10,5))

plt.bar(courses, values, color = 'blue', width = 0.4)

plt.xlabel("Ligen")
plt.ylabel("Number of goals")
plt.title("Total number of goals for each league")
plt.show()

df_GoalsbySquads = df.groupby(['Comp','Squad'], as_index=False).sum()

df_GoalsbySquadTemp = df_GoalsbySquads[['Comp','Squad','RealGoals','RealShots']]

df_GoalsbySquadsBL = df_GoalsbySquadTemp[df_GoalsbySquadTemp['Comp'] == "Bundesliga"]

df_GoalsbySquadsBL

goalsBL = list(df_GoalsbySquadsBL['RealGoals'])
shotsBL = list(df_GoalsbySquadsBL['RealShots'])
squadsBL = list(df_GoalsbySquadsBL['Squad'])

def ShowBLGraph():
    plt.figure(figsize=(12,8))
    plt.scatter(goalsBL,shotsBL,s=50,alpha=0.5)
    plt.axhline(y=500, color='red')
    plt.axvline(x=60, color='red')
    plt.xlabel("Goals")
    plt.ylabel("Shots")
    plt.title("Bundesliga - Shots / Goal ratio")
    for i in range(len(squadsBL)):
        if(goalsBL[i]> 60):
            plt.annotate(squadsBL[i],(goalsBL[i], shotsBL[i]), ha='left')
    plt.show()

df_GoalsbySquads = df.groupby(['Comp','Squad'], as_index=False).sum()

df_GoalsbySquadTemp = df_GoalsbySquads[['Comp','Squad','RealGoals','RealShots']]

df_GoalsbySquadsLL = df_GoalsbySquadTemp[df_GoalsbySquadTemp['Comp'] == "La Liga"]

df_GoalsbySquadsLL

goalsLL = list(df_GoalsbySquadsLL['RealGoals'])
shotsLL = list(df_GoalsbySquadsLL['RealShots'])
squadsLL = list(df_GoalsbySquadsLL['Squad'])

def ShowLLGraph():
    plt.figure(figsize=(12,8))
    plt.scatter(goalsLL,shotsLL,s=50,alpha=0.5)
    plt.axhline(y=500, color='red')
    plt.axvline(x=55, color='red')
    plt.xlabel("Goals")
    plt.ylabel("Shots")
    plt.title("La Liga - Shots / Goal ratio")
    for i in range(len(squadsLL)):
        if(goalsLL[i]> 55):
            plt.annotate(squadsLL[i],(goalsLL[i], shotsLL[i]), ha='left')


df_GoalsbySquads = df.groupby(['Comp','Squad'], as_index=False).sum()

df_GoalsbySquadTemp = df_GoalsbySquads[['Comp','Squad','RealGoals','RealShots']]

df_GoalsbySquadsL1 = df_GoalsbySquadTemp[df_GoalsbySquadTemp['Comp'] == "Ligue 1"]

df_GoalsbySquadsL1

goalsL1 = list(df_GoalsbySquadsL1['RealGoals'])
shotsL1 = list(df_GoalsbySquadsL1['RealShots'])
squadsL1 = list(df_GoalsbySquadsL1['Squad'])

def ShowL1Graph():
    plt.figure(figsize=(12,8))
    plt.scatter(goalsL1,shotsL1,s=50,alpha=0.5)
    plt.axhline(y=463, color='red')
    plt.axvline(x=60, color='red')
    plt.xlabel("Goals")
    plt.ylabel("Shots")
    plt.title("Ligue 1 - Shots / Goal ratio")
    for i in range(len(squadsL1)):
        if(goalsL1[i]>= 60):
            plt.annotate(squadsL1[i],(goalsL1[i], shotsL1[i]), ha='left')


df_GoalsbySquads = df.groupby(['Comp','Squad'], as_index=False).sum()

df_GoalsbySquadTemp = df_GoalsbySquads[['Comp','Squad','RealGoals','RealShots']]

df_GoalsbySquadsPL = df_GoalsbySquadTemp[df_GoalsbySquadTemp['Comp'] == "Premier League"]

df_GoalsbySquadsPL

goalsPL = list(df_GoalsbySquadsPL['RealGoals'])
shotsPL = list(df_GoalsbySquadsPL['RealShots'])
squadsPL = list(df_GoalsbySquadsPL['Squad'])

def ShowPLGraph():
    plt.figure(figsize=(12,8))
    plt.scatter(goalsPL,shotsPL,s=50,alpha=0.5)
    plt.axhline(y=550, color='red')
    plt.axvline(x=60, color='red')
    plt.xlabel("Goals")
    plt.ylabel("Shots")
    plt.title("Premier League - Shots / Goal ratio")
    for i in range(len(squadsPL)):
        if(goalsPL[i]>= 60):
            plt.annotate(squadsPL[i],(goalsPL[i], shotsPL[i]), ha='left')

df_GoalsbySquads = df.groupby(['Comp','Squad'], as_index=False).sum()

df_GoalsbySquadTemp = df_GoalsbySquads[['Comp','Squad','RealGoals','RealShots']]

df_GoalsbySquadsSA = df_GoalsbySquadTemp[df_GoalsbySquadTemp['Comp'] == "Serie A"]

df_GoalsbySquadsSA

goalsSA = list(df_GoalsbySquadsSA['RealGoals'])
shotsSA = list(df_GoalsbySquadsSA['RealShots'])
squadsSA = list(df_GoalsbySquadsSA['Squad'])

def ShowSAGraph():
    plt.figure(figsize=(12,8))
    plt.scatter(goalsSA,shotsSA,s=50,alpha=0.5)
    plt.axhline(y=500, color='red')
    plt.axvline(x=55, color='red')
    plt.xlabel("Goals")
    plt.ylabel("Shots")
    plt.title("Serie A - Shots / Goal ratio")
    for i in range(len(squadsSA)):
        if(goalsSA[i]>= 55):
            plt.annotate(squadsSA[i],(goalsSA[i], shotsSA[i]), ha='left')
    plt.show()


ligen = df.groupby('Comp', as_index=False).sum()

ligenComp = list(ligen['Comp'])

League = widgets.Dropdown(
    options = ligenComp,
    value = None,
    description='League:',
)

def ShowGraph(League):
    if(League == 'Bundesliga'):
        clear_output()
        ShowBLGraph()
    if(League == 'La Liga'):
        clear_output()
        ShowLLGraph()
    if(League == 'Serie A'):
        clear_output()
        ShowSAGraph()
    if(League == 'Ligue 1'):
        clear_output()
        ShowL1Graph()
    if(League == 'Premier League'):
        clear_output()
        ShowPLGraph()
        
widgets.interact(ShowGraph, League=ligenComp)
