# -*- coding: utf-8 -*-
"""
/***************************************************************************
 pcFilterSlider
                                 A QGIS plugin
 GUI panel to change values in simple query builder filter for point clouds.
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                              -------------------
        begin                : 2023-12-17
        git sha              : $Format:%H$
        copyright            : (C) 2023 by Klas Karlsson
        email                : klas.karlsson@geosupportsystem.se
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""
from qgis.PyQt.QtCore import QSettings, QTranslator, QCoreApplication, Qt
from qgis.PyQt.QtGui import QIcon
from qgis.PyQt.QtWidgets import QAction
# Initialize Qt resources from file resources.py
from .resources import *

# Import the code for the DockWidget
from .pc_filter_slider_dockwidget import pcFilterSliderDockWidget
import os.path

# Import widget functionality libraries
from qgis.core import QgsProject


class pcFilterSlider:
    """QGIS Plugin Implementation."""

    def __init__(self, iface):
        """Constructor.

        :param iface: An interface instance that will be passed to this class
            which provides the hook by which you can manipulate the QGIS
            application at run time.
        :type iface: QgsInterface
        """
        # Save reference to the QGIS interface
        self.iface = iface

        # initialize plugin directory
        self.plugin_dir = os.path.dirname(__file__)

        # initialize locale
        locale = QSettings().value('locale/userLocale')[0:2]
        locale_path = os.path.join(
            self.plugin_dir,
            'i18n',
            'pcFilterSlider_{}.qm'.format(locale))

        if os.path.exists(locale_path):
            self.translator = QTranslator()
            self.translator.load(locale_path)
            QCoreApplication.installTranslator(self.translator)

        # Declare instance attributes
        self.actions = []
        self.menu = self.tr(u'&Point Cloud Filter Slider')
        # TODO: We are going to let the user set this up in a future iteration
        self.toolbar = self.iface.addToolBar(u'pcFilterSlider')
        self.toolbar.setObjectName(u'pcFilterSlider')

        #print "** INITIALIZING pcFilterSlider"

        self.pluginIsActive = False
        self.dockwidget = None


    # noinspection PyMethodMayBeStatic
    def tr(self, message):
        """Get the translation for a string using Qt translation API.

        We implement this ourselves since we do not inherit QObject.

        :param message: String for translation.
        :type message: str, QString

        :returns: Translated version of message.
        :rtype: QString
        """
        # noinspection PyTypeChecker,PyArgumentList,PyCallByClass
        return QCoreApplication.translate('pcFilterSlider', message)


    def add_action(
        self,
        icon_path,
        text,
        callback,
        enabled_flag=True,
        add_to_menu=True,
        add_to_toolbar=True,
        status_tip=None,
        whats_this=None,
        parent=None):
        """Add a toolbar icon to the toolbar.

        :param icon_path: Path to the icon for this action. Can be a resource
            path (e.g. ':/plugins/foo/bar.png') or a normal file system path.
        :type icon_path: str

        :param text: Text that should be shown in menu items for this action.
        :type text: str

        :param callback: Function to be called when the action is triggered.
        :type callback: function

        :param enabled_flag: A flag indicating if the action should be enabled
            by default. Defaults to True.
        :type enabled_flag: bool

        :param add_to_menu: Flag indicating whether the action should also
            be added to the menu. Defaults to True.
        :type add_to_menu: bool

        :param add_to_toolbar: Flag indicating whether the action should also
            be added to the toolbar. Defaults to True.
        :type add_to_toolbar: bool

        :param status_tip: Optional text to show in a popup when mouse pointer
            hovers over the action.
        :type status_tip: str

        :param parent: Parent widget for the new action. Defaults None.
        :type parent: QWidget

        :param whats_this: Optional text to show in the status bar when the
            mouse pointer hovers over the action.

        :returns: The action that was created. Note that the action is also
            added to self.actions list.
        :rtype: QAction
        """

        icon = QIcon(icon_path)
        action = QAction(icon, text, parent)
        action.triggered.connect(callback)
        action.setEnabled(enabled_flag)

        if status_tip is not None:
            action.setStatusTip(status_tip)

        if whats_this is not None:
            action.setWhatsThis(whats_this)

        if add_to_toolbar:
            self.toolbar.addAction(action)

        if add_to_menu:
            self.iface.addPluginToMenu(
                self.menu,
                action)

        self.actions.append(action)

        return action


    def initGui(self):
        """Create the menu entries and toolbar icons inside the QGIS GUI."""

        icon_path = ':/plugins/pc_filter_slider/icon.png'
        self.add_action(
            icon_path,
            text=self.tr(u'PC Filter Slider'),
            callback=self.run,
            parent=self.iface.mainWindow())

    #--------------------------------------------------------------------------

    def onClosePlugin(self):
        """Cleanup necessary items here when plugin dockwidget is closed"""

        # print("** CLOSING pcFilterSlider")

        # disconnects
        self.dockwidget.closingPlugin.disconnect(self.onClosePlugin)

        # remove this statement if dockwidget is to remain
        # for reuse if plugin is reopened
        # Commented next statement since it causes QGIS crashe
        # when closing the docked window:
        # self.dockwidget = None

        self.pluginIsActive = False


    def unload(self):
        """Removes the plugin menu item and icon from QGIS GUI."""

        #print "** UNLOAD pcFilterSlider"

        for action in self.actions:
            self.iface.removePluginMenu(
                self.tr(u'&Point Cloud Filter Slider'),
                action)
            self.iface.removeToolBarIcon(action)
        # remove the toolbar
        del self.toolbar

    #--------------------------------------------------------------------------

    def initiate_widget(self):
        pc_select = self.dockwidget.cmbPointCloudLayer
        pc_select.clear()
        for layer in QgsProject.instance().mapLayers().values():
            if layer.type() == 6:
                pc_select.addItems([layer.name()])
        self.pc_layer_change(pc_select.currentText())

    def reset(self):
        global attribute_min
        global attribute_max
        self.dockwidget.lblStartValue.setText(str(round(attribute_min,1)))
        self.dockwidget.lblMaxCutoffValue.setText(str(round(attribute_max,1)))
        self.dockwidget.lblMaxThicknessValue.setText(str(round(attribute_delta,2)))
        self.dockwidget.sliderThickness.setValue(99)
        self.dockwidget.sliderCutoff.setValue(0)        
        self.filter_pc()
        

    def pc_filter_active(self):
        global pc_layer
        try:
            if self.dockwidget.chkActive.isChecked():
                self.filter_pc()
            else:
                pc_layer.setSubsetString("")
        except:
            print("Check your project!")

    def pc_layer_change(self, value):
        global pc_layer
        pc_selected = value
        for layer in QgsProject.instance().mapLayers().values():
            if layer.name() == value:
                pc_layer = layer
        self.dockwidget.cmbAttribute.clear()
        try:
            for a in pc_layer.attributes().attributes():
                self.dockwidget.cmbAttribute.addItems([a.name()])
            self.dockwidget.cmbAttribute.setCurrentText("Z")
            self.pc_attribute_change("Z")
        except:
            print("No Valid Point Cloud layer in project.")

    def pc_attribute_change(self, value):
        global attribute
        global pc_layer
        global attribute_min
        global attribute_max
        global attribute_delta
        try:
            attribute = value
        except:
            attribute = "Z"
        attribute_min = pc_layer.statistics().minimum(attribute)
        attribute_max = pc_layer.statistics().maximum(attribute)
        attribute_delta = attribute_max - attribute_min
        self.reset()        

    def pc_cutoff_change(self, value):
        self.filter_pc()

    def filter_pc(self):
        global pc_layer
        global attribute
        try:
            if not pc_layer.isValid():
                print("No valid Point Cloud layer")
                return
        except:
            print("Check your project!")
            return
        
        layer_name = pc_layer.name()
        filter_min = round(attribute_min + self.dockwidget.sliderCutoff.value() * attribute_delta / 100,2)
        self.dockwidget.lblCutoff.setText(str(filter_min))
        filter_max = round(filter_min + self.dockwidget.sliderThickness.value() * attribute_delta / 100,2)
        self.dockwidget.lblThickness.setText(str(round(self.dockwidget.sliderThickness.value() * attribute_delta / 100,2)))
        filter_string = attribute + " > " + str(filter_min)
        filter_string += " AND "
        filter_string += attribute + " < " + str(filter_max)
        pc_layer.setSubsetString(filter_string)
        self.dockwidget.chkActive.setChecked(True)
        
    def run(self):
        """Run method that loads and starts the plugin"""

        if not self.pluginIsActive:
            self.pluginIsActive = True

            #print "** STARTING pcFilterSlider"

            # dockwidget may not exist if:
            #    first run of plugin
            #    removed on close (see self.onClosePlugin method)
            if self.dockwidget == None:
                # Create the dockwidget (after translation) and keep reference
                self.dockwidget = pcFilterSliderDockWidget()

            # connect to provide cleanup on closing of dockwidget
            self.dockwidget.closingPlugin.connect(self.onClosePlugin)

            # show the dockwidget
            # TODO: fix to allow choice of dock location
            self.iface.addDockWidget(Qt.LeftDockWidgetArea, self.dockwidget)
            self.initiate_widget()
            self.dockwidget.show()

            # connect combobox for point cloud layer select
            self.dockwidget.cmbPointCloudLayer.currentTextChanged.connect(self.pc_layer_change)
            # connect combobox for point cloud attribute select
            self.dockwidget.cmbAttribute.currentTextChanged.connect(self.pc_attribute_change)
            # connect slider changes
            self.dockwidget.sliderCutoff.valueChanged.connect(self.pc_cutoff_change)
            self.dockwidget.sliderThickness.valueChanged.connect(self.pc_cutoff_change)
            # connect active checkbox
            self.dockwidget.chkActive.stateChanged.connect(self.pc_filter_active)
            # connect reset button
            self.dockwidget.btnReset.clicked.connect(self.reset)
