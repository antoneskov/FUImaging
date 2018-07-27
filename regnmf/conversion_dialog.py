# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'conversion_dialog.ui'
#
# Created: Wed Oct  3 15:38:47 2012
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_conversion_dialog(object):
    def setupUi(self, conversion_dialog):
        conversion_dialog.setObjectName("conversion_dialog")
        conversion_dialog.setWindowModality(QtCore.Qt.NonModal)
        conversion_dialog.resize(284, 199)
        conversion_dialog.setModal(True)
        self.formLayout = QtWidgets.QFormLayout(conversion_dialog)
        self.formLayout.setFieldGrowthPolicy(QtWidgets.QFormLayout.FieldsStayAtSizeHint)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(conversion_dialog)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.SpanningRole, self.label)
        self.label_2 = QtWidgets.QLabel(conversion_dialog)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.buttonBox = QtWidgets.QDialogButtonBox(conversion_dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonBox.sizePolicy().hasHeightForWidth())
        self.buttonBox.setSizePolicy(sizePolicy)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.SpanningRole, self.buttonBox)
        self.stimulus_on_box = QtWidgets.QSpinBox(conversion_dialog)
        self.stimulus_on_box.setMaximum(1000000)
        self.stimulus_on_box.setProperty("value", 8)
        self.stimulus_on_box.setObjectName("stimulus_on_box")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.stimulus_on_box)
        self.stimulus_end_box = QtWidgets.QSpinBox(conversion_dialog)
        self.stimulus_end_box.setMaximum(1000000)
        self.stimulus_end_box.setProperty("value", 16)
        self.stimulus_end_box.setObjectName("stimulus_end_box")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.stimulus_end_box)
        self.label_3 = QtWidgets.QLabel(conversion_dialog)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.label_4 = QtWidgets.QLabel(conversion_dialog)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.framerate_box = QtWidgets.QDoubleSpinBox(conversion_dialog)
        self.framerate_box.setMaximum(100000.0)
        self.framerate_box.setSingleStep(0.1)
        self.framerate_box.setProperty("value", 4.0)
        self.framerate_box.setObjectName("framerate_box")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.framerate_box)

        self.retranslateUi(conversion_dialog)
        self.buttonBox.accepted.connect(conversion_dialog.accept)
        self.buttonBox.rejected.connect(conversion_dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(conversion_dialog)

    def retranslateUi(self, conversion_dialog):
        conversion_dialog.setWindowTitle(QtCore.QCoreApplication.translate("conversion_dialog", "Dialog", None))
        self.label.setText(QtCore.QCoreApplication.translate("conversion_dialog", "bla", None))
        self.label_2.setText(QtCore.QCoreApplication.translate("conversion_dialog", "framerate", None))
        self.label_3.setText(QtCore.QCoreApplication.translate("conversion_dialog", "stimulus onset (frame)", None))
        self.label_4.setText(QtCore.QCoreApplication.translate("conversion_dialog", "stimulus end (frame)", None))

