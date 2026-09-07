# Part and GPF Loader with Parameter Reader

ID: A7246742B-21
Programming Language: Alibre Script, IronPython2.7
LLM or AI Product: CustomChatGPT
By StephenBot: No
Status: Done
Category: Testbed
Reviewed: No
Created time: January 26, 2025 1:21 PM
AI summary: Python script that loads a part and its global parameters, creates a timestamped output folder, and lists favorite parameters from the GPF. Handles errors when the part or GPF is missing.

```python
import math                             # For math operations
from datetime import datetime          # For timestamp
import os, sys                         # For path/file operations & sys.exit
print("Script has started...")

# Step 1: Access the current part
try:
    part = CurrentPart()
    print("Part loaded: {}".format(part.Name))
except Exception as e:
    print("Error: No part is currently loaded in Alibre.\n{}".format(str(e)))
    sys.exit()  # Exit if no part is available

# Step 2: Attempt to access an already-linked GPF
try:
    # Add GPF Link Code Here
    print("GPF loaded (linked to part): {}".format(GPF.Name))
except:
    # If there's no GPF linked, fallback to open a known GPF from disk
    print("No linked GPF found. Trying to open from path...")
    GPFpath = r"{path}"              # Adjust as needed
    GPFname = "New_Global_Parameters_Script"         # The GPF 'internal name'
    try:
        GPF = GlobalParameters(GPFpath, GPFname)
        print("Opened GPF from disk: '{}'".format(GPF.Name))
    except Exception as ex:
        print("Error: Could not open GPF from disk.\n{}".format(str(ex)))
        sys.exit()

# OPTIONAL: You can set units for your script if needed
Units.Current = UnitTypes.Inches

# Step 3: Create the output folder
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")  # For unique naming
output_folder = os.path.join(
    r"{path}",          # Base folder
    "{}_{}_{}".format(part.Name, GPF.Name, timestamp) # E.g. "PartName_GPFName_YYYYMMDD_HHMMSS"
)
os.makedirs(output_folder)
print("Output folder created: {}".format(output_folder))

# Step 4: Read *favorite* parameters from the GPF
Fake_Favorites = [param.Comment for param in GPF.Parameters if param.Comment]
print("Favorite parameters in GPF: {}".format(Fake_Favorites))

# (Optional) Debug or additional listing:
# Show all parameter names, values, and comments
all_names = [p.Name for p in GPF.Parameters]
all_values = [p.Value for p in GPF.Parameters]
all_comments = [p.Comment for p in GPF.Parameters]

print("All Param Names: ", all_names)
print("All Param Values:", all_values)
print("All Param Comments (Fake_Favorites):", all_comments)
print("Script completed successfully.")
```