
layer = QgsProject.instance().mapLayersByName('Polska')
actual_layers = QgsProject.instance().mapLayers().values()

for lay in actual_layers:
    column_names_to_del = lay.fields().names()
    if "Nr_regist" in column_names_to_del:
        lay.startEditing()
        layer_prov_to_del = lay.dataProvider()
        layer_prov_to_del.deleteAttributes([3])
        lay.commitChanges()
    QgsProject.instance().removeMapLayer(lay)

Vectorlayer = iface.addVectorLayer("/home/damian/GIS_COURSES/Poland_shapefile/pl_10km.shp", "Polska", "ogr")

Vectorcrs = Vectorlayer.crs()

Vectorextent = Vectorlayer.extent()

min_x = Vectorextent.xMinimum()
max_x = Vectorextent.xMaximum()
min_y = Vectorextent.yMinimum()
max_y = Vectorextent.yMaximum()

n_feature = Vectorlayer.featureCount()

for field in Vectorlayer.fields():
    pass
    
features = Vectorlayer.getFeatures()
for f in features:
    attr = f.attributes()
    geom = f.geometry()
    vertices = geom.asMultiPolygon()
    
    for vvv in vertices:
        for vv in vvv:
            for v in vv:
                print(v.x(), v.y())
    break
    
column_names = Vectorlayer.fields().names()

Vectorlayer.startEditing()
layer_provider = Vectorlayer.dataProvider()
layer_provider.addAttributes([QgsField("Nr_regist", QVariant.Double)])

features = Vectorlayer.getFeatures()
nr = 1000
for f in features:
    id = f.id()
    nr = nr+1
    attr_value = {3: nr}
    layer_provider.changeAttributeValues({id:attr_value})
    

Vectorlayer.commitChanges()


#csrsrc = QgsCoordinateReferenceSystem(3035)
#csrdest = QgsCoordinateReferenceSystem(2177)

#xform = QgsCoordinateTransform(csrsrc, csrdest, QgsProject.instance())

