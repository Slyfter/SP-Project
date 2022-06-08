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

name = 'Robert Lewandowski'


df_FW = df[df['Pos'] == 'FW']
df_FW = df_FW[['Player', 'Pos', 'Comp', 'Squad', 'AerWon%']].copy()
df_FW['Goals'] = round(df['Goals'] * df['90s'])
df_FW['DriSucc'] = round(df['DriSucc'] * df['90s'])
df_FW['TouAttPen'] = round(df['TouAttPen'] * df['90s'])
df_FW['GCA'] = round(df['GCA'] * df['90s'])
df_FW['G/Sh%'] = round(df['G/Sh'] * 100)

df_complist = df_FW['Comp']
df_complist = df_complist.drop_duplicates()
complist = df_complist

playerlistBL = df_FW[df_FW['Comp'] == 'Bundesliga']
playerlistBL = playerlistBL['Player']

playerlistSA = df_FW[df_FW['Comp'] == 'Serie A']
playerlistSA = playerlistSA['Player']

playerlistPL = df_FW[df_FW['Comp'] == 'Premier League']
playerlistPL = playerlistPL['Player']

playerlistLL = df_FW[df_FW['Comp'] == 'La Liga']
playerlistLL = playerlistLL['Player']

playerlistL1 = df_FW[df_FW['Comp'] == 'Ligue 1']
playerlistL1 = playerlistL1['Player']

CompDropDown = widgets.Dropdown(
    options = complist,
    value = 'Bundesliga',
    description='League:',
)

def getBLPlayers(PlayerBLDropdown):
    name = PlayerBLDropdown
    list = df_FW[df_FW['Player'] == name].values.tolist()
    x = list[0]
    x.pop(0)
    x.pop(0)
    x.pop(0)
    x.pop(0)
    print(x)

def getSAPlayers(PlayerSADropdown):
    name = PlayerSADropdown
    list = df_FW[df_FW['Player'] == name].values.tolist()
    x = list[0]
    x.pop(0)
    x.pop(0)
    x.pop(0)
    x.pop(0)
    print(x)

def getPLPlayers(PlayerPLDropdown):
    name = PlayerPLDropdown
    list = df_FW[df_FW['Player'] == name].values.tolist()
    x = list[0]
    x.pop(0)
    x.pop(0)
    x.pop(0)
    x.pop(0)
    print(x)
def getLLPlayers(PlayerLLDropdown):
    name = PlayerLLDropdown
    list = df_FW[df_FW['Player'] == name].values.tolist()
    x = list[0]
    x.pop(0)
    x.pop(0)
    x.pop(0)
    x.pop(0)
    print(x)

def getL1Players(PlayerL1Dropdown):
    name = PlayerL1Dropdown
    list = df_FW[df_FW['Player'] == name].values.tolist()
    x = list[0]
    x.pop(0)
    x.pop(0)
    x.pop(0)
    x.pop(0)
    print(x)


def showLeague(CompDropDown):
    if (CompDropDown == 'Bundesliga'):
        PlayerBLDropdown = widgets.Dropdown(
            options = playerlistBL,
            value = None,
            description='Player:',
        )
        widgets.interact(getBLPlayers, PlayerBLDropdown=playerlistBL)

    if (CompDropDown == 'Serie A'):
        PlayerSADropdown = widgets.Dropdown(
            options = playerlistSA,
            value = None,
            description='Player:',
        )
        widgets.interact(getSAPlayers, PlayerSADropdown=playerlistSA)
     
    if (CompDropDown == 'Premier League'):
        PlayerPLDropdown = widgets.Dropdown(
            options = playerlistPL,
            value = None,
            description='Player:',
        )         
        widgets.interact(getPLPlayers, PlayerPLDropdown=playerlistPL)

    if (CompDropDown == 'La Liga'):
        PlayerPLDropdown = widgets.Dropdown(
            options = playerlistLL,
            value = None,
            description='Player:',
        )
        widgets.interact(getLLPlayers, PlayerLLDropdown=playerlistLL)

    if (CompDropDown == 'Ligue 1'):
        PlayerL1Dropdown = widgets.Dropdown(
            options = playerlistL1,
            value = None,
            description='Player:',
        )
        widgets.interact(getL1Players, PlayerL1Dropdown=playerlistL1)

widgets.interact(showLeague, CompDropDown=complist)



