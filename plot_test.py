# -*- coding: utf-8 -*-
"""
Created on Sun Mar 23 10:51:37 2014

@author: florian
"""

f = dialog.Plotter.figure_list[0]
data_ax = f.axes[0]

f.delaxes(f.axes[0])
f.add_subplot(2,1,1)
for l in data_ax.lines:
    lab = l.get_label()
    x = l.get_data()[0]
    y = l.get_data()[1]
    plt.plot(x,y, label = lab)
    
f.add_subplot(2,1,2)
for l in data_ax.lines:
    lab = l.get_label()
    x = l.get_data()[0]
    y = l.get_data()[1]
    plt.plot(x,y, label = 'MAV::' + lab)


plt.title('MAV')