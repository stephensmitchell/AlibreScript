# Assembly and Part Thumbnail Generator (IronPython 2.7)

ID: A7246742B-18
Programming Language: Alibre Script, IronPython2.7
LLM or AI Product: CustomChatGPT
By StephenBot: No
Status: Done
Category: Testbed
Reviewed: No
Created time: January 12, 2025 5:04 AM
AI summary: Script generates thumbnails for assembly and part files, saves them as .jpg, and creates an Excel workbook embedding these images in 300×300 pixel cells. User inputs thumbnail size and output folder, and the script handles both parts and assemblies recursively.

```python
# https://www.alibre.com/forum/index.php?threads/add-icon-image-from-the-alibre-file-to-the-parts-list.25649/#post-176092 | @Cator from Alibre Forum

# ------------------------------------------------------------
# Assembly and Part Thumbnail Generator (IronPython 2.7)
# ------------------------------------------------------------
# This script:
#   1. Prompts the user for thumbnail size and output folder.
#   2. Detects whether the current document is an Assembly or Part.
#   3. Explores the assembly/subassemblies to:
#       - Count identical parts (group by normalized name).
#       - Save part/subassembly thumbnails as .jpg.
#   4. Creates an Excel workbook (Images_NET.xlsx) that embeds
#      all images found in the chosen folder, placing each image
#      inside a cell sized 300×300 pixels (approx).
# ------------------------------------------------------------

import clr
import sys
import re
import os
from collections import defaultdict

# Add references for .NET interop with Excel
clr.AddReference("System")
clr.AddReference("Microsoft.Office.Interop.Excel")

from Microsoft.Office.Interop import Excel

# Minimal MsoTriState "enum" to avoid referencing Microsoft.Office.Core
class MsoTriState:
    msoFalse = 0
    msoTrue = -1

# ------------------------------------------------------------
# STEP 1: Prompt user for inputs (thumbnail size + save folder)
# ------------------------------------------------------------

Win = Windows()  # Provided by your CAD/automation environment
Option = [
    ['Thumbnail Size', WindowsInputTypes.Real, 100],
    ['Save Folder',   WindowsInputTypes.Folder, None],
]
Values = Win.OptionsDialog("Image from Assembly", Option, 100)

if Values is None:
    sys.exit()

dimension_thumb = Values[0]
save_path = Values[1]

# ------------------------------------------------------------
# STEP 2: Detect if we have an Assembly or a Part
# ------------------------------------------------------------

def detect_type():
    """
    Detect if the object is an assembly or a part based on common attributes.
    """
    try:
        if hasattr(CurrentAssembly(), 'Parts'):
            obj = CurrentAssembly()
            obj_type = 'Assembly'
        else:
            raise Exception("Invalid assembly")
    except:
        if hasattr(CurrentPart(), 'Name'):
            obj = CurrentPart()
            obj_type = 'Part'
        else:
            raise Exception("Invalid part")
    return obj, obj_type

# ------------------------------------------------------------
# STEP 3: Generate thumbnails for each Part/Subassembly
# ------------------------------------------------------------

def normalize_part_name(part_name):
    """
    Remove unique identifiers like <1>, <2>, etc. from part names.
    """
    return re.sub(r"<\d+>", "", part_name)

def clean_file_name(name):
    """
    Remove invalid characters for Windows file names.
    """
    invalid_chars = r'<>:"/\|?*'
    return re.sub('[{}]'.format(re.escape(invalid_chars)), '_', name)

def ListPartsInAssembly(assembly, save_path):
    """
    Explore the assembly (and subassemblies), group identical parts,
    count quantities, and save thumbnails for parts/subassemblies.
    """
    parts_count = defaultdict(int)

    def process_assembly(asm):
        for part in asm.Parts:
            part_name = part.Name if hasattr(part, 'Name') else str(part)
            normalized_name = normalize_part_name(part_name)
            parts_count[normalized_name] += 1

            cleaned_name = clean_file_name(normalized_name)
            part.SaveThumbnail(
                os.path.join(save_path, cleaned_name + '.jpg'),
                dimension_thumb,
                dimension_thumb
            )

        for sub_asm in asm.SubAssemblies:
            sub_asm_name = sub_asm.Name if hasattr(sub_asm, 'Name') else str(sub_asm)
            cleaned_name = clean_file_name(sub_asm_name)
            sub_asm.SaveThumbnail(
                os.path.join(save_path, cleaned_name + '.jpg'),
                dimension_thumb,
                dimension_thumb
            )
            # Recurse into subassembly
            process_assembly(sub_asm)

    process_assembly(assembly)

    # Print consolidated part list
    print("\nConsolidated Part List:")
    for part, quantity in parts_count.items():
        print("- {}: {}".format(part, quantity))

# ------------------------------------------------------------
# STEP 4: Create Excel workbook and embed images with 300×300 cells
# ------------------------------------------------------------

def GenerateExcelWithImagesNET(image_directory):
    """
    Creates an Excel workbook that lists all images in `image_directory`
    in two columns:
        1. Image Name
        2. Embedded Image (300×300 px, approx)
    """
    # Start Excel
    excel = Excel.ApplicationClass()
    excel.Visible = False  # Change to True if you want to see Excel UI

    # Create a new Workbook (which has one blank worksheet by default)
    workbook = excel.Workbooks.Add()
    sheet = workbook.Worksheets[1]

    # Header cells
    sheet.Cells[1, 1].Value2 = "Image Name"
    sheet.Cells[1, 2].Value2 = "Image"

    # (Optional) freeze the header row or format as needed
    # sheet.Range("A1:B1").Font.Bold = True

    # Convert 300 px to points (approx: 1 px ≈ 0.75 pt at 96 DPI)
    # 300 px * (72 / 96) = 225 pt
    cell_size_points = 225  

    # Set entire column B's width so it can hold ~300 px
    # ~ 42.5 characters in standard Excel measure ≈ 300 px
    sheet.Columns("B").ColumnWidth = 42.5

    row = 2
    valid_extensions = ('.jpg', '.jpeg', '.png', '.bmp', '.gif')

    for filename in os.listdir(image_directory):
        if filename.lower().endswith(valid_extensions):
            image_path = os.path.join(image_directory, filename)

            # Write file name in column A
            sheet.Cells[row, 1].Value2 = filename

            # Set the row height to match 300 px (~225 points)
            sheet.Rows(row).RowHeight = cell_size_points

            # Calculate the cell's top-left in points
            left = sheet.Cells(row, 2).Left
            top = sheet.Cells(row, 2).Top

            # Insert the image as a shape that fits ~300×300 px
            picture = sheet.Shapes.AddPicture(
                Filename=image_path,
                LinkToFile=MsoTriState.msoFalse,      # Do not link to file
                SaveWithDocument=MsoTriState.msoTrue, # Embed in the workbook
                Left=left,
                Top=top,
                Width=cell_size_points,
                Height=cell_size_points
            )

            row += 1

    # Auto-fit Column A for better readability
    sheet.Columns("A").AutoFit()

    # Save workbook in the same folder
    excel_file_path = os.path.join(image_directory, "Images_NET.xlsx")
    workbook.SaveAs(excel_file_path)
    workbook.Close(False)
    excel.Quit()

    print("\nExcel file with images created at: {}".format(excel_file_path))

# ------------------------------------------------------------
# MAIN EXECUTION
# ------------------------------------------------------------

def Main():
    obj, obj_type = detect_type()

    if obj_type == 'Part':
        # Generate a single thumbnail for this part
        print("Current document is a Part; generating thumbnail.")
        cleaned_name = clean_file_name(obj.Name)
        obj.SaveThumbnail(
            os.path.join(save_path, cleaned_name + '.jpg'),
            dimension_thumb,
            dimension_thumb
        )
    else:
        # Treat it as an Assembly
        print("Current document is an Assembly; generating thumbnails.")
        ListPartsInAssembly(obj, save_path)

    # Finally, create the Excel workbook with 300×300 embedded images
    GenerateExcelWithImagesNET(save_path)

Main()
```