# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_windowNew.ui'
#
# Created: Fri Apr  5 19:24:26 2013
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainGuiWin(object):
    def setupUi(self, MainGuiWin):
        MainGuiWin.setObjectName("MainGuiWin")
        MainGuiWin.resize(728, 724)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainGuiWin.sizePolicy().hasHeightForWidth())
        MainGuiWin.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(MainGuiWin)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.preprocessing_box = QtWidgets.QGroupBox(self.centralwidget)
        self.preprocessing_box.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.preprocessing_box.sizePolicy().hasHeightForWidth())
        self.preprocessing_box.setSizePolicy(sizePolicy)
        self.preprocessing_box.setCheckable(False)
        self.preprocessing_box.setObjectName("preprocessing_box")
        self.formLayout = QtWidgets.QFormLayout(self.preprocessing_box)
        self.formLayout.setFieldGrowthPolicy(QtWidgets.QFormLayout.FieldsStayAtSizeHint)
        self.formLayout.setObjectName("formLayout")
        self.label_3 = QtWidgets.QLabel(self.preprocessing_box)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.lowpass_spinner = QtWidgets.QSpinBox(self.preprocessing_box)
        self.lowpass_spinner.setMinimum(0)
        self.lowpass_spinner.setMaximum(10)
        self.lowpass_spinner.setProperty("value", 0)
        self.lowpass_spinner.setObjectName("lowpass_spinner")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lowpass_spinner)
        self.label_4 = QtWidgets.QLabel(self.preprocessing_box)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.highpass_spinner = QtWidgets.QSpinBox(self.preprocessing_box)
        self.highpass_spinner.setMinimum(0)
        self.highpass_spinner.setMaximum(10)
        self.highpass_spinner.setProperty("value", 0)
        self.highpass_spinner.setObjectName("highpass_spinner")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.highpass_spinner)
        self.label_5 = QtWidgets.QLabel(self.preprocessing_box)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.spatial_spinner = QtWidgets.QSpinBox(self.preprocessing_box)
        self.spatial_spinner.setMinimum(1)
        self.spatial_spinner.setMaximum(4)
        self.spatial_spinner.setObjectName("spatial_spinner")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.spatial_spinner)
        self.preprocess_button = QtWidgets.QPushButton(self.preprocessing_box)
        self.preprocess_button.setObjectName("preprocess_button")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.SpanningRole, self.preprocess_button)
        self.verticalLayout_2.addWidget(self.preprocessing_box)
        self.factorize_box = QtWidgets.QGroupBox(self.centralwidget)
        self.factorize_box.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.factorize_box.sizePolicy().hasHeightForWidth())
        self.factorize_box.setSizePolicy(sizePolicy)
        self.factorize_box.setObjectName("factorize_box")
        self.formLayout_3 = QtWidgets.QFormLayout(self.factorize_box)
        self.formLayout_3.setFieldGrowthPolicy(QtWidgets.QFormLayout.FieldsStayAtSizeHint)
        self.formLayout_3.setObjectName("formLayout_3")
        self.label_8 = QtWidgets.QLabel(self.factorize_box)
        self.label_8.setObjectName("label_8")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.n_modes_spinner = QtWidgets.QSpinBox(self.factorize_box)
        self.n_modes_spinner.setMinimum(1)
        self.n_modes_spinner.setMaximum(1000)
        self.n_modes_spinner.setObjectName("n_modes_spinner")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.n_modes_spinner)
        self.label_7 = QtWidgets.QLabel(self.factorize_box)
        self.label_7.setObjectName("label_7")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.methods_box = QtWidgets.QComboBox(self.factorize_box)
        self.methods_box.setObjectName("methods_box")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.methods_box)
        self.sparseness_label = QtWidgets.QLabel(self.factorize_box)
        self.sparseness_label.setObjectName("sparseness_label")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.sparseness_label)
        self.sparseness_spinner = QtWidgets.QDoubleSpinBox(self.factorize_box)
        self.sparseness_spinner.setObjectName("sparseness_spinner")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.sparseness_spinner)
        self.smoothness_label = QtWidgets.QLabel(self.factorize_box)
        self.smoothness_label.setObjectName("smoothness_label")
        self.formLayout_3.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.smoothness_label)
        self.smoothness_spinner = QtWidgets.QDoubleSpinBox(self.factorize_box)
        self.smoothness_spinner.setObjectName("smoothness_spinner")
        self.formLayout_3.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.smoothness_spinner)
        self.maxcount_label = QtWidgets.QLabel(self.factorize_box)
        self.maxcount_label.setObjectName("maxcount_label")
        self.formLayout_3.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.maxcount_label)
        self.maxcount_spinner = QtWidgets.QSpinBox(self.factorize_box)
        self.maxcount_spinner.setProperty("value", 30)
        self.maxcount_spinner.setObjectName("maxcount_spinner")
        self.formLayout_3.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.maxcount_spinner)
        self.factorize_label = QtWidgets.QLabel(self.factorize_box)
        self.factorize_label.setStyleSheet("QLabel {color : red; }")
        self.factorize_label.setText("")
        self.factorize_label.setObjectName("factorize_label")
        self.formLayout_3.setWidget(5, QtWidgets.QFormLayout.SpanningRole, self.factorize_label)
        self.factorize_button = QtWidgets.QPushButton(self.factorize_box)
        self.factorize_button.setObjectName("factorize_button")
        self.formLayout_3.setWidget(6, QtWidgets.QFormLayout.SpanningRole, self.factorize_button)
        self.verticalLayout_2.addWidget(self.factorize_box)
        self.export_box = QtWidgets.QGroupBox(self.centralwidget)
        self.export_box.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.export_box.sizePolicy().hasHeightForWidth())
        self.export_box.setSizePolicy(sizePolicy)
        self.export_box.setObjectName("export_box")
        self.formLayout_4 = QtWidgets.QFormLayout(self.export_box)
        self.formLayout_4.setFieldGrowthPolicy(QtWidgets.QFormLayout.FieldsStayAtSizeHint)
        self.formLayout_4.setObjectName("formLayout_4")
        self.label_12 = QtWidgets.QLabel(self.export_box)
        self.label_12.setObjectName("label_12")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_12)
        self.format_box = QtWidgets.QComboBox(self.export_box)
        self.format_box.setObjectName("format_box")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.format_box)
        self.plot_export_button = QtWidgets.QPushButton(self.export_box)
        self.plot_export_button.setEnabled(False)
        self.plot_export_button.setObjectName("plot_export_button")
        self.formLayout_4.setWidget(1, QtWidgets.QFormLayout.SpanningRole, self.plot_export_button)
        self.verticalLayout_2.addWidget(self.export_box)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.session_box = QtWidgets.QComboBox(self.centralwidget)
        self.session_box.setEnabled(False)
        self.session_box.setObjectName("session_box")
        self.gridLayout.addWidget(self.session_box, 1, 0, 1, 1)
        self.session_label = QtWidgets.QLabel(self.centralwidget)
        self.session_label.setObjectName("session_label")
        self.gridLayout.addWidget(self.session_label, 0, 0, 1, 1)
        self.plot_selection_label = QtWidgets.QLabel(self.centralwidget)
        self.plot_selection_label.setObjectName("plot_selection_label")
        self.gridLayout.addWidget(self.plot_selection_label, 0, 1, 1, 1)
        self.plot_threshold_label = QtWidgets.QLabel(self.centralwidget)
        self.plot_threshold_label.setObjectName("plot_threshold_label")
        self.gridLayout.addWidget(self.plot_threshold_label, 0, 2, 1, 1)
        self.plot_threshold_box = QtWidgets.QComboBox(self.centralwidget)
        self.plot_threshold_box.setEnabled(False)
        self.plot_threshold_box.setObjectName("plot_threshold_box")
        self.gridLayout.addWidget(self.plot_threshold_box, 1, 2, 1, 1)
        self.plot_selection_box = QtWidgets.QComboBox(self.centralwidget)
        self.plot_selection_box.setEnabled(False)
        self.plot_selection_box.setObjectName("plot_selection_box")
        self.gridLayout.addWidget(self.plot_selection_box, 1, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 453, 597))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)
        self.verticalLayout.addWidget(self.scrollArea)
        self.horizontalLayout.addLayout(self.verticalLayout)
        MainGuiWin.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainGuiWin)
        self.statusbar.setObjectName("statusbar")
        MainGuiWin.setStatusBar(self.statusbar)
        self.menuBar = QtWidgets.QMenuBar(MainGuiWin)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 728, 25))
        self.menuBar.setObjectName("menuBar")
        self.menuFile = QtWidgets.QMenu(self.menuBar)
        self.menuFile.setObjectName("menuFile")
        MainGuiWin.setMenuBar(self.menuBar)
        self.actionLoad = QtWidgets.QAction(MainGuiWin)
        self.actionLoad.setObjectName("actionLoad")
        self.actionSave = QtWidgets.QAction(MainGuiWin)
        self.actionSave.setObjectName("actionSave")
        self.menuFile.addAction(self.actionLoad)
        self.menuFile.addAction(self.actionSave)
        self.menuBar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainGuiWin)
        QtCore.QMetaObject.connectSlotsByName(MainGuiWin)

    def retranslateUi(self, MainGuiWin):
        MainGuiWin.setWindowTitle(QtCore.QCoreApplication.translate("MainGuiWin", "MainWindow", None))
        self.preprocessing_box.setTitle(QtCore.QCoreApplication.translate("MainGuiWin", "preprocessing", None))
        self.label_3.setText(QtCore.QCoreApplication.translate("MainGuiWin", "lowpass:", None))
        self.label_4.setText(QtCore.QCoreApplication.translate("MainGuiWin", "highpass", None))
        self.label_5.setText(QtCore.QCoreApplication.translate("MainGuiWin", "spatial down:", None))
        self.preprocess_button.setText(QtCore.QCoreApplication.translate("MainGuiWin", "Preprocess", None))
        self.factorize_box.setTitle(QtCore.QCoreApplication.translate("MainGuiWin", "factorization", None))
        self.label_8.setText(QtCore.QCoreApplication.translate("MainGuiWin", "n_modes", None))
        self.label_7.setText(QtCore.QCoreApplication.translate("MainGuiWin", "method", None))
        self.sparseness_label.setText(QtCore.QCoreApplication.translate("MainGuiWin", "sparseness", None))
        self.smoothness_label.setText(QtCore.QCoreApplication.translate("MainGuiWin", "smoothness", None))
        self.maxcount_label.setText(QtCore.QCoreApplication.translate("MainGuiWin", "maxcount", None))
        self.factorize_button.setText(QtCore.QCoreApplication.translate("MainGuiWin", "Factorize", None))
        self.export_box.setTitle(QtCore.QCoreApplication.translate("MainGuiWin", "export", None))
        self.label_12.setText(QtCore.QCoreApplication.translate("MainGuiWin", "format", None))
        self.plot_export_button.setText(QtCore.QCoreApplication.translate("MainGuiWin", "Export Plots and Factorization", None))
        self.session_label.setText(QtCore.QCoreApplication.translate("MainGuiWin", "session", None))
        self.plot_selection_label.setText(QtCore.QCoreApplication.translate("MainGuiWin", "plot", None))
        self.plot_threshold_label.setText(QtCore.QCoreApplication.translate("MainGuiWin", "threshold", None))
        self.menuFile.setTitle(QtCore.QCoreApplication.translate("MainGuiWin", "File", None))
        self.actionLoad.setText(QtCore.QCoreApplication.translate("MainGuiWin", "load", None))
        self.actionSave.setText(QtCore.QCoreApplication.translate("MainGuiWin", "save", None))

