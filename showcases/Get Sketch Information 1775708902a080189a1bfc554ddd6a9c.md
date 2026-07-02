# Get Sketch Information

ID: A7246742B-1
Programming Language: Alibre Script, IronPython2.7
LLM or AI Product: CustomChatGPT
By StephenBot: No
Status: Done
Category: Testbed
Reviewed: No
Created time: January 9, 2025 7:56 PM
AI summary: Python script that finds and lists a part's 3D sketches matching a naming pattern, catches exceptions for sketches that don't exist, and prints details about the found sketches and their figures.

```python
def find_3d_sketches(part, sketch_format="3DSketch<{}>", max_sketches=50):
    found = []
    for i in range(1, max_sketches+1):
        sketch_name = sketch_format.format(i)
        try:
            sk3d = part.Get3DSketch(sketch_name)
            if sk3d is not None:
                found.append(sk3d)
        except:
            pass
    return found

def main():
    part = CurrentPart()
    if not part:
        print("No active part found. Open a part first.")
        return

    # Change this string if your 3D sketches use a different pattern:
    # e.g. "3D Sketch<{}>", "3D-Sketch<{}>", or "3D Skizze<{}>"
    three_d_sketch_pattern = "3D Sketch<{}>"

    sketches_3d = find_3d_sketches(part, sketch_format=three_d_sketch_pattern, max_sketches=50)
    if not sketches_3d:
        print("No 3D sketches found matching '%s'." % three_d_sketch_pattern)
        return

    for sk in sketches_3d:
        print("----------------------------------------")
        print("  Found 3D Sketch:", sk.Name)
        figures = sk.Figures
        print("  Number of figures:", len(figures))
        for idx, fig in enumerate(figures):
            print("    Figure {}: {}".format(idx+1, type(fig)))

    print("Done!")

main()
```