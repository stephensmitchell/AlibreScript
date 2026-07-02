# Parameter Showcase

ID: A7246742B-26
Programming Language: Alibre Script, IronPython2.7
LLM or AI Product: CustomChatGPTPro
Model: o1
By StephenBot: No
Status: Done
Category: Testbed
Reviewed: No
Created time: February 23, 2025 8:06 PM
AI summary: Alibre Script code that creates, lists, updates, and deletes part parameters such as Width, Height, and EquationParam.

```python
import sys
from AlibreScript.API import *

# Ensure we are using millimeters for script units
Units.Current = UnitTypes.Millimeters

# Create a new part
part = Part("Parameter_Showcase")

# Create parameters (C - Create)
def create_parameters():
    print("Creating parameters...")
    part.AddParameter("Width", ParameterTypes.Distance, 50.0)
    part.AddParameter("Height", ParameterTypes.Distance, ParameterUnits.Centimeters, 5.0)
    part.AddParameter("Angle", ParameterTypes.Angle, 30.0)
    part.AddParameter("HoleDiameter", ParameterTypes.Distance, 12.0)
    part.AddParameter("EquationParam", ParameterTypes.Distance, "Width/2")
    print("Parameters created successfully.")

# Read and list all parameters (R - Read)
def list_parameters():
    print("Listing all parameters...")
    if not part.Parameters:
        print("No parameters found.")
    else:
        for param in part.Parameters:
            print("---------------------------------")
            print("Name: ", param.Name)
            print("Type: ", param.Type)
            print("Units: ", param.Units)
            print("Value: ", param.Value)
            print("Raw Value: ", param.RawValue)
            print("Equation: ", param.Equation)
            print("Comment: ", param.Comment if param.Comment else "None")
    print("---------------------------------")

# Update parameter values and equations (U - Update)
def update_parameters():
    print("Updating parameters...")
    width_param = part.GetParameter("Width")
    if width_param:
        width_param.Value = 75.0
        print("Updated 'Width' parameter to 75.0 mm")
    
    equation_param = part.GetParameter("EquationParam")
    if equation_param:
        equation_param.Equation = "Height * 2"
        print("Updated 'EquationParam' equation to 'Height * 2'")
    
    print("Parameters updated successfully.")

# Delete a parameter (D - Delete)
def delete_parameter(param_name):
    print("Deleting parameter: ", param_name)
    param = part.GetParameter(param_name)
    if param:
        part.RemoveFeature(param.Name)
        print("Parameter deleted: ", param_name)
    else:
        print("Parameter not found: ", param_name)

# Check if a parameter exists
def parameter_exists(param_name):
    return part.GetParameter(param_name) is not None

# Main Execution Flow
create_parameters()
list_parameters()
update_parameters()
list_parameters()
delete_parameter("HoleDiameter")
list_parameters()

print("Parameter showcase completed.")

```

Output:

