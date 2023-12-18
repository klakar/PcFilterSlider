# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pc_filter_slider_dockwidget_base.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_pcFilterSliderDockWidgetBase(object):
    def setupUi(self, pcFilterSliderDockWidgetBase):
        pcFilterSliderDockWidgetBase.setObjectName("pcFilterSliderDockWidgetBase")
        pcFilterSliderDockWidgetBase.resize(403, 740)
        self.dockWidgetContents = QtWidgets.QWidget()
        self.dockWidgetContents.setObjectName("dockWidgetContents")
        self.gridLayout = QtWidgets.QGridLayout(self.dockWidgetContents)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.lblPointCloudLayer = QtWidgets.QLabel(self.dockWidgetContents)
        self.lblPointCloudLayer.setObjectName("lblPointCloudLayer")
        self.verticalLayout.addWidget(self.lblPointCloudLayer)
        self.cmbPointCloudLayer = QtWidgets.QComboBox(self.dockWidgetContents)
        self.cmbPointCloudLayer.setObjectName("cmbPointCloudLayer")
        self.verticalLayout.addWidget(self.cmbPointCloudLayer)
        self.lblAttribute = QtWidgets.QLabel(self.dockWidgetContents)
        self.lblAttribute.setObjectName("lblAttribute")
        self.verticalLayout.addWidget(self.lblAttribute)
        self.cmbAttribute = QtWidgets.QComboBox(self.dockWidgetContents)
        self.cmbAttribute.setObjectName("cmbAttribute")
        self.verticalLayout.addWidget(self.cmbAttribute)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem)
        self.lblMaxThickness = QtWidgets.QLabel(self.dockWidgetContents)
        self.lblMaxThickness.setObjectName("lblMaxThickness")
        self.horizontalLayout_5.addWidget(self.lblMaxThickness)
        self.lblMaxThicknessValue = QtWidgets.QLabel(self.dockWidgetContents)
        self.lblMaxThicknessValue.setObjectName("lblMaxThicknessValue")
        self.horizontalLayout_5.addWidget(self.lblMaxThicknessValue)
        self.verticalLayout_5.addLayout(self.horizontalLayout_5)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem1)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem2)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lblSliceThickness = QtWidgets.QLabel(self.dockWidgetContents)
        self.lblSliceThickness.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lblSliceThickness.setObjectName("lblSliceThickness")
        self.verticalLayout_2.addWidget(self.lblSliceThickness)
        self.lblThickness = QtWidgets.QLabel(self.dockWidgetContents)
        self.lblThickness.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lblThickness.setObjectName("lblThickness")
        self.verticalLayout_2.addWidget(self.lblThickness)
        self.horizontalLayout_9.addLayout(self.verticalLayout_2)
        self.verticalLayout_5.addLayout(self.horizontalLayout_9)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem3)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem4)
        self.lblMinThickness = QtWidgets.QLabel(self.dockWidgetContents)
        self.lblMinThickness.setObjectName("lblMinThickness")
        self.horizontalLayout_6.addWidget(self.lblMinThickness)
        self.lblMinThicknessValue = QtWidgets.QLabel(self.dockWidgetContents)
        self.lblMinThicknessValue.setObjectName("lblMinThicknessValue")
        self.horizontalLayout_6.addWidget(self.lblMinThicknessValue)
        self.verticalLayout_5.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_2.addLayout(self.verticalLayout_5)
        self.sliderThickness = QtWidgets.QSlider(self.dockWidgetContents)
        self.sliderThickness.setProperty("value", 99)
        self.sliderThickness.setOrientation(QtCore.Qt.Vertical)
        self.sliderThickness.setObjectName("sliderThickness")
        self.horizontalLayout_2.addWidget(self.sliderThickness)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem5)
        self.lblMaxCutoff = QtWidgets.QLabel(self.dockWidgetContents)
        self.lblMaxCutoff.setObjectName("lblMaxCutoff")
        self.horizontalLayout_3.addWidget(self.lblMaxCutoff)
        self.lblMaxCutoffValue = QtWidgets.QLabel(self.dockWidgetContents)
        self.lblMaxCutoffValue.setObjectName("lblMaxCutoffValue")
        self.horizontalLayout_3.addWidget(self.lblMaxCutoffValue)
        self.verticalLayout_4.addLayout(self.horizontalLayout_3)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem6)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem7)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.lblLowCutoff = QtWidgets.QLabel(self.dockWidgetContents)
        self.lblLowCutoff.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lblLowCutoff.setObjectName("lblLowCutoff")
        self.verticalLayout_3.addWidget(self.lblLowCutoff)
        self.lblCutoff = QtWidgets.QLabel(self.dockWidgetContents)
        self.lblCutoff.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lblCutoff.setObjectName("lblCutoff")
        self.verticalLayout_3.addWidget(self.lblCutoff)
        self.horizontalLayout_10.addLayout(self.verticalLayout_3)
        self.verticalLayout_4.addLayout(self.horizontalLayout_10)
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem8)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem9)
        self.lblMinCutoff = QtWidgets.QLabel(self.dockWidgetContents)
        self.lblMinCutoff.setObjectName("lblMinCutoff")
        self.horizontalLayout_4.addWidget(self.lblMinCutoff)
        self.lblStartValue = QtWidgets.QLabel(self.dockWidgetContents)
        self.lblStartValue.setObjectName("lblStartValue")
        self.horizontalLayout_4.addWidget(self.lblStartValue)
        self.verticalLayout_4.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_2.addLayout(self.verticalLayout_4)
        self.sliderCutoff = QtWidgets.QSlider(self.dockWidgetContents)
        self.sliderCutoff.setOrientation(QtCore.Qt.Vertical)
        self.sliderCutoff.setObjectName("sliderCutoff")
        self.horizontalLayout_2.addWidget(self.sliderCutoff)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.gridLayout.addLayout(self.verticalLayout, 3, 0, 1, 1)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.chkActive = QtWidgets.QCheckBox(self.dockWidgetContents)
        self.chkActive.setObjectName("chkActive")
        self.horizontalLayout_8.addWidget(self.chkActive)
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem10)
        self.btnReset = QtWidgets.QPushButton(self.dockWidgetContents)
        self.btnReset.setObjectName("btnReset")
        self.horizontalLayout_8.addWidget(self.btnReset)
        self.gridLayout.addLayout(self.horizontalLayout_8, 1, 0, 1, 1)
        pcFilterSliderDockWidgetBase.setWidget(self.dockWidgetContents)

        self.retranslateUi(pcFilterSliderDockWidgetBase)
        QtCore.QMetaObject.connectSlotsByName(pcFilterSliderDockWidgetBase)

    def retranslateUi(self, pcFilterSliderDockWidgetBase):
        _translate = QtCore.QCoreApplication.translate
        pcFilterSliderDockWidgetBase.setWindowTitle(_translate("pcFilterSliderDockWidgetBase", "Point Cloud Filter Slider"))
        self.lblPointCloudLayer.setText(_translate("pcFilterSliderDockWidgetBase", "Point Cloud Layer"))
        self.lblAttribute.setText(_translate("pcFilterSliderDockWidgetBase", "Attribute"))
        self.lblMaxThickness.setText(_translate("pcFilterSliderDockWidgetBase", "Max"))
        self.lblMaxThicknessValue.setText(_translate("pcFilterSliderDockWidgetBase", "100"))
        self.lblSliceThickness.setText(_translate("pcFilterSliderDockWidgetBase", "Thickness"))
        self.lblThickness.setText(_translate("pcFilterSliderDockWidgetBase", "1"))
        self.lblMinThickness.setText(_translate("pcFilterSliderDockWidgetBase", "Min"))
        self.lblMinThicknessValue.setText(_translate("pcFilterSliderDockWidgetBase", "0"))
        self.lblMaxCutoff.setText(_translate("pcFilterSliderDockWidgetBase", "Max"))
        self.lblMaxCutoffValue.setText(_translate("pcFilterSliderDockWidgetBase", "100"))
        self.lblLowCutoff.setText(_translate("pcFilterSliderDockWidgetBase", "Cutoff"))
        self.lblCutoff.setText(_translate("pcFilterSliderDockWidgetBase", "50"))
        self.lblMinCutoff.setText(_translate("pcFilterSliderDockWidgetBase", "Min"))
        self.lblStartValue.setText(_translate("pcFilterSliderDockWidgetBase", "0"))
        self.chkActive.setText(_translate("pcFilterSliderDockWidgetBase", "Activate"))
        self.btnReset.setText(_translate("pcFilterSliderDockWidgetBase", "Reset"))
