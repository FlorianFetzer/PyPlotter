# -*- coding: utf-8 -*-
"""
Created on Thu Mar 20 17:38:17 2014

@author: florian
"""

import sys 
import os
from PyQt4 import QtGui, QtCore
from diag import Ui_Dialog as Dlg
from DataReader import DataReader
from Plotter import Plotter
import numpy as np

class MeinDialog(QtGui.QDialog, Dlg): 
    def __init__(self): 
        QtGui.QDialog.__init__(self) 
        self.setupUi(self)        
        self.datreader = DataReader()        
        self.Plotter = Plotter()
        self.directory = os.getcwd()
        self.WorkingD_label.setText(self.directory)
        
        self.ShowFile_PB.clicked.connect(self.show_file_start) # shows first lines in the textbrowser
        self.ReadSets_PB.clicked.connect(self.read_set) # reads all files that start with lineEdit and creates a dict in the Sets_Dict[set][file][column]
        self.PlotFile_PB.clicked.connect(self.plotfile)
        self.MAV_slider.valueChanged.connect(self.mav_valuechanged)
        self.MAV_slider.sliderReleased.connect(self.mav_released)
        self.LP_slider.sliderReleased.connect(self.lp)
        self.LP_slider.valueChanged.connect(self.lp_valuechanged)
        self.HP_slider.sliderReleased.connect(self.hp)
        self.HP_slider.valueChanged.connect(self.hp_valuechanged)
        #self.CutZeros.clicked.connect(self.cut_zeros_filedict)
        self.PlotColumn_PB.clicked.connect(self.plotcolumn)
        self.Clear_PB.clicked.connect(self.clear)
        self.Export_PB.clicked.connect(self.export)
        self.FFT_PB.clicked.connect(self.fft)
        self.ReadLabBook.clicked.connect(self.readlabbook)
        self.MAVEdit.returnPressed.connect(self.mav_released)
        self.MVAREdit.returnPressed.connect(self.mvar)
        self.MMMINEdit.returnPressed.connect(self.mmmin)
        self.Corr_PB.clicked.connect(self.correlate)
        self.Select_PB.clicked.connect(self.open_filedialog)  
        self.Pyro_PB.clicked.connect(self.read_pyro)
        
        self.Sets_Dict = dict() # contains [set1][file1][column1] - the data
        self.Files_Dict = dict() # contains [filename 1]: 'set-filename' 
        self.Columns_Dict = dict() # contains[set-filename-column]: same
        
    def read_pyro(self):
        print 'read_pyro'
        filelist = list()
        filelist = [f for f in os.listdir(self.directory) if f.startswith(self.lineEdit.text())]
        print filelist
        filelist = [os.path.join(self.directory, f) for f in filelist]
        cols_of_interest = [str(c).rstrip(' ').lstrip(' ') for c in self.ColsOfInterestEdit.text().split(',')]
        print cols_of_interest
        self.Sets_Dict[str(self.lineEdit.text())] = self.datreader.read_pyro(filelist, cols_of_interest)
        #self.cut_zeros_filedict()
        self.update_SetScroll()
        self.update_Files_Dict() 
        self.update_FileScroll()
        self.update_Columns_Dict()
        self.update_ColumnScroll()
        print self.Sets_Dict.keys()
        
        
    def open_filedialog(self):
        files = str(QtGui.QFileDialog.getOpenFileName(None, QtCore.QString('Select File'), QtCore.QString(os.getcwd()),QtCore.QString('*.txt')))
        print files
        self.lineEdit.setText(os.path.basename(files))
        self.WorkingD_label.setText(os.path.dirname(files))
        self.directory = os.path.dirname(files)
        
    def correlate(self):
        fnum = self.Plotter.plot_eval(self.Plotter.correlate, 0, int(self.CurrentFigureEdit.text()), self.InActiveFigure.isChecked(), self.SelectedRange.isChecked(), self.SubtractMean_PB.isChecked())
        self.CurrentFigureEdit.setText(str(fnum))
        
    def readlabbook(self):
        #self.HistoryEdit.insertPlainText(self.HistoryEdit.text())
        print 'read labbook'
        lab_dict = self.datreader.get_labdict(str(self.lineEdit.text()))
        filelist = lab_dict.keys()
        print filelist
        path = self.directory
        filelist = [os.path.join(path, f) for f in filelist if f in os.listdir(path)]
        print filelist
        cols_of_interest = [str(c).rstrip(' ').lstrip(' ') for c in self.ColsOfInterestEdit.text().split(',')]
        print cols_of_interest
        self.Sets_Dict[str(self.lineEdit.text())] = self.datreader.read_files(filelist, cols_of_interest)
        #self.cut_zeros_filedict()
        lab_dict = self.datreader.get_labdict(str(self.lineEdit.text()))
        for f in self.Sets_Dict[str(self.lineEdit.text())].keys():
            for info in lab_dict[f].keys():
                self.Sets_Dict[str(self.lineEdit.text())][f][info] = lab_dict[f][info]
        self.update_SetScroll()
        self.update_Files_Dict() 
        self.update_FileScroll()
        self.update_Columns_Dict()
        self.update_ColumnScroll()
        print self.Sets_Dict.keys()
    
    def mvar(self):
        fnum = self.Plotter.plot_eval(self.Plotter.mvar, int(self.MVAREdit.text()), int(self.CurrentFigureEdit.text()), self.InActiveFigure.isChecked(), self.SelectedRange.isChecked(), self.SubtractMean_PB.isChecked())
        self.CurrentFigureEdit.setText(str(fnum))
        
    def mmmin(self):
        fnum = self.Plotter.plot_eval(self.Plotter.mmmin, int(self.MMMINEdit.text()), int(self.CurrentFigureEdit.text()), self.InActiveFigure.isChecked(), self.SelectedRange.isChecked(), self.SubtractMean_PB.isChecked())
        self.CurrentFigureEdit.setText(str(fnum))
        
        
    def mav_released(self):
        #if not self.InActiveFigure.isChecked():
         #   self.MAVEdit.setText(str(self.MAV_slider.value())) 
        fnum = self.Plotter.plot_eval(self.Plotter.mav, int(self.MAVEdit.text()), int(self.CurrentFigureEdit.text()), self.InActiveFigure.isChecked(), self.SelectedRange.isChecked(), self.SubtractMean_PB.isChecked())
        self.CurrentFigureEdit.setText(str(fnum))
        
    def fft(self):
        print 'fft'
        fnum = self.Plotter.plot_eval(self.Plotter.fft, 0, int(self.CurrentFigureEdit.text()), self.InActiveFigure.isChecked(), self.SelectedRange.isChecked(), self.SubtractMean_PB.isChecked())
        self.CurrentFigureEdit.setText(str(fnum))
    
    def export(self):
        self.Plotter.export(int(self.CurrentFigureEdit.text()))
        
        
    def clear(self):
        self.Sets_Dict = dict()
        self.update_SetScroll()
        self.Files_Dict = dict()
        self.update_FileScroll()
        self.Columns_Dict = dict()
        self.update_ColumnScroll()
        
    def lp_valuechanged(self):
        self.LPEdit.setText(str(self.LP_slider.value()))       
       
    def lp(self):
        print 'mav'
        self.MAVEdit.setText(str(self.LP_slider.value()))
        
    def hp_valuechanged(self):
        self.HPEdit.setText(str(self.HP_slider.value()))       
       
    def hp(self):
        print 'mav'
        self.MAVEdit.setText(str(self.HP_slider.value()))
        
    def mav_valuechanged(self):
        self.MAVEdit.setText(str(self.MAV_slider.value()))
        if self.InActiveFigure.isChecked():
            fnum = self.Plotter.plot_eval(self.Plotter.mav, int(self.MAVEdit.text()), int(self.CurrentFigureEdit.text()), self.InActiveFigure.isChecked(), self.SelectedRange.isChecked(), self.SubtractMean_PB.isChecked())
            self.CurrentFigureEdit.setText(str(fnum))

    def plotcolumn(self):
        for col in self.ColumnScroll.selectedItems():
            key = str(col.text()).split('::')
            col_data = self.Sets_Dict[key[0]][key[1]][key[2]]
            x_axis = self.Sets_Dict[key[0]][key[1]]['Zeit']
            label = str(col.text()+ '')
            self.Plotter.plot_column(x_axis, col_data, int(self.CurrentFigureEdit.text()), label)
        
