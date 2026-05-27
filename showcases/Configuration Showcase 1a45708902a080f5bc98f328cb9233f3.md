# Configuration Showcase

ID: A7246742B-25
Programming Language: Alibre Script, IronPython2.7
LLM or AI Product: CustomChatGPTPro
Model: o1
By StephenBot: No
Status: Done
Category: Testbed
Reviewed: No
Created time: February 23, 2025 7:30 PM
AI summary: Showcases configuration management using IronPython 2.7, including creating, activating, and modifying configurations, along with locking properties and retrieving configuration information.

```python
# Configurations Showcase

# Ensure compatibility with IronPython 2.7
from __future__ import print_function

# Create a new part
PartName = "ConfigurationDemoPart"
P = Part(PartName)

# Check if a configuration exists
def ConfigurationExists(part, config_name):
    for config in part.Configurations:
        if config.Name == config_name:
            return True
    return False

# Create a new configuration
def CreateConfiguration(part, config_name, base_config=None):
    if not ConfigurationExists(part, config_name):
        if base_config:
            return part.AddConfiguration(config_name, base_config)
        else:
            return part.AddConfiguration(config_name)
    else:
        print("Configuration '{}' already exists.".format(config_name))
        return None

# Retrieve configuration information
def GetConfigurationInfo(part):
    print("\nConfigurations in the part:")
    for config in part.Configurations:
        print("- Name: {}".format(config.Name))
        print("  Active: {}".format("Yes" if config.IsActive else "No"))

# Activate a configuration
def ActivateConfiguration(part, config_name):
    if ConfigurationExists(part, config_name):
        config = part.GetConfiguration(config_name)
        config.Activate()
        print("Activated configuration: {}".format(config_name))
    else:
        print("Configuration '{}' not found.".format(config_name))

# Lock or unlock configuration properties
def ModifyConfigurationLocks(part, config_name, lock=True):
    if ConfigurationExists(part, config_name):
        config = part.GetConfiguration(config_name)
        if lock:
            config.LockAll()
            print("All properties locked for configuration '{}'".format(config_name))
        else:
            config.UnlockAll()
            print("All properties unlocked for configuration '{}'".format(config_name))
    else:
        print("Configuration '{}' not found.".format(config_name))

# Set specific configuration locks
def SetConfigurationLocks(part, config_name, locks):
    if ConfigurationExists(part, config_name):
        config = part.GetConfiguration(config_name)
        config.SetLocks(locks)
        print("Locks set for configuration '{}'".format(config_name))
    else:
        print("Configuration '{}' not found.".format(config_name))

# Get the currently active configuration
def GetActiveConfiguration(part):
    active_config = part.GetActiveConfiguration()
    print("Current active configuration: {}".format(active_config.Name))

# Main execution
print("Starting Configuration Showcase...")

# Create Configurations
CreateConfiguration(P, "Config_A")
CreateConfiguration(P, "Config_B", "Config_A")

# Display all configurations
GetConfigurationInfo(P)

# Activate a configuration
ActivateConfiguration(P, "Config_A")

# Modify configuration locks
ModifyConfigurationLocks(P, "Config_A", lock=True)
ModifyConfigurationLocks(P, "Config_A", lock=False)

# Set specific locks on a configuration
SetConfigurationLocks(P, "Config_A", LockTypes.SuppressNewFeatures | LockTypes.LockColorProperties)

# Get the currently active configuration
GetActiveConfiguration(P)

# Display final configurations
GetConfigurationInfo(P)

print("Configuration Showcase Completed.")

```

Output:

```
Starting Configuration Showcase...

Configurations in the part:
- Name: Config<1>
  Active: Yes
- Name: Config_A
  Active: No
- Name: Config_B
  Active: No
Activated configuration: Config_A
All properties locked for configuration 'Config_A'
All properties unlocked for configuration 'Config_A'
Locks set for configuration 'Config_A'
Current active configuration: Config_A

Configurations in the part:
- Name: Config<1>
  Active: No
- Name: Config_A
  Active: Yes
- Name: Config_B
  Active: No
Configuration Showcase Completed.
```