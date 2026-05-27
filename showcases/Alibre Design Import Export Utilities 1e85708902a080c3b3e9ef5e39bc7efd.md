# Alibre Design Import/Export Utilities

ID: A7246742B-32
Programming Language: Alibre Script, IronPython2.7
LLM or AI Product: CustomChatGPTPro
Model: o1
By StephenBot: No
Status: In progress
Category: Testbed
Reviewed: No
Created time: May 3, 2025 4:03 AM
AI summary: Utilities for importing and exporting parts in Alibre Design using Python, including functions for exporting to SAT and STEP formats, and importing from STEP, IGES, and SAT files, with error handling for initialization and file operations.

```python
import clr
clr.AddReference("AlibreScriptAddOn")
clr.AddReference('System.Runtime.InteropServices')
from System.Runtime.InteropServices import Marshal
from AlibreScript.API import *

class AlibreDesignImportExportUtils:
    def __init__(self):
        """Initialize the Alibre Python Utils session."""
        try:
            self.alibre = Marshal.GetActiveObject("AlibreX.AutomationHook")
            self.root = self.alibre.Root
        except Exception as e:
            print "Failed to initialize Alibre Python Utils: %s" % e
            self.alibre = None
            self.root = None

    def export_part_to_sat(self, filename, sat_version=7, save_colors=False):
        """Exports the active part to a SAT file."""
        if not self.alibre or not self.root:
            print "Alibre Python Utils is not initialized."
            return
        try:
            myPart = Part(self.root.TopmostSession)
            myPart.ExportSAT(filename, sat_version, save_colors)
            print "Successfully exported the part to SAT: %s" % filename
        except Exception as e:
            print "An error occurred during SAT export: %s" % e

    def export_part_to_step(self, filename, format="STEP203"):
        """Exports the active part to STEP203 or STEP214."""
        if not self.alibre or not self.root:
            print "Alibre Python Utils is not initialized."
            return
        try:
            myPart = Part(self.root.TopmostSession)
            if format.upper() == "STEP203":
                myPart.ExportSTEP203(filename)
                print "Exported STEP203 to %s" % filename
            elif format.upper() == "STEP214":
                myPart.ExportSTEP214(filename)
                print "Exported STEP214 to %s" % filename
            else:
                print "Unknown STEP format: %s" % format
        except Exception as e:
            print "An error occurred during STEP export: %s" % e

    def import_step_part(self, filepath):
        """Imports a STEP (.step or .stp) file as a part."""
        try:
            part = Part(filepath, Part.FileTypes.STEP)
            print "Successfully imported STEP file: %s" % filepath
            return part
        except Exception as e:
            print "An error occurred during STEP import: %s" % e
            return None

    def import_iges_part(self, filepath):
        """Imports an IGES (.igs/.iges) file as a part."""
        try:
            part = Part(filepath, Part.FileTypes.IGES)
            print "Successfully imported IGES file: %s" % filepath
            return part
        except Exception as e:
            print "An error occurred during IGES import: %s" % e
            return None

    def import_sat_part(self, filepath):
        """Imports a SAT (.sat) file as a part."""
        try:
            part = Part(filepath, Part.FileTypes.SAT)
            print "Successfully imported SAT file: %s" % filepath
            return part
        except Exception as e:
            print "An error occurred during SAT import: %s" % e
            return None

```