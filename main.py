"""
TODO: Run a While-Infinite Loop, Cache all used Qs to form N Unique papers
"""

# from docx import Document
from docxtpl import DocxTemplate
from brain import *
from random import randint

# GET as INPUT-GUI
inputs = {
    "prefix_tpl" : input("Enter the Folder Name: ")+"-",
    "year" : "2025*",
    "saveas" : "",#as a separate dir for the test papers generated per one run
}

## TODO: use path reference used by Python-Simplified
myDirs = {
    "pwd" : '.',
    ".csv" : "data-sets",
    "tpl" : "templates",
    "mqp" : resource_path("model-paper/"+inputs["prefix_tpl"][:-1]),
}


# contains set of used-IDs for a given Section/Part A->0, B->1... G->6
used_ids = {i : set() for i in range(7)}
# total Qs in each part
used_ids["total"] = [0 for i in range(7)]
#part_B
used_ids["done"] = [False for i in range(7)]
used_ids["done"][1] = True

pre_idx = 1
# to create as many unique papers as possible
while not all(used_ids["done"]) :

    #templates-map
    tpls = {
        "SS": "SS_Template.docx",
    }

    # GET some inputs from GUI <std, whichLessonsToFocus...>
    context = {
        "year" : inputs['year'],
        "std" : "Senior 1",
    }

    tpl_name = resource_path(f'{myDirs["tpl"]}/{tpls["SS"]}')
    doc = DocxTemplate(tpl_name)

    parts_map = {
        0 : (10, 1, 0, 5),
        # 1 : (),
        2 : (10, 2, 0, 1),
        3 : (6, 2, 0, 1),
        4 : (3, 2, 0, 1),
        5 : (2, 2, 0, 1),
        6 : (1, 0, 0, 1),
    }


    csv_file, part_qs = [], []
    csv_name = resource_path(f'{myDirs[".csv"]}/{context["std"]}/Part_A.csv')
    csv_file = getPart(csv_name, *parts_map[0], used_ids, 0)
    part_qs = getJsonFormat("part_A", "{3}", csv_file)
    updateObject(context, part_qs)

    #TODO: PART B
    for i, c in enumerate("CDEF") :
        csv_file, part_qs = [], []
        csv_name = resource_path(f'{myDirs[".csv"]}/{context["std"]}/Part_{c}.csv')
        csv_file = getPart(csv_name, *parts_map[i+2], used_ids, i+2)
        part_qs = getJsonFormat(f"part_{c}", "{4} ({2} -> {3}) [{1}]", csv_file)
        updateObject(context, part_qs)

    csv_file, part_qs = [], []
    csv_name = resource_path(f'{myDirs[".csv"]}/{context["std"]}/Part_G.csv')
    csv_file = getPart(csv_name, *parts_map[6], used_ids, 6)
    part_qs = getJsonFormat("part_G", "{2} [{1}]", csv_file)
    updateObject(context, part_qs)


    doc.render(context)

    newFileName = saveFile(doc, myDirs["mqp"], inputs['prefix_tpl'] + f"{pre_idx}_")

    # openDoc(newFileName, myDirs["mqp"])
    pre_idx += 1

print("Successfully Downloaded all the Possible Model-Papers")
print("Check it Out in:")
print("\t", myDirs["mqp"])
open_file_explorer(myDirs["mqp"])