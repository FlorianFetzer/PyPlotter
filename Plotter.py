# -*- coding: utf-8 -*-
"""
Created on Fri Mar 21 08:58:40 2014

@author: florian
"""

import numpy as np
import matplotlib.pyplot as plt

class Plotter:
    figure_list = list()
    
    
    def plot_file(self, fil,cols_of_interest, figure_number, title):
        """  f is filedict, cols_of_interst is defined in dialog """
        print 'plot_file'
        if figure_number in range(len(self.figure_list)):
            f = self.figure_list[figure_number]
        else:
            f = plt.figure(figure_number)
            self.figure_list.append(f)
        for col in cols_of_interest:
            print col
            if col !='Zeit':
                plt.plot(fil['Zeit'], fil[col], label = col)
        plt.title(title)
        plt.legend()
                
    def plot_column(self, x_axis, col_data, figure_number, lab):
        print 'plot column'
        if figure_number in range(len(self.figure_list)):
            f = self.figure_list[figure_number]
        else:
            f = plt.figure(figure_number)
            self.figure_list.append(f)
        plt.plot(x_axis, col_data, label = lab)
        plt.legend()
        
            
            
    def newfigure(self):
        f = plt.figure(len(self.figure_list))
        self.figure_list.append(f)
    