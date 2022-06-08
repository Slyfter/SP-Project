import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import textwrap
import ipywidgets as widgets
from ipywidgets import interact, interact_manual
import IPython.display
from IPython.display import display, clear_output
import plotly.graph_objects as go
from mplsoccer import Radar, FontManager


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

a_values = []
b_values = []

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
    a_values = x

def getSAPlayers(PlayerSADropdown):
    name = PlayerSADropdown
    list = df_FW[df_FW['Player'] == name].values.tolist()
    x = list[0]
    x.pop(0)
    x.pop(0)
    x.pop(0)
    x.pop(0)
    a_values = x

def getPLPlayers(PlayerPLDropdown):
    name = PlayerPLDropdown
    list = df_FW[df_FW['Player'] == name].values.tolist()
    x = list[0]
    x.pop(0)
    x.pop(0)
    x.pop(0)
    x.pop(0)
    a_values = x
def getLLPlayers(PlayerLLDropdown):
    name = PlayerLLDropdown
    list = df_FW[df_FW['Player'] == name].values.tolist()
    x = list[0]
    x.pop(0)
    x.pop(0)
    x.pop(0)
    x.pop(0)
    a_values = x

def getL1Players(PlayerL1Dropdown):
    name = PlayerL1Dropdown
    list = df_FW[df_FW['Player'] == name].values.tolist()
    x = list[0]
    x.pop(0)
    x.pop(0)
    x.pop(0)
    x.pop(0)
    a_values = x


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


#---------------       
CompDropDown2 = widgets.Dropdown(
    options = complist,
    value = 'Bundesliga',
    description='League:',
)

def getBLPlayers2(PlayerBLDropdown2):
    name = PlayerBLDropdown2
    list = df_FW[df_FW['Player'] == name].values.tolist()
    x = list[0]
    x.pop(0)
    x.pop(0)
    x.pop(0)
    x.pop(0)
    b_values = x

def getSAPlayers2(PlayerSADropdown2):
    name = PlayerSADropdown2
    list = df_FW[df_FW['Player'] == name].values.tolist()
    x = list[0]
    x.pop(0)
    x.pop(0)
    x.pop(0)
    x.pop(0)
    b_values = x

def getPLPlayers2(PlayerPLDropdown2):
    name = PlayerPLDropdown2
    list = df_FW[df_FW['Player'] == name].values.tolist()
    x = list[0]
    x.pop(0)
    x.pop(0)
    x.pop(0)
    x.pop(0)
    b_values = x
def getLLPlayers2(PlayerLLDropdown2):
    name = PlayerLLDropdown2
    list = df_FW[df_FW['Player'] == name].values.tolist()
    x = list[0]
    x.pop(0)
    x.pop(0)
    x.pop(0)
    x.pop(0)
    b_values = x

def getL1Players2(PlayerL1Dropdown2):
    name = PlayerL1Dropdown2
    list = df_FW[df_FW['Player'] == name].values.tolist()
    x = list[0]
    x.pop(0)
    x.pop(0)
    x.pop(0)
    x.pop(0)
    b_values = x


def showLeague2(CompDropDown2):
    if (CompDropDown2 == 'Bundesliga'):
        PlayerBLDropdown2 = widgets.Dropdown(
            options = playerlistBL,
            value = None,
            description='Player:',
        )
        widgets.interact(getBLPlayers2, PlayerBLDropdown2=playerlistBL)

    if (CompDropDown2 == 'Serie A'):
        PlayerSADropdown2 = widgets.Dropdown(
            options = playerlistSA,
            value = None,
            description='Player:',
        )
        widgets.interact(getSAPlayers2, PlayerSADropdown2=playerlistSA)
     
    if (CompDropDown2 == 'Premier League'):
        PlayerPLDropdown2 = widgets.Dropdown(
            options = playerlistPL,
            value = None,
            description='Player:',
        )         
        widgets.interact(getPLPlayers2, PlayerPLDropdown2=playerlistPL)

    if (CompDropDown2 == 'La Liga'):
        PlayerPLDropdown2 = widgets.Dropdown(
            options = playerlistLL,
            value = None,
            description='Player:',
        )
        widgets.interact(getLLPlayers2, PlayerLLDropdown2=playerlistLL)

    if (CompDropDown2 == 'Ligue 1'):
        PlayerL1Dropdown2 = widgets.Dropdown(
            options = playerlistL1,
            value = None,
            description='Player:',
        )
        widgets.interact(getL1Players2, PlayerL1Dropdown2=playerlistL1)
widgets.interact(showLeague2, CompDropDown2=complist)
##----------------

URL1 = ('https://github.com/googlefonts/SourceSerifProGFVersion/blob/main/'
        'fonts/SourceSerifPro-Regular.ttf?raw=true')
serif_regular = FontManager(URL1)
URL2 = ('https://github.com/googlefonts/SourceSerifProGFVersion/blob/main/'
        'fonts/SourceSerifPro-ExtraLight.ttf?raw=true')
serif_extra_light = FontManager(URL2)
URL3 = ('https://github.com/google/fonts/blob/main/ofl/rubikmonoone/'
        'RubikMonoOne-Regular.ttf?raw=true')
rubik_regular = FontManager(URL3)
URL4 = 'https://github.com/googlefonts/roboto/blob/main/src/hinted/Roboto-Thin.ttf?raw=true'
robotto_thin = FontManager(URL4)
URL5 = 'https://github.com/googlefonts/roboto/blob/main/src/hinted/Roboto-Regular.ttf?raw=true'
robotto_regular = FontManager(URL5)
URL6 = 'https://github.com/googlefonts/roboto/blob/main/src/hinted/Roboto-Bold.ttf?raw=true'
robotto_bold = FontManager(URL6)

ranges = [(0,100),(0,100),(0,100),(0,100),(0,100),(0,100)]
params = ['AerWon%', 'Goals', 'DriSucc', 'TouAttPen', 'GCA', 'G/SH%']
low =  [0, 0, 0, 0, 0, 0]
high = [100, 100, 100, 100, 100, 100]
bruno_values =  [0.25, 0.42, 0.42, 3.47, 1.04, 8.06]
bruyne_values = [0.32, 0.00, 0.43, 3.50, 0.98, 7.72]
values = [[20,20,20,20,20,20],[20,20,20,20,20,20]]
title = 'das ishc de titel'
endnote = 'dis mami'

radar = Radar(params, low, high,
              # whether to round any of the labels to integers instead of decimal places
              round_int=[False]*6,
              num_rings=4,  # the number of concentric circles (excluding center circle)
              # if the ring_width is more than the center_circle_radius then
              # the center circle radius will be wider than the width of the concentric circles
              ring_width=1, center_circle_radius=1)

# plot radar
fig, ax = radar.setup_axis()
rings_inner = radar.draw_circles(ax=ax, facecolor='#ffb2b2', edgecolor='#fc5f5f')
radar_output = radar.draw_radar_compare(a_values, b_values, ax=ax,
                                        kwargs_radar={'facecolor': '#00f2c1', 'alpha': 0.6},
                                        kwargs_compare={'facecolor': '#d80499', 'alpha': 0.6})
radar_poly, radar_poly2, vertices1, vertices2 = radar_output
range_labels = radar.draw_range_labels(ax=ax, fontsize=15,
                                       fontproperties=robotto_thin.prop)
param_labels = radar.draw_param_labels(ax=ax, fontsize=15,
                                       fontproperties=robotto_regular.prop)