```
Creating parameters...
Parameters created successfully.
Listing all parameters...
---------------------------------
('Name: ', 'Width')
('Type: ', AlibreScript.API.ParameterTypes.Distance)
('Units: ', AlibreScript.API.ParameterUnits.Centimeters)
('Value: ', 50.0)
('Raw Value: ', 5.0)
('Equation: ', '')
('Comment: ', 'None')
---------------------------------
('Name: ', 'EquationParam')
('Type: ', AlibreScript.API.ParameterTypes.Distance)
('Units: ', AlibreScript.API.ParameterUnits.Centimeters)
('Value: ', 25.0)
('Raw Value: ', 2.5)
('Equation: ', 'Width/2')
('Comment: ', 'None')
---------------------------------
('Name: ', 'HoleDiameter')
('Type: ', AlibreScript.API.ParameterTypes.Distance)
('Units: ', AlibreScript.API.ParameterUnits.Centimeters)
('Value: ', 11.999999999999998)
('Raw Value: ', 1.2)
('Equation: ', '')
('Comment: ', 'None')
---------------------------------
('Name: ', 'Height')
('Type: ', AlibreScript.API.ParameterTypes.Distance)
('Units: ', AlibreScript.API.ParameterUnits.Centimeters)
('Value: ', 50.0)
('Raw Value: ', 5.0)
('Equation: ', '')
('Comment: ', 'None')
---------------------------------
('Name: ', 'Angle')
('Type: ', AlibreScript.API.ParameterTypes.Angle)
('Units: ', AlibreScript.API.ParameterUnits.Degrees)
('Value: ', 29.999999999999996)
('Raw Value: ', 29.999999999999996)
('Equation: ', '')
('Comment: ', 'None')
---------------------------------
Updating parameters...
Updated 'Width' parameter to 75.0 mm
Updated 'EquationParam' equation to 'Height * 2'
Parameters updated successfully.
Listing all parameters...
---------------------------------
('Name: ', 'Width')
('Type: ', AlibreScript.API.ParameterTypes.Distance)
('Units: ', AlibreScript.API.ParameterUnits.Centimeters)
('Value: ', 75.0)
('Raw Value: ', 7.5)
('Equation: ', '')
('Comment: ', 'None')
---------------------------------
('Name: ', 'EquationParam')
('Type: ', AlibreScript.API.ParameterTypes.Distance)
('Units: ', AlibreScript.API.ParameterUnits.Centimeters)
('Value: ', 100.0)
('Raw Value: ', 10.0)
('Equation: ', 'Height * 2')
('Comment: ', 'None')
---------------------------------
('Name: ', 'HoleDiameter')
('Type: ', AlibreScript.API.ParameterTypes.Distance)
('Units: ', AlibreScript.API.ParameterUnits.Centimeters)
('Value: ', 11.999999999999998)
('Raw Value: ', 1.2)
('Equation: ', '')
('Comment: ', 'None')
---------------------------------
('Name: ', 'Height')
('Type: ', AlibreScript.API.ParameterTypes.Distance)
('Units: ', AlibreScript.API.ParameterUnits.Centimeters)
('Value: ', 50.0)
('Raw Value: ', 5.0)
('Equation: ', '')
('Comment: ', 'None')
---------------------------------
('Name: ', 'Angle')
('Type: ', AlibreScript.API.ParameterTypes.Angle)
('Units: ', AlibreScript.API.ParameterUnits.Degrees)
('Value: ', 29.999999999999996)
('Raw Value: ', 29.999999999999996)
('Equation: ', '')
('Comment: ', 'None')
---------------------------------
('Deleting parameter: ', 'HoleDiameter')
('Parameter deleted: ', 'HoleDiameter')
Listing all parameters...
---------------------------------
('Name: ', 'Width')
('Type: ', AlibreScript.API.ParameterTypes.Distance)
('Units: ', AlibreScript.API.ParameterUnits.Centimeters)
('Value: ', 75.0)
('Raw Value: ', 7.5)
('Equation: ', '')
('Comment: ', 'None')
---------------------------------
('Name: ', 'EquationParam')
('Type: ', AlibreScript.API.ParameterTypes.Distance)
('Units: ', AlibreScript.API.ParameterUnits.Centimeters)
('Value: ', 100.0)
('Raw Value: ', 10.0)
('Equation: ', 'Height * 2')
('Comment: ', 'None')
---------------------------------
('Name: ', 'HoleDiameter')
('Type: ', AlibreScript.API.ParameterTypes.Distance)
('Units: ', AlibreScript.API.ParameterUnits.Centimeters)
('Value: ', 11.999999999999998)
('Raw Value: ', 1.2)
('Equation: ', '')
('Comment: ', 'None')
---------------------------------
('Name: ', 'Height')
('Type: ', AlibreScript.API.ParameterTypes.Distance)
('Units: ', AlibreScript.API.ParameterUnits.Centimeters)
('Value: ', 50.0)
('Raw Value: ', 5.0)
('Equation: ', '')
('Comment: ', 'None')
---------------------------------
('Name: ', 'Angle')
('Type: ', AlibreScript.API.ParameterTypes.Angle)
('Units: ', AlibreScript.API.ParameterUnits.Degrees)
('Value: ', 29.999999999999996)
('Raw Value: ', 29.999999999999996)
('Equation: ', '')
('Comment: ', 'None')
---------------------------------
Parameter showcase completed.

```