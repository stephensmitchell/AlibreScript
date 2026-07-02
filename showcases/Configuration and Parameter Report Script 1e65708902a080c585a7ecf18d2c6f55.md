# Configuration and Parameter Report Script

ID: A7246742B-31
Programming Language: Alibre Script, IronPython2.7
LLM or AI Product: CustomChatGPTPro
Model: o1
By StephenBot: No
Status: Done
Category: Testbed
Reviewed: No
Created time: April 30, 2025 11:10 PM
AI summary: The script prints a configuration and parameter report covering local and global configurations and parameters, with their names, types, values, and statuses. It first retrieves configuration information and ends with a report completion message.

[001.AD_PKG](001.ad_pkg)

```python
from __future__ import print_function

# Always refer to the currently active part
P = CurrentPart()
G = GlobalParameters("001", False)

# Retrieve configuration information
def GetConfigurationInfo(part):
    print("\n[Local Configurations]")
    for config in part.Configurations:
        print("- Name: {}".format(config.Name))
        print("  Active: {}".format("Yes" if config.IsActive else "No"))

# Display all global configurations
def DisplayGlobalConfigurations(gparams):
    print("\n[Global Configurations]")
    for config in gparams.Configurations:
        print("- Name: {}".format(config.Name))
        print("  Active: {}".format("Yes" if config.IsActive else "No"))

# Display all global parameters
def DisplayGlobalParameters(gparams):
    print("\n[Global Parameters]")
    for param in gparams.Parameters:
        print("- Name: {}".format(param.Name))
        print("  Type: {}".format(param.Type))
        print("  Value: {}".format(param.Value))
        print("  Raw Value: {}".format(param.RawValue))
        print("  Equation: {}".format(param.Equation))
        print("  Units: {}".format(param.Units))
        print("  Comment: {}".format(param.Comment))

# Display all local parameters
def DisplayLocalParameters(part):
    print("\n[Local Parameters]")
    for param in part.Parameters:
        print("- Name: {}".format(param.Name))
        print("  Type: {}".format(param.Type))
        print("  Value: {}".format(param.Value))
        print("  Raw Value: {}".format(param.RawValue))
        print("  Equation: {}".format(param.Equation))
        print("  Units: {}".format(param.Units))
        print("  Comment: {}".format(param.Comment))

# Main execution
print("Starting Configuration and Parameter Report...")

GetConfigurationInfo(P)
DisplayLocalParameters(P)
DisplayGlobalParameters(G)
DisplayGlobalConfigurations(G)

print("Report Completed.")

```

![image.png](image%208.png)

![image.png](image%209.png)

```bash
>>>
Starting Configuration and Parameter Report...

[Local Configurations]
- Name: PartTest1
  Active: Yes
- Name: PartTest2
  Active: No

[Local Parameters]
- Name: D3
  Type: Distance
  Value: 914.4
  Raw Value: 91.44
  Equation: HEIGHT
  Units: Centimeters
  Comment: 
- Name: D7
  Type: Distance
  Value: 46.6461893250
  Raw Value: 4.66461893250
  Equation: 
  Units: Centimeters
  Comment: 
- Name: D2
  Type: Distance
  Value: 1676.4
  Raw Value: 167.64
  Equation: LENGTH
  Units: Centimeters
  Comment: 
- Name: D4
  Type: Distance
  Value: 88.9419006348
  Raw Value: 8.89419006348
  Equation: 
  Units: Centimeters
  Comment: 
- Name: D6
  Type: Distance
  Value: 1524.0
  Raw Value: 152.4
  Equation: 
  Units: Centimeters
  Comment: 
- Name: D1
  Type: Distance
  Value: 914.4
  Raw Value: 91.44
  Equation: HEIGHT
  Units: Centimeters
  Comment: 

[Global Parameters]
- Name: length
  Type: Distance
  Value: 1676.4
  Raw Value: 167.64
  Equation: 
  Units: Centimeters
  Comment: 
- Name: height
  Type: Distance
  Value: 914.4
  Raw Value: 91.44
  Equation: 
  Units: Centimeters
  Comment: 

[Global Configurations]
- Name: Test1
  Active: No
- Name: Test2
  Active: Yes
Report Completed.
>>>
```