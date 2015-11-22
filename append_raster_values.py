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
arcpy.env.workspace = "c:/608Data/aqua_appended"
tem_path = "c:/608Data/temperature/temperature14"
rh_path = "c:/608Data/relative_humidity/relative_humidity14"
blh_path = "c:/608Data/boundary_layer_height"
uwind_path = "c:/608Data/UWind/UWind14"
vwind_path = "c:/608Data/VWind/VWind14"
sp_path = "c:/608Data/surface_pressure/surface_pressure14"
aod = "c:/608Data/aqua_aod"
output = "c:/608Data/aqua_shape_aod"
count = 0

# Check out the ArcGIS Spatial Analyst extension license
arcpy.CheckOutExtension("Spatial")

for item in arcpy.ListFiles("*.shp"):
    inPointFeatures = item
    julian = date_to_julian(int(item[4:6]), int(item[6:8]))
    aod_string = str(julian)
    while len(aod_string) < 3:
        aod_string = "0" + aod_string
    day_string = str(julian%365)
    inRasterList = [[aod + "/MYD04_3K.A" + item[0:4] + aod_string + ".tif", "aod"],
                    [rh_path + "/rh_14_JD_" + day_string + ".tif", "hum"],
                    [tem_path + "/t2m_14_JD_" + day_string + ".tif", "tem"],
                    [sp_path + "/sp_14_JD_" + day_string + ".tif", "sp"],
                    [uwind_path + "/uwind_14_JD_" + day_string + ".tif", "uwind"],
                    [vwind_path + "/vwind_14_JD_" + day_string + ".tif", "vwind"],
                    [blh_path + "/BLH08/blh_08_JD_" + day_string + ".tif", "blh_08"],
                    [blh_path + "/BLH20/blh_20_JD_" + day_string + ".tif", "blh_20"]]
    try:
        ExtractMultiValuesToPoints(inPointFeatures, inRasterList, "NONE")
    except:
        print item
    count += 1
    print count
