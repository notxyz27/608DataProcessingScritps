# ----------------------------------------------------------------------------
# Change names of aod files
# ----------------------------------------------------------------------------

# Import os module
import os

# Define the path to the folder containing files for renaming
file_path = "c:/"

# Iterate the folder to rename each file
for item in os.listdir(file_path):
    os.rename(file_path + item, file_path + item[:17])