# -*- coding: utf-8 -*-
"""
Created on Thu Nov  8 17:39:25 2018

@author: Shreyas S
"""

import pandas as pd
from plotly.offline import plot
import plotly.graph_objs as go

pubg = pd.read_csv('PUBG_Player_Statistics.csv')

df_pubg = pubg.apply(pd.to_numeric, errors='ignore')
df_new_pubg = df_pubg.head(10)


trace = go.Scatter(x = df_new_pubg['solo_RoundsPlayed'], y = df_new_pubg['solo_Wins'],
                   name = 'Rounds Won')
layout = go.Layout(title = 'Pubg Wins vs Rounds Played',
                   plot_bgcolor = 'rgb(230,230, 230)',
                   showlegend = True)
fig = go.Figure(data = [trace], layout = layout)

plot(fig, filename = 'test')


df_bar_pubg = df_pubg.head(20)

trace1 = go.Bar(x = df_bar_pubg['player_name'],
                y = df_bar_pubg['solo_RoundsPlayed'],
                name = 'Rounds Played')

trace2 = go.Bar(x = df_bar_pubg['player_name'],
                y = df_bar_pubg['solo_Wins'],
                name = 'Wins')

data = [trace1, trace2]

layout = go.Layout(barmode = 'group')

fig = go.Figure(data = data, layout = layout)

plot(fig, filename = 'GroupBar')