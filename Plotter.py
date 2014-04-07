# -*- coding: utf-8 -*-
"""
Created on Fri Mar 21 08:58:40 2014

@author: florian
"""
import copy
import numpy as np
import matplotlib.pyplot as plt
import os

class Plotter:
    figure_list = dict()       
         
         
    def export(self, figure_number):
        exnumber = str(np.max([int(s.split('_')[1].strip('.txt')) for s in os.listdir(os.getcwd()) if s.startswith('export')]) + 1)
        header = ''
        li = list()
        for ax in self.figure_list[figure_number].axes:
            for l in ax.lines:
                li.append(l.get_data()[0])
                li.append(l.get_data()[1])
                header = header + 'X-Axis' + '\t' + l.get_label() + '\t'
                print header
                print len(li)
        x = np.asanyarray(li)
        x = x.swapaxes(0,1)
        np.savetxt('export_' +exnumber + '.txt', x, fmt = '%3.4f')
        fi = open('export_' +exnumber + '.txt','r+')
        old = fi.read()
        fi.seek(0)
        fi.write(header + '\n' + old)
        fi.close()
    
    def plot_file(self, fil,cols_of_interest, figure_number, title):
        """  f is filedict, cols_of_interst is defined in dialog """
        print 'plot_file'
        if figure_number in self.figure_list.keys():
            f = self.figure_list[figure_number]
        else:
            f = plt.figure(figure_number)
            self.figure_list[figure_number] = f
        for col in cols_of_interest:
            print col
            if col !='Zeit':
                plt.plot(fil['Zeit'], fil[col], label = col)
        plt.title(title)
        plt.legend()
        print self.figure_list
                
    def plot_column(self, x_axis, col_data, figure_number, lab):
        print 'plot column'
        if figure_number in self.figure_list.keys():
            f = self.figure_list[figure_number]                
        else:
            f = plt.figure(figure_number)
            self.figure_list[figure_number] = f
            f.add_axes()
            plt.title('Data Plot')
        data_ax = f.axes[0]
        data_ax.plot(x_axis, col_data, label = lab)
        plt.legend(prop={'size':6})
        plt.title('Data Plot')
        print self.figure_list
        
    def plot_eval(self, eval_function, args, figure_number, in_active_figure, selected_range, subtract_mean):
        f = self.figure_list[figure_number]
        data_ax = f.axes[0]
        data_ax_xlim = data_ax.get_xlim()
        print 'xlim ', data_ax.get_xlim()
        if in_active_figure:
            if len(f.axes)==1: # bis jetz nur die Daten in einziger achse
                print 'first, add axes'
                f.delaxes(f.axes[0])
                f.add_subplot(2,1,1)
                for l in data_ax.lines:
                    lab = l.get_label()
                    x = l.get_data()[0]
                    y = l.get_data()[1]
                    plt.plot(x,y, label = lab)
                    plt.xlim(data_ax_xlim)
                plt.legend()    
                eval_ax = f.add_subplot(2,1,2)
                if eval_function != self.fft:
                    eval_ax.set_xlim(data_ax_xlim)
            else:
                print '2nd'
                eval_ax = f.axes[1]
                eval_ax.lines = [] # clear old lines
            for l in data_ax.lines:
                line_data = l.get_data()
                if selected_range:  # get line with only data of the x-range in the figure
                    end_ind = len(line_data[0])-1
                    start_ind = 0
                    for i in range(len(line_data[0])-1): # find range
                        if line_data[0][i+1] > data_ax.get_xlim()[0] and line_data[0][i] <= data_ax.get_xlim()[0]:
                            start_ind = i
                            print start_ind
                        if line_data[0][i+1] > data_ax.get_xlim()[1] and line_data[0][i] <= data_ax.get_xlim()[1]:
                            end_ind = i
                            print end_ind - start_ind
                            break
                    l.set_data(line_data[0][start_ind:end_ind], line_data[1][start_ind:end_ind])
                    print 'len line_data before eval_func ', len(l.get_data()[0])
                (x,y,lab) = eval_function(l, args, subtract_mean)
                l.set_data(line_data)
                eval_ax.plot(x,y, label = lab)
                eval_ax.set_xlim((np.min(x), np.max(x)))
                eval_ax.set_ylim((np.min(y), np.max(y)))
                if eval_function == self.fft:
                    plt.title('FFT')
            print 'Anz. der Axen: ', len(f.axes)
        else:
            figure_number = np.max(self.figure_list.keys())+ 1
            print 'new figure: ', figure_number
            feval = plt.figure(figure_number) # last figure
            self.figure_list[figure_number] = feval
            data_ax = f.axes[0]
            for l in data_ax.lines:
                line_data = l.get_data()
                if selected_range:  # get line with only data of the x-range in the figure
                    end_ind = len(line_data[0])-1
                    start_ind = 0
                    for i in range(len(l.get_data()[0])-1): # find range
                        if l.get_data()[0][i+1] > data_ax.get_xlim()[0] and l.get_data()[0][i] <= data_ax.get_xlim()[0]:
                            start_ind = i
                        if l.get_data()[0][i+1] > data_ax.get_xlim()[1] and l.get_data()[0][i] <= data_ax.get_xlim()[1]:
                            end_ind = i
                            break
                    l.set_data(l.get_data()[0][start_ind:end_ind], l.get_data()[1][start_ind:end_ind])
                (x,y,lab) = eval_function(l, args, subtract_mean)
                l.set_data(line_data)
                plt.plot(x,y, label = lab)
        plt.title(lab.split('::')[0])
        plt.legend()
        print self.figure_list
        return figure_number        
        
    def mav(self, l, mav_edit, subtract_mean):
        print 'Plotter.mav'
        lab = l.get_label()
        x = l.get_data()[0]
        y = np.zeros(len(l.get_data()[1]) + 2*mav_edit)
        y[0:mav_edit] = l.get_data()[1][0]
        y[mav_edit:mav_edit + len(l.get_data()[1])] = l.get_data()[1]
        y[mav_edit + len(l.get_data()[1])-1:] = l.get_data()[1][-1]
        y = np.convolve(y, np.ones(mav_edit)/mav_edit, 'same')
        y = y[mav_edit:-mav_edit]
        return (x,y,'MAV-'+str(mav_edit) + '::' + lab)
        
    def mvar(self, l, mav_edit, subtract_mean):
        print 'Plotter.mvar'
        lab = l.get_label()
        x = l.get_data()[0]
        y = np.zeros(len(l.get_data()[1]) + 2*mav_edit)
        y[0:mav_edit] = l.get_data()[1][0:mav_edit]
        y[mav_edit:mav_edit + len(l.get_data()[1])] = l.get_data()[1]
        y[mav_edit + len(l.get_data()[1])-1:] = l.get_data()[1][-1]
        print mav_edit,len(y)-mav_edit
        yn = np.zeros(len(y))
        for i in range(mav_edit,len(y)-mav_edit):
            yn[i] = np.var(y[i-int(mav_edit/2):i+mav_edit - int(mav_edit/2)])
        yn = yn[mav_edit:-mav_edit]
        print mav_edit,len(yn)-mav_edit
        return (x,yn,'MVAR-'+str(mav_edit) + ', avg='+str(np.mean(yn))+ '::' + lab)
        
    def mmmin(self, l, mav_edit, subtract_mean):
        print 'Plotter.mvar'
        lab = l.get_label()
        x = l.get_data()[0]
        y = np.zeros(len(l.get_data()[1]) + 2*mav_edit)
        y[0:mav_edit] = l.get_data()[1][0:mav_edit]
        y[mav_edit:mav_edit + len(l.get_data()[1])] = l.get_data()[1]
        y[mav_edit + len(l.get_data()[1])-1:] = l.get_data()[1][-1]
        yn = np.zeros(len(y))
        for i in range(mav_edit,len(y)-mav_edit):
            print i
            yn[i] = np.max(y[i-int(mav_edit/2):i+mav_edit - int(mav_edit/2)]) / np.min(y[i-int(mav_edit/2):i+mav_edit - int(mav_edit/2)])
        yn = yn[mav_edit:-mav_edit]
        return (x,yn,'MMMIN-'+str(mav_edit) + ', avg='+str(np.mean(yn))+ '::' + lab)
        
    def autocorr(self,l, args, subtract_mean):
        print 'Plotter.autocorr'
        lab = l.get_label()
        x = l.get_data()[0]
        y = l.get_data()[1]
        centered_signal = y - np.mean(y)
        ft_signal = np.fft.fft(centered_signal)
        powerSpectralDensity = np.abs(ft_signal)**2
        autoc = np.real(np.fft.ifft(powerSpectralDensity) / len(centered_signal))
        return (np.arange(0,len(autoc,x[2]-x[1])), autoc, 'Autocorr::' + lab)
        
    def correlate(self,l, args, subtract_mean):
        print 'Plotter.corr'
        lab = l.get_label()
        x = l.get_data()[0]
        y = l.get_data()[1]
        centered_signal = y - np.mean(y)
        ft_signal = np.fft.fft(centered_signal)
        powerSpectralDensity = np.abs(ft_signal)**2
        autoc = np.real(np.fft.ifft(powerSpectralDensity) / len(centered_signal))
        print autoc.flat[0]
        #print len(np.arange(0,len(autoc),x[2]-x[1]))
        return (np.arange(0,len(autoc)*(x[2]-x[1]),x[2]-x[1]), autoc/autoc.flat[0], 'Autocorr::' + lab)
        
    def fft(self,l, args, subtract_mean):
        print 'Plotter.fft'
        lab = l.get_label()
        x = l.get_data()[0]
        y = l.get_data()[1]
        if subtract_mean:
            y = y-np.mean(y)
        spec = np.abs(np.fft.fft(y)) / np.sum(np.abs(np.fft.fft(y)))
        print len(x), len(y)
        freqs = np.fft.fftfreq(spec.size, x[2]-x[1])
        idx = np.argsort(freqs)
        return (freqs[idx], spec[idx], 'FFT::' + lab)
          
            
    def newfigure(self):
        f = plt.figure(len(self.figure_list))
        self.figure_list.append(f)
    