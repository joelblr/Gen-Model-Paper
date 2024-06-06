"""
TODO: Run a While-Infinite Loop, Cache all used Qs to form N Unique papers
"""

# from docx import Document
from docxtpl import DocxTemplate
from brain import *
from random import randint


pre_idx = 1
# to create as many unique papers as possible
while not all(used_ids["done"]) :

    # GET some inputs from GUI <standard, whichLessonsToFocus...>
    context = {
        "year" : inputs['year'],
        "standard" : inputs['standard'],
    }

    tpl_name = resource_path(rectifiedPath(myDirs["tpl"], inputs["tpl"]))
    doc = DocxTemplate(tpl_name)


    csv_file, part_qs = [], []
    csv_name = resource_path(rectifiedPath(myDirs[".csv"], 'Part_A.csv'))
    csv_file = getPart(csv_name, *parts_map[0], 0)
    part_qs = getJsonFormat(["part_A"], ["{3}"], csv_file)
    updateObject(context, part_qs)

    csv_file, part_qs = [], []
    csv_name = resource_path(rectifiedPath(myDirs[".csv"], 'Part_B2.csv'))
    csv_file = getPart(csv_name, *parts_map[1], 1)
    part_qs = getJsonFormat(["part_B", "part_B1"], ["{4} ({2} -> {3}) [{1}]", "{5}"], csv_file)
    updateObject(context, part_qs)


    for i, c in enumerate("CDEF") :
        csv_file, part_qs = [], []
        csv_name = resource_path(rectifiedPath(myDirs[".csv"], f'Part_{c}.csv'))
        csv_file = getPart(csv_name, *parts_map[i+2], i+2)
        part_qs = getJsonFormat([f"part_{c}"], ["{4} ({2} -> {3}) [{1}]"], csv_file)
        updateObject(context, part_qs)

    csv_file, part_qs = [], []
    csv_name = resource_path(rectifiedPath(myDirs[".csv"], 'Part_G.csv'))
    csv_file = getPart(csv_name, *parts_map[6], 6)
    part_qs = getJsonFormat(["part_G"], ["{2} [{1}]"], csv_file)
    updateObject(context, part_qs)


    doc.render(context)

    newFileName = saveFile(doc, myDirs["mqp"], inputs['prefix_tpl'] + f"{pre_idx}_")

    # openDoc(newFileName, myDirs["mqp"])
    pre_idx += 1

print("Successfully Downloaded all the Possible Model-Papers")
print("Check it Out in:")
print("\t", myDirs["mqp"])
open_file_explorer(myDirs["mqp"])