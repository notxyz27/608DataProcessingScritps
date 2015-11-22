# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------
# test.py
# Created on: 2015-11-18 13:54:33.00000
#   (generated by ArcGIS/ModelBuilder)
# Description: 
# Scripts for extracting temperature, relative humidity, planetary boundary layer,
# surface pressure, U wind and V wind data stored in .nc file. The data is extracted
# and stored in rasters each of which shows the records for one of above factors
# at a particular time in a day.  
# ---------------------------------------------------------------------------

# Import arcpy module
import arcpy


# Local variables:
# Define the path to the .nc file
input_nc = "C:\\608Data\\netcdf\\data\\20140901_20150831_tem2m_1400_step0.nc"
# Temporay raster file generated from .nc
t2m_Layer1 = "t2m_Layer1"
# Output file prefix
output_tif = "C:\\608Data\\temperature\\temperature14\\t2m_14_"
# Temporay raster file for a single band stored in tem_Layer1
tem = "tem_layer"
# Process: Make NetCDF Raster Layer
arcpy.MakeNetCDFRasterLayer_md(input_nc, "t2m", "longitude", "latitude", t2m_Layer1, "time", "", "BY_VALUE")
for i in range(1, 366):
    # Process: Make Raster Layer
    arcpy.MakeRasterLayer_management(t2m_Layer1, tem, "", "DEFAULT", str(i))

    # Process: Copy Raster
    arcpy.CopyRaster_management(tem, output_tif + "JD_" + str((i+243)%365) + ".tif", "", "", "", "NONE", "NONE", "", "NONE", "NONE")

    print i

