import arcpy
from arcpy.sa import *

aod_input = "d:/608/March/aod"
aod_output = "d:/608/March/aod_none"

count = 0

arcpy.CheckOutExtension("Spatial")

for i in range(60, 91, 1):
    inRaster = aod_input + "/MYD04_3K.A20150" + str(i) + ".tif"
    whereClause = "Value = -9999"
    outSetNull = SetNull(inRaster, inRaster, whereClause)
    outSetNull.save(aod_output + "/none_JD_" + str(i) + ".tif")
    count += 1
    print count
