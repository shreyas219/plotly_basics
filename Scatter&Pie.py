# -*- coding: utf-8 -*-
"""
Created on Sun Nov  4 14:48:09 2018

@author: Shreyas S
"""
import plotly.plotly as py
from plotly.offline import plot
import plotly.graph_objs as go
import numpy as np

#Code to create scatter plot

N = 2000
example_x = np.random.rand(N)
example_x = list(example_x)
example_y = np.random.rand(N)
example_y = list(example_y)

trace = go.Scatter(
        x = example_x,
        y = example_y,
        mode = 'markers')

data = [trace]

plot(data)


#Code to create pie chart

#create categories
groups = ["Python", "R", "SQL", "MATLAB", "Java", "C/C++"]

#create the value of those categories respectively
percent = [150,130,100,40,20,15]

#Assign colors to the category respectively
colors = ["#FB0602", "#FBBB02", "#E8FB02", "#0AFB02", "#02A0FB", "#FB02DD"]

trace = go.Pie(labels = groups, values = percent,
               hoverinfo = 'label+percent', textinfo = 'label+value',
               textfont = dict(size = 20),
               marker = dict(colors = colors,
                             line = dict(color = '#6A6A6A', width = 2)))
                                         
                                         
plot([trace])
          