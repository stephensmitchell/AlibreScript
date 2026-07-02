# Python script for generating thumbnails and an Excel report

ID: A7246742B-20
Programming Language: Alibre Script, IronPython2.7
LLM or AI Product: CustomChatGPT
By StephenBot: No
Status: Done
Category: Testbed
Reviewed: No
Created time: January 18, 2025 1:58 AM
AI summary: Python script generates thumbnails and an Excel report for parts and assemblies. It has utility functions for file naming and thumbnail saving, and writes images and quantities into Excel.

```python
import clr
import sys
import re
import os

from collections import defaultdict

clr.AddReference("System")
clr.AddReference("Microsoft.Office.Interop.Excel")

from Microsoft.Office.Interop import Excel

################################################################
# Minimal MsoTriState "enum" for AddPicture in .NET Excel interop
################################################################
class MsoTriState:
    msoFalse = 0
    msoTrue = -1

###########################################################
# 1) UTILITY FUNCTIONS
###########################################################

def clean_file_name(name):
    """
    Replace any invalid Windows file-system characters with underscores.
    """
    if not isinstance(name, basestring):
        # Fallback if name is None or some other non-string
        return "NoName"

    invalid_chars = r'<>:"/\\|?*'
    return re.sub('[{}]'.format(re.escape(invalid_chars)), '_', name)

def normalize_part_name(part_name):
    """
    Remove angle-bracket instance tags like <1>, <2>, etc.
    """
    return re.sub(r"<\d+>", "", part_name)

def debug_print(*args):
    """
    Simple helper so we can add debugging lines. 
    Example usage: debug_print("Message:", value)
    """
    msg = " ".join(str(a) for a in args)
    print(msg)

###########################################################
# 2) PROMPT FOR THUMBNAIL SIZE & SAVE FOLDER
###########################################################

Win = Windows()  # Provided by Alibre Script environment
Option = [
    ['Thumbnail Size',  WindowsInputTypes.Real,   100],
    ['Save Folder',     WindowsInputTypes.Folder, None],
]
Values = Win.OptionsDialog("Image from Assembly", Option, 100)
if Values is None:
    sys.exit()  # user canceled

dimension_thumb = Values[0]  # e.g. 100
save_path      = Values[1]  # user-chosen folder

if not os.path.isdir(save_path):
    raise EnvironmentError("The selected folder does not exist: " + save_path)

debug_print("### DEBUG PRINT ###  Using dimension:", dimension_thumb)
debug_print("### DEBUG PRINT ###  Thumbnails and Excel will be in:", save_path)

###########################################################
# 3) DETECT ASSEMBLY OR PART
###########################################################
def detect_type():
    """
    Returns a tuple: (obj, typeString) 
    where typeString is 'Assembly' or 'Part'.
    """
    try:
        if hasattr(CurrentAssembly(), 'Parts'):
            return (CurrentAssembly(), 'Assembly')
        else:
            raise Exception("Not a valid assembly")
    except:
        if hasattr(CurrentPart(), 'Name'):
            return (CurrentPart(), 'Part')
        else:
            raise Exception("Document is neither valid Part nor Assembly")

###########################################################
# 4) ENUMERATE PARTS IN AN ASSEMBLY & COUNT QUANTITIES
###########################################################
Assembly_Name = None
Assembly_DNum = None

def count_parts_in_assembly(assembly):
    """
    Returns a dict { normalizedName : quantity }.
    Also sets global Assembly_Name and Assembly_DNum from the top-level.
    """
    parts_count = defaultdict(int)

    def process_asm(asm):
        global Assembly_Name
        global Assembly_DNum

        Assembly_Name = asm.Name or "Assembly"
        Assembly_DNum = asm.DocumentNumber or "NoDocNum"

        # Count top-level parts
        for p in asm.Parts:
            pname = normalize_part_name(p.Name)
            parts_count[pname] += 1

        # Sub-assemblies
        for sa in asm.SubAssemblies:
            sname = normalize_part_name(sa.Name)
            parts_count[sname] += 1
            process_asm(sa)  # recursion

    process_asm(assembly)
    return parts_count

###########################################################
# 5) THUMBNAIL GENERATION
###########################################################
def generate_thumbnails_with_quantities(assembly, parts_count, folderpath):
    """
    Saves a single thumbnail for each unique part/sub-assembly:
        {CleanedPartName};{CleanedDocNumber};{Quantity}.jpg
    """
    saved_thumbnails = set()

    def save_thumb(name, docnum, quantity, item_obj):
        """
        Actually do the SaveThumbnail to folderpath, with debug prints.
        """
        n_safe = name or "NoName"
        d_safe = docnum or "NoDocNum"

        c_name   = clean_file_name(n_safe)
        c_docnum = clean_file_name(d_safe)

        final_filename = "{};{};{}.jpg".format(c_name, c_docnum, quantity)
        path_out = os.path.join(folderpath, final_filename)

        geometry_hash = getattr(item_obj, 'GeometryHash', id(item_obj))
        unique_id = (final_filename, geometry_hash)

        if unique_id not in saved_thumbnails:
            debug_print("### DEBUG PRINT ###  Saving thumbnail:", path_out)
            item_obj.SaveThumbnail(path_out, dimension_thumb, dimension_thumb)
            saved_thumbnails.add(unique_id)
        else:
            debug_print("### DEBUG PRINT ###  Skipped duplicate thumbnail:", final_filename)

    def traverse_asm(asm):
        # parts
        for p in asm.Parts:
            p_name = normalize_part_name(p.Name)
            p_doc  = p.DocumentNumber
            p_qty  = parts_count[p_name]
            save_thumb(p_name, p_doc, p_qty, p)

        # sub-assemblies
        for sa in asm.SubAssemblies:
            sa_name = normalize_part_name(sa.Name)
            sa_doc  = sa.DocumentNumber
            sa_qty  = parts_count[sa_name]
            save_thumb(sa_name, sa_doc, sa_qty, sa)

            traverse_asm(sa)

    traverse_asm(assembly)

###########################################################
# 6) BUILD THE EXCEL WORKSHEET WITH IMAGES
###########################################################
def GenerateExcelWithImagesNET(image_directory):
    """
    1) Loops over all .jpg/.png/etc. in 'image_directory'.
    2) Splits filename on semicolons: "PartName;DocNum;Qty.jpg".
    3) Writes name, docnum, qty in columns A,B,D.
    4) Embeds the image in column C.
    5) Saves Excel as: "<Assembly_DNum> <Assembly_Name>.xlsx".
    """
    debug_print("### DEBUG PRINT ###  Scanning directory for thumbnails:", image_directory)

    excel = Excel.ApplicationClass()
    excel.Visible = False

    workbook = excel.Workbooks.Add()
    sheet = workbook.Worksheets[1]

    # HEADERS
    sheet.Cells[1, 1].Value2 = "Part Name"
    sheet.Cells[1, 2].Value2 = "Doc #"
    sheet.Cells[1, 3].Value2 = "Image"
    sheet.Cells[1, 4].Value2 = "Quantity"
    sheet.Cells[1, 5].Value2 = "Purchased"
    sheet.Cells[1, 6].Value2 = "Ready"

    sheet.Columns("C").ColumnWidth = 15

    row = 2
    valid_extensions = ('.jpg', '.jpeg', '.png', '.bmp', '.gif')

    # We'll make images about 75 points high/wide
    cell_size_points = 75

    all_files = os.listdir(image_directory)
    if not all_files:
        debug_print("### DEBUG PRINT ###  WARNING: No files found in folder:", image_directory)

    for filename in all_files:
        fn_lower = filename.lower()
        if fn_lower.endswith(valid_extensions):
            debug_print("### DEBUG PRINT ###  Found image file:", filename)

            base_no_ext, ext = os.path.splitext(filename)
            parts = base_no_ext.split(';')
            if len(parts) < 3:
                debug_print("### DEBUG PRINT ###  Skipping file (not enough semicolons):", filename)
                continue

            parted_name   = parts[0]
            parted_docnum = parts[1]
            parted_qty_str = parts[2]

            try:
                parted_qty = int(parted_qty_str)
            except:
                parted_qty = 1

            # Write data in columns A,B,D
            sheet.Cells[row, 1].Value2 = parted_name
            sheet.Cells[row, 2].Value2 = parted_docnum
            sheet.Cells[row, 4].Value2 = parted_qty

            # Row height for image
            sheet.Rows[row].RowHeight = cell_size_points

            image_path = os.path.join(image_directory, filename)
            left = sheet.Cells[row, 3].Left
            top  = sheet.Cells[row, 3].Top

            # Insert the picture
            picture = sheet.Shapes.AddPicture(
                Filename=image_path,
                LinkToFile=MsoTriState.msoFalse,
                SaveWithDocument=MsoTriState.msoTrue,
                Left=left,
                Top=top,
                Width=cell_size_points,
                Height=cell_size_points
            )

            row += 1

    sheet.Columns("A").AutoFit()
    sheet.Columns("B").AutoFit()

    global Assembly_DNum
    global Assembly_Name

    # If we never set them => single Part fallback
    if not Assembly_DNum:
        Assembly_DNum = "PART"
    if not Assembly_Name:
        Assembly_Name = "SINGLE"

    # Clean them for final path:
    Assembly_DNum  = clean_file_name(Assembly_DNum)
    Assembly_Name  = clean_file_name(Assembly_Name)

    excel_file_path = os.path.join(image_directory,
        "{} {}.xlsx".format(Assembly_DNum, Assembly_Name)
    )

    debug_print("### DEBUG PRINT ###  Saving Excel to:", excel_file_path)

    workbook.SaveAs(excel_file_path)
    workbook.Close(False)
    excel.Quit()

    debug_print("### DEBUG PRINT ###  Excel file with images created at:", excel_file_path)

###########################################################
# 7) MAIN
###########################################################
def Main():
    try:
        doc_obj, doc_type = detect_type()
    except Exception as exc:
        print("Error detecting Part or Assembly:", exc)
        return

    debug_print("### DEBUG PRINT ###  Detected type:", doc_type)

    if doc_type == 'Part':
        debug_print("### DEBUG PRINT ###  Single Part scenario.")
        part = doc_obj
        c_name  = clean_file_name(part.Name or "Part")
        c_docno = clean_file_name(part.DocumentNumber or "NoDocNum")
        final_filename = "{};{};1.jpg".format(c_name, c_docno)
        path_out = os.path.join(save_path, final_filename)

        debug_print("### DEBUG PRINT ###  Saving Part thumbnail:", path_out)
        part.SaveThumbnail(path_out, dimension_thumb, dimension_thumb)

    else:
        debug_print("### DEBUG PRINT ###  Assembly scenario: Counting parts.")
        parts_count = count_parts_in_assembly(doc_obj)

        debug_print("### DEBUG PRINT ###  Generating thumbnails with doc # + quantity.")
        generate_thumbnails_with_quantities(doc_obj, parts_count, save_path)

    debug_print("### DEBUG PRINT ###  Building Excel sheet from generated images.")
    GenerateExcelWithImagesNET(save_path)

Main()

```