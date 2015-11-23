# ----------------------------------------------------------------------------
# Convert feature classes to excel files
# ----------------------------------------------------------------------------
# import arcpy module
import arcpy

# Define the workspace and output folder
arcpy.env.workspace = "c:/608Data/test/process8.gdb"
output_path = "c:/608Data/excel_files"

count = 0
# Interate features in the geodatabase to convert them into excel files
for item in arcpy.ListFeatureClasses("*", "All"):
    output_excel = output_path + "/aqua_" + item[-8:] + ".xls"
    arcpy.TableToExcel_conversion(item, output_excel)
    count += 1
    print count