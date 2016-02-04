import arcpy
from arcpy.sa import *

aod_input = "d:/608/March/aod_none"
tm_input = "d:/608/March/tem"
hum_input = "d:/608/March/rh"
blh_input = "d:/608/March/blh/blh14"
windspeed_input = "d:/608/March/windspeed"
sp_input = "d:/608/March/sp"
output = "d:/608/March/model_none"

arcpy.CheckOutExtension("Spatial")

count = 0

for i in range(60, 91, 1):
    aod_over_1000 = Divide(aod_input + "/none_JD_" + str(i) + ".tif", 1000.0)
    aod_facts = Times(41.136, aod_over_1000)
    hum_facts = Times(-0.414, hum_input + "/rh_14_JD_" + str(i) + ".tif")
    tm_facts = Times(0.787, tm_input + "/t2m_14_JD_" + str(i) + ".tif")
    sp_over_1000 = Divide(sp_input + "/sp_14_JD_" + str(i) + ".tif", 1000.0)
    sp_facts = Times(-1.261, sp_over_1000)
    ws_facts = Times(2.458, windspeed_input + "/windspeed_14_JD_" + str(i) + ".tif")
    blh_facts = Times(-0.025, blh_input + "/blh_14_JD_" + str(i) + ".tif")
    # Use Map Algebra
    outRaster = aod_facts + hum_facts + tm_facts + sp_facts + ws_facts + blh_facts - 74.551
    outRaster.save(output + "/JD_" + str(i) + ".tif")

    count += 1
    print count
    
