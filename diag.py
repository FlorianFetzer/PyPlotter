# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Desktop\qt\Pyplotter\diag.ui'
#
# Created: Tue Mar 25 15:06:01 2014
#      by: PyQt4 UI code generator 4.9.5
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(954, 592)
        self.OK_PB = QtGui.QPushButton(Dialog)
        self.OK_PB.setGeometry(QtCore.QRect(20, 550, 75, 23))
        self.OK_PB.setAutoDefault(True)
        self.OK_PB.setDefault(True)
        self.OK_PB.setObjectName(_fromUtf8("OK_PB"))
        self.Abbr_PB = QtGui.QPushButton(Dialog)
        self.Abbr_PB.setGeometry(QtCore.QRect(100, 550, 75, 23))
        self.Abbr_PB.setObjectName(_fromUtf8("Abbr_PB"))
        self.groupBox = QtGui.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(20, 10, 631, 271))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.lineEdit = QtGui.QLineEdit(self.groupBox)
        self.lineEdit.setGeometry(QtCore.QRect(2, 30, 131, 20))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.PlotSets_PB = QtGui.QPushButton(self.groupBox)
        self.PlotSets_PB.setGeometry(QtCore.QRect(140, 150, 75, 23))
        self.PlotSets_PB.setObjectName(_fromUtf8("PlotSets_PB"))
        self.ReadSets_PB = QtGui.QPushButton(self.groupBox)
        self.ReadSets_PB.setGeometry(QtCore.QRect(20, 90, 101, 23))
        self.ReadSets_PB.setObjectName(_fromUtf8("ReadSets_PB"))
        self.PlotColumn_PB = QtGui.QPushButton(self.groupBox)
        self.PlotColumn_PB.setGeometry(QtCore.QRect(420, 150, 75, 23))
        self.PlotColumn_PB.setObjectName(_fromUtf8("PlotColumn_PB"))
        self.ReadLabBook = QtGui.QPushButton(self.groupBox)
        self.ReadLabBook.setGeometry(QtCore.QRect(20, 60, 101, 23))
        self.ReadLabBook.setObjectName(_fromUtf8("ReadLabBook"))
        self.label_6 = QtGui.QLabel(self.groupBox)
        self.label_6.setGeometry(QtCore.QRect(180, 10, 46, 13))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.label_7 = QtGui.QLabel(self.groupBox)
        self.label_7.setGeometry(QtCore.QRect(440, 10, 46, 13))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.label_8 = QtGui.QLabel(self.groupBox)
        self.label_8.setGeometry(QtCore.QRect(300, 10, 46, 13))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.ShowFile_PB = QtGui.QPushButton(self.groupBox)
        self.ShowFile_PB.setGeometry(QtCore.QRect(30, 120, 75, 23))
        self.ShowFile_PB.setObjectName(_fromUtf8("ShowFile_PB"))
        self.SetScroll = QtGui.QListWidget(self.groupBox)
        self.SetScroll.setGeometry(QtCore.QRect(140, 30, 121, 111))
        self.SetScroll.setSelectionMode(QtGui.QAbstractItemView.MultiSelection)
        self.SetScroll.setObjectName(_fromUtf8("SetScroll"))
        self.FileScroll = QtGui.QListWidget(self.groupBox)
        self.FileScroll.setGeometry(QtCore.QRect(270, 30, 141, 111))
        self.FileScroll.setSelectionMode(QtGui.QAbstractItemView.MultiSelection)
        self.FileScroll.setObjectName(_fromUtf8("FileScroll"))
        self.ColumnScroll = QtGui.QListWidget(self.groupBox)
        self.ColumnScroll.setGeometry(QtCore.QRect(420, 30, 201, 111))
        self.ColumnScroll.setSelectionMode(QtGui.QAbstractItemView.MultiSelection)
        self.ColumnScroll.setObjectName(_fromUtf8("ColumnScroll"))
        self.PlotFile_PB = QtGui.QPushButton(self.groupBox)
        self.PlotFile_PB.setGeometry(QtCore.QRect(270, 150, 75, 23))
        self.PlotFile_PB.setObjectName(_fromUtf8("PlotFile_PB"))
        self.ColsOfInterestEdit = QtGui.QLineEdit(self.groupBox)
        self.ColsOfInterestEdit.setGeometry(QtCore.QRect(130, 220, 291, 20))
        self.ColsOfInterestEdit.setObjectName(_fromUtf8("ColsOfInterestEdit"))
        self.label_10 = QtGui.QLabel(self.groupBox)
        self.label_10.setGeometry(QtCore.QRect(30, 220, 101, 20))
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.AverageSets = QtGui.QCheckBox(self.groupBox)
        self.AverageSets.setGeometry(QtCore.QRect(140, 180, 121, 21))
        self.AverageSets.setChecked(False)
        self.AverageSets.setObjectName(_fromUtf8("AverageSets"))
        self.Clear_PB = QtGui.QPushButton(self.groupBox)
        self.Clear_PB.setGeometry(QtCore.QRect(10, 150, 111, 31))
        self.Clear_PB.setObjectName(_fromUtf8("Clear_PB"))
        self.groupBox_2 = QtGui.QGroupBox(Dialog)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 290, 631, 171))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.FFT_PB = QtGui.QPushButton(self.groupBox_2)
        self.FFT_PB.setGeometry(QtCore.QRect(450, 80, 75, 23))
        self.FFT_PB.setObjectName(_fromUtf8("FFT_PB"))
        self.LP_slider = QtGui.QSlider(self.groupBox_2)
        self.LP_slider.setGeometry(QtCore.QRect(40, 80, 111, 19))
        self.LP_slider.setMaximum(10000)
        self.LP_slider.setOrientation(QtCore.Qt.Horizontal)
        self.LP_slider.setObjectName(_fromUtf8("LP_slider"))
        self.HP_slider = QtGui.QSlider(self.groupBox_2)
        self.HP_slider.setGeometry(QtCore.QRect(230, 80, 151, 19))
        self.HP_slider.setMaximum(10000)
        self.HP_slider.setOrientation(QtCore.Qt.Horizontal)
        self.HP_slider.setObjectName(_fromUtf8("HP_slider"))
        self.label = QtGui.QLabel(self.groupBox_2)
        self.label.setGeometry(QtCore.QRect(80, 100, 46, 13))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_3 = QtGui.QLabel(self.groupBox_2)
        self.label_3.setGeometry(QtCore.QRect(290, 100, 46, 13))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.MAV_slider = QtGui.QSlider(self.groupBox_2)
        self.MAV_slider.setGeometry(QtCore.QRect(140, 140, 160, 19))
        self.MAV_slider.setMaximum(1000)
        self.MAV_slider.setOrientation(QtCore.Qt.Horizontal)
        self.MAV_slider.setObjectName(_fromUtf8("MAV_slider"))
        self.label_5 = QtGui.QLabel(self.groupBox_2)
        self.label_5.setGeometry(QtCore.QRect(70, 140, 61, 20))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_2 = QtGui.QLabel(self.groupBox_2)
        self.label_2.setGeometry(QtCore.QRect(480, 20, 91, 20))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.CurrentFigureEdit = QtGui.QLineEdit(self.groupBox_2)
        self.CurrentFigureEdit.setGeometry(QtCore.QRect(580, 20, 31, 20))
        self.CurrentFigureEdit.setObjectName(_fromUtf8("CurrentFigureEdit"))
        self.LPEdit = QtGui.QLineEdit(self.groupBox_2)
        self.LPEdit.setGeometry(QtCore.QRect(160, 80, 31, 20))
        self.LPEdit.setObjectName(_fromUtf8("LPEdit"))
        self.HPEdit = QtGui.QLineEdit(self.groupBox_2)
        self.HPEdit.setGeometry(QtCore.QRect(390, 80, 31, 20))
        self.HPEdit.setObjectName(_fromUtf8("HPEdit"))
        self.InActiveFigure = QtGui.QCheckBox(self.groupBox_2)
        self.InActiveFigure.setGeometry(QtCore.QRect(310, 20, 141, 17))
        self.InActiveFigure.setChecked(True)
        self.InActiveFigure.setObjectName(_fromUtf8("InActiveFigure"))
        self.MAVEdit = QtGui.QLineEdit(self.groupBox_2)
        self.MAVEdit.setGeometry(QtCore.QRect(310, 140, 31, 20))
        self.MAVEdit.setObjectName(_fromUtf8("MAVEdit"))
        self.SelectedRange = QtGui.QCheckBox(self.groupBox_2)
        self.SelectedRange.setGeometry(QtCore.QRect(120, 20, 121, 17))
        self.SelectedRange.setObjectName(_fromUtf8("SelectedRange"))
        self.Export_PB = QtGui.QPushButton(self.groupBox_2)
        self.Export_PB.setGeometry(QtCore.QRect(500, 130, 121, 23))
        self.Export_PB.setObjectName(_fromUtf8("Export_PB"))
        self.SubtractMean_PB = QtGui.QCheckBox(self.groupBox_2)
        self.SubtractMean_PB.setGeometry(QtCore.QRect(540, 80, 101, 17))
        self.SubtractMean_PB.setObjectName(_fromUtf8("SubtractMean_PB"))
        self.groupBox_3 = QtGui.QGroupBox(Dialog)
        self.groupBox_3.setGeometry(QtCore.QRect(20, 470, 421, 71))
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.textBrowser = QtGui.QTextBrowser(Dialog)
        self.textBrowser.setGeometry(QtCore.QRect(660, 10, 291, 171))
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        self.label_9 = QtGui.QLabel(Dialog)
        self.label_9.setGeometry(QtCore.QRect(660, 200, 46, 13))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.HistoryEdit = QtGui.QPlainTextEdit(Dialog)
        self.HistoryEdit.setGeometry(QtCore.QRect(660, 230, 104, 71))
        self.HistoryEdit.setObjectName(_fromUtf8("HistoryEdit"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.OK_PB.setText(QtGui.QApplication.translate("Dialog", "ok", None, QtGui.QApplication.UnicodeUTF8))
        self.Abbr_PB.setText(QtGui.QApplication.translate("Dialog", "abbr", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("Dialog", "Read Data", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit.setText(QtGui.QApplication.translate("Dialog", "testdata/laborbuch.txt", None, QtGui.QApplication.UnicodeUTF8))
        self.PlotSets_PB.setText(QtGui.QApplication.translate("Dialog", "Plot Sets", None, QtGui.QApplication.UnicodeUTF8))
        self.ReadSets_PB.setText(QtGui.QApplication.translate("Dialog", "Read Set", None, QtGui.QApplication.UnicodeUTF8))
        self.PlotColumn_PB.setText(QtGui.QApplication.translate("Dialog", "Plot Column", None, QtGui.QApplication.UnicodeUTF8))
        self.ReadLabBook.setText(QtGui.QApplication.translate("Dialog", "Read from LabBook", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("Dialog", "Sets", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("Dialog", "Columns", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("Dialog", "Files", None, QtGui.QApplication.UnicodeUTF8))
        self.ShowFile_PB.setText(QtGui.QApplication.translate("Dialog", "Show File", None, QtGui.QApplication.UnicodeUTF8))
        self.PlotFile_PB.setText(QtGui.QApplication.translate("Dialog", "Plot File", None, QtGui.QApplication.UnicodeUTF8))
        self.ColsOfInterestEdit.setText(QtGui.QApplication.translate("Dialog", "Zeit, R-Raw, T-Raw, P-Raw, Refl, Temp, Plasma", None, QtGui.QApplication.UnicodeUTF8))
        self.label_10.setText(QtGui.QApplication.translate("Dialog", "Columns of interest", None, QtGui.QApplication.UnicodeUTF8))
        self.AverageSets.setText(QtGui.QApplication.translate("Dialog", "Average over Set", None, QtGui.QApplication.UnicodeUTF8))
        self.Clear_PB.setText(QtGui.QApplication.translate("Dialog", "Clear All", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("Dialog", "Eval Data", None, QtGui.QApplication.UnicodeUTF8))
        self.FFT_PB.setText(QtGui.QApplication.translate("Dialog", "FFT", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Dialog", "Low Pass", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Dialog", "High Pass", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("Dialog", "Moving Avg.", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Dialog", "active Data Figure", None, QtGui.QApplication.UnicodeUTF8))
        self.CurrentFigureEdit.setText(QtGui.QApplication.translate("Dialog", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.InActiveFigure.setText(QtGui.QApplication.translate("Dialog", "Apply in Current Figure", None, QtGui.QApplication.UnicodeUTF8))
        self.SelectedRange.setText(QtGui.QApplication.translate("Dialog", "Use Selected range", None, QtGui.QApplication.UnicodeUTF8))
        self.Export_PB.setText(QtGui.QApplication.translate("Dialog", "export Plotted Data", None, QtGui.QApplication.UnicodeUTF8))
        self.SubtractMean_PB.setText(QtGui.QApplication.translate("Dialog", "subtract mean", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_3.setTitle(QtGui.QApplication.translate("Dialog", "Save Data", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setText(QtGui.QApplication.translate("Dialog", "History", None, QtGui.QApplication.UnicodeUTF8))
        self.HistoryEdit.setPlainText(QtGui.QApplication.translate("Dialog", "asAS", None, QtGui.QApplication.UnicodeUTF8))

