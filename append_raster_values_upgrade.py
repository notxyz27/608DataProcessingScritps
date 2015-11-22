# ---------------------------------------------------------------------------
# Scripts for extracting values in raster files and append extracted values to
# shapefiles according to spatail selection
# ---------------------------------------------------------------------------

# Function that helps to convert date to julian date
def date_to_julian(month, day):
    """
    Helper function to convert date to julian date
    """
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    julian_date = 0
    for index in range(month-1):
        julian_date += month_days[index]
    julian_date += day
    return julian_date

# Import arcpy module and arcpy.sa
import arcpy
from arcpy.sa import *

# Define the workspace and raster input files
arcpy.env.workspace = "c:/608Data/test/aqua_initial.gdb"
tem_path = "c:/608Data/temperature/temperature14"
rh_path = "c:/608Data/relative_humidity/relative_humidity14"
blh_path = "c:/608Data/boundary_layer_height"
uwind_path = "c:/608Data/UWind/UWind14"
vwind_path = "c:/608Data/VWind/VWind14"
sp_path = "c:/608Data/surface_pressure/surface_pressure14"
aod = "c:/608Data/aqua_aod"
output = "c:/608Data/test/aqua_final.gdb"
count = 0

# Check out the ArcGIS Spatial Analyst extension license
arcpy.CheckOutExtension("Spatial")

for item in arcpy.ListFeatureClasses("*", "All"):
    inPointFeatures = item
    julian = date_to_julian(int(item[5:7]), int(item[7:9]))
    aod_string = str(julian)
    while len(aod_string) < 3:
        aod_string = "0" + aod_string
    day_string = str(julian%365)
    inRasterList = [aod + "/MYD04_3K.A" + item[1:5] + aod_string + ".tif",
                    rh_path + "/rh_14_JD_" + day_string + ".tif",
                    tem_path + "/t2m_14_JD_" + day_string + ".tif",
                    sp_path + "/sp_14_JD_" + day_string + ".tif",
                    uwind_path + "/uwind_14_JD_" + day_string + ".tif",
                    vwind_path + "/vwind_14_JD_" + day_string + ".tif",
                    blh_path + "/BLH08/blh_08_JD_" + day_string + ".tif",
                    blh_path + "/BLH20/blh_20_JD_" + day_string + ".tif"]
    outPointList = ["c:/608Data/test/process1.gdb/aqua_aod" + item[1:9],
                    "c:/608Data/test/process2.gdb/aqua_rh" + item[1:9],
                    "c:/608Data/test/process3.gdb/aqua_t2m" + item[1:9],
                    "c:/608Data/test/process4.gdb/aqua_sp" + item[1:9],
                    "c:/608Data/test/process5.gdb/aqua_uw" + item[1:9],
                    "c:/608Data/test/process6.gdb/aqua_vw" + item[1:9],
                    "c:/608Data/test/process7.gdb/aqua_blh08_" + item[1:9],
                    "c:/608Data/test/process8.gdb/aqua_blh20_" + item[1:9]]
    try:
        ExtractValuesToPoints(inPointFeatures, inRasterList[0], outPointList[0],
                      "NONE", "VALUE_ONLY")
        arcpy.AlterField_management(outPointList[0], "RASTERVALU", "AOD")
        
        ExtractValuesToPoints(outPointList[0], inRasterList[1], outPointList[1],
                      "NONE", "VALUE_ONLY")
        arcpy.AlterField_management(outPointList[1], "RASTERVALU", "hum")
        
        ExtractValuesToPoints(outPointList[1], inRasterList[2], outPointList[2],
                      "NONE", "VALUE_ONLY")
        arcpy.AlterField_management(outPointList[2], "RASTERVALU", "t2m")
        
        ExtractValuesToPoints(outPointList[2], inRasterList[3], outPointList[3],
                      "NONE", "VALUE_ONLY")
        arcpy.AlterField_management(outPointList[3], "RASTERVALU", "sp")
        
        ExtractValuesToPoints(outPointList[3], inRasterList[4], outPointList[4],
                      "NONE", "VALUE_ONLY")
        arcpy.AlterField_management(outPointList[4], "RASTERVALU", "uwind")
        
        ExtractValuesToPoints(outPointList[4], inRasterList[5], outPointList[5],
                      "NONE", "VALUE_ONLY")
        arcpy.AlterField_management(outPointList[5], "RASTERVALU", "vwind")
        
        ExtractValuesToPoints(outPointList[5], inRasterList[6], outPointList[6],
                      "NONE", "VALUE_ONLY")
        arcpy.AlterField_management(outPointList[6], "RASTERVALU", "blh08")
        
        ExtractValuesToPoints(outPointList[6], inRasterList[7], outPointList[7],
                      "NONE", "VALUE_ONLY")
        arcpy.AlterField_management(outPointList[7], "RASTERVALU", "blh20")

    except:
        print item
    count += 1
    print count
