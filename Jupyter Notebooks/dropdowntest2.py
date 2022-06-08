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

CompDropDown = widgets.Dropdown(
    options = complist,
    value = None,
    description='League:',
)

def showLeague(CompDropDown):
    if (CompDropDown == 'Bundesliga'):
        PlayerBLDropdown = widgets.Dropdown(
            options = playerlistBL,
            value = None,
            description='Player:',
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
                

        widgets.interact(getBLPlayers, PlayerBLDropdown=playerlistBL)

widgets.interact(showLeague, CompDropDown=complist)