#    def cut_zeros_filedict(self):
#        print 'cut_zeros_filedict'
#        if self.CutZeros.isChecked() == True:
#            print 'checked'
#            for fd in self.Files_Dict.keys():
#                self.Files_Dict[fd] = self.datreader.cutzeros_file_dict(self.Files_Dict[fd])
                
        
    def plotfile(self):
        for f in self.FileScroll.selectedItems():
            key = str(f.text()).split('::')
            print key
            title = str(f.text()) 
            self.Plotter.plot_file(self.Sets_Dict[key[0]][key[1]], [ str(c).rstrip(' ').lstrip(' ') for c in self.ColsOfInterestEdit.text().split(',')], int(self.CurrentFigureEdit.text()), title)
            

    def read_set(self):
        print 'read_set'
        filelist = list()
        filelist = [f for f in os.listdir(self.directory) if f.startswith(self.lineEdit.text())]
        print filelist
        filelist = [os.path.join(self.directory, f) for f in filelist]
        cols_of_interest = [str(c).rstrip(' ').lstrip(' ') for c in self.ColsOfInterestEdit.text().split(',')]
        print cols_of_interest
        self.Sets_Dict[str(self.lineEdit.text())] = self.datreader.read_files(filelist, cols_of_interest)
        #self.cut_zeros_filedict()
        self.update_SetScroll()
        self.update_Files_Dict() 
        self.update_FileScroll()
        self.update_Columns_Dict()
        self.update_ColumnScroll()
        print self.Sets_Dict.keys()
        
    def update_ColumnScroll(self):
        print 'update_ColumnScroll'
        self.ColumnScroll.clear()
        for col in self.Columns_Dict.keys():
            item = QtGui.QListWidgetItem()
            item.setText(col)
            self.ColumnScroll.addItem(item)
                
            
    def update_Columns_Dict(self):
        print 'update_FilesDict'
        cols_of_interest = [str(c).rstrip(' ').lstrip(' ') for c in self.ColsOfInterestEdit.text().split(',')]
        for s in self.Sets_Dict.keys(): # sets
            for f in self.Sets_Dict[s].keys(): #files
                for c in self.Sets_Dict[s][f].keys():
                    if c in cols_of_interest:
                        self.Columns_Dict[s + '::' + f + '::' + c] = s + '::' + f + '::' + c
        
    def update_Files_Dict(self):
        print 'update_FilesDict'
        for s in self.Sets_Dict.keys(): # sets
            print s
            for f in self.Sets_Dict[s].keys(): #files
                print f
                self.Files_Dict[f] = str(s) + '::'+ str(f)
        #self.cut_zeros_filedict()
                
        
    def update_SetScroll(self):
        print 'update_SetScroll'
        self.SetScroll.clear()
        for key in self.Sets_Dict.keys():
            item = QtGui.QListWidgetItem()
            item.setText(str(key))
            self.SetScroll.addItem(item)
        
    def update_FileScroll(self):
        print 'update_FileScroll'
        self.FileScroll.clear()
        for key in self.Files_Dict.keys():
            item = QtGui.QListWidgetItem()
            item.setText(str(self.Files_Dict[key]))
            self.FileScroll.addItem(item)

    def show_file_start(self):
        try:
            f = open(self.lineEdit.text())
            s= ''
            for i in range(12):
                s = s+f.readline()
            self.textBrowser.setText(s)
        except:
            print 'Error in file read'
        
        
        
#if __name__ == '__main__':
app = QtGui.QApplication(sys.argv) 
dialog = MeinDialog() 
dialog.show() 
#sys.exit(app.exec_())