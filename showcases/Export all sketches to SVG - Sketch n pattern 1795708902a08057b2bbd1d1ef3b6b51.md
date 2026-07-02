# Export all sketches to SVG - Sketch<n> pattern

ID: A7246742B-17
Programming Language: Alibre Script, IronPython2.7
LLM or AI Product: CustomChatGPT
By StephenBot: No
Status: Done
Category: Testbed
Reviewed: No
Created time: January 12, 2025 12:56 AM
AI summary: Exports all 2D sketches named 'Sketch<1>', 'Sketch<2>', etc., from the current part to SVG files, up to 50 sketches. Handles unsaved parts and errors when sketches are not found.

```python
def export_all_sketches_guessing_names():
    """
    Attempts to export every 2D sketch named 'Sketch<1>', 'Sketch<2>', etc.,
    up to some range, from the currently open part. 
    This includes sketches not used by features, 
    but also can produce errors if the name doesn't exist.
    """

    Win = Windows()
    
    # Attempt to get the current part
    try:
        part_obj = CurrentPart()
    except:
        print("Not a part. Canceling.")
        return

    # If part is new/unsaved, prompt user to save
    if not part_obj.FileName:
        folder = Win.SelectFolderDialog("", "Save new part to export sketches?")
        if not folder:
            print("Canceled. No export.")
            return
        part_obj.Save(folder)

    import os
    folder_path = os.path.dirname(part_obj.FileName)

    # Let's define an upper bound. We'll guess up to 50 sketches.
    # Increase if your design might have more.
    max_sketches = 50
    exported_count = 0

    for i in range(1, max_sketches+1):
        sketch_name = "Sketch<{}>".format(i)
        try:
            sketch_obj = part_obj.GetSketch(sketch_name)
            svg_path = os.path.join(folder_path, "Sketch_{}.svg".format(i))
            sketch_obj.ExportSVG(svg_path)
            print("Exported:", sketch_name, "=>", svg_path)
            exported_count += 1
        except:
            # means the sketch name wasn't found or error exporting
            pass
    
    print("Done. Exported {} sketches as .svg in total.".format(exported_count))

# Usage:
# export_all_sketches_guessing_names()

```