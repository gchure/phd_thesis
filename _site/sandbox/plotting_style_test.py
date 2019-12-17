# -*- coding:utf-8 -*-
#%%
import sys
sys.path.insert(0, '../')
import numpy as np
import matplotlib.pyplot as plt
import phd.viz
import imp
import bokeh.io 
import bokeh.plotting
bokeh.io.output_notebook()
imp.reload(phd.viz)
colors = phd.viz.phd_style()
# _colors, _color = phd.viz.bokeh_theme()


fig, ax = plt.subplots(1, 1)
x = np.linspace(-2 * np.pi, 2 * np.pi, 200)
for i in range(1, 5):
    y1 = np.sin(1/i * np.sin(1/i * np.sin(i * x)))
    ax.plot(x, y1)

ax.set_xlabel('this is the x axis [$k_BT$]')
ax.set_ylabel(r'this is the $y$ axis [$\Delta\varepsilon_{RA}$]')



p = bokeh.plotting.figure(width=600, height=400, x_axis_label='this is the x axis',
                          y_axis_label='this is the y axis')



x = np.linspace(-2 * np.pi, 2 * np.pi, 200)
for i in range(1, 5):
    y1 = np.sin(1/i * np.sin(1/i * np.sin(i * x)))
    p.line(x, y1, color=_color[i-1])



bokeh.io.show(p)



#%%
