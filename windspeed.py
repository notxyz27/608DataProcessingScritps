import arcpy
from arcpy.sa import *

uwind_input = "d:/608/March/uwind"
vwind_input = "d:/608/March/vwind"
output = "d:/608/March/windspeed"

arcpy.CheckOutExtension("Spatial")

count = 0

for i in range(60, 91, 1):
    uwind_square = Square(uwind_input + "/uwind_14_JD_" + str(i) + ".tif")
    vwind_square = Square(vwind_input + "/vwind_14_JD_" + str(i) + ".tif")
    sum_square = Plus(uwind_square, vwind_square)
    wind_speed = SquareRoot(sum_square)
    wind_speed.save(output + "/windspeed_14_JD_" + str(i) + ".tif")
    count += 1
    print count
    

