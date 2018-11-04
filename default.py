# -*- coding: utf-8 -*-
"""
Created on Sun Nov  4 12:27:15 2018

@author: Shreyas S
"""
import plotly
from plotly.offline import iplot, plot

#basic plotting. This will plot the data and display it in an html file
# while the below command is run
plot([{"x": [10,20,30,40,50,60,70,80,90,100], "y":[19,14,56,5,22,46,30,90,61,35]}]) 

import plotly.graph_objs as go
import numpy as np

x = np.random.randn(2000)
x = list(x)
y = np.random.randn(2000)
y = list(y)

plot([go.Histogram2dContour(x = x, y = y, contours = dict(coloring = 'heatmap')),
      go.Scatter(x = x, y = y, mode = 'markers', marker = dict(color = 'white', size = 3, opacity = 0.3))], show_link = False)