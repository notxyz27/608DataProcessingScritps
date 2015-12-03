"""
GEOG 608 Urban Remote Sensing Project
Data preprocessing scripts

"""
# Import system modules
import arcpy

# Define workspace
arcpy.env.workspace = r"C:\608Data\terra"

# Define output folder 
output = r"C:\608Data\terra_shapefile"

# Counter
count = 0
    
# Generate shapefiles according to Lon, Lat fields in txt files
for item in arcpy.ListFiles():
    layer = item.rstrip(".txt") + "_Layer"
    arcpy.MakeXYEventLayer_management(item, "Lon", "Lat", layer, 4326)
    arcpy.FeatureClassToShapefile_conversion(layer, output)
    count += 1
    print count
    
# Define workspace
arcpy.env.workspace = r"C:\608Data\aqua"

# Define output folder 
output = r"C:\608Data\aqua_shapefile"

# Counter
count = 0
    
# Generate shapefiles according to Lon, Lat fields in txt files
for item in arcpy.ListFiles():
    layer = item.rstrip(".txt") + "_Layer"
    arcpy.MakeXYEventLayer_management(item, "Lon", "Lat", layer, 4326)
    arcpy.FeatureClassToShapefile_conversion(layer, output)
    count += 1
    print count