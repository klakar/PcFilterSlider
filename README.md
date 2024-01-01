# PcFilterSlider
QGIS plugin to set and change simple filters for point cloud graphically.

![bild](https://github.com/klakar/PcFilterSlider/assets/6375959/0a6bc6ac-37dc-44df-867c-32a2831a3584)

## Usage
Goto "Releases" and download the zip-file. In QGIS you open "Manage and install Plug-Ins" and select the "Install from ZIP" option.
Approve install from unknown sources (if you trust the file you downloaded). Your plugin is then available in the Plugins menu.

Before you activate the plugin you should load any pointcloud layer you want to work with. THEN you activate the plugin panel. If you change the pointcloud layers in your layers panel, you need to restart the plugin for it to update available layers. Just close the panel and start it again.

The plugin will pick one layer and the Z attribute. You can change layer and attribute if you want to filter something else.

The sliders will be set to the layer and the selected attributes min and max values.

The left slider will control the "span" of the filter, from the minimum cut-off value and up.

The right slider will control the cut-off value that the filter will use for the lower end of the filter. Any value below this value will be filtered out. Values above this, plus the value of the Thickness slider, will also be filtered out.

## Development

I'm not planning on a lot of development for this plugin. It does what I need it to do.

I will keep it here for a while trying to catch any anoying bugs, and then push it to the official plugin repository.

It you have any grand ideas about new funcionality, you are welcome to develop them yourself. :wink:
