
"""
TODO: Run a While-Infinite Loop, Cache all used Qs to form N Unique papers
"""

# from docx import Document
from docxtpl import DocxTemplate
from brain import *
from random import randint

# GET as INPUT-GUI
inputs = {
    "prefix_tpl" : "model-paper",
    "year" : "2025*",
    "saveas" : "",#as a separate dir for the test papers generated per one run
}

## TODO: use path reference used by Python-Simplified
myDirs = {
    "pwd" : '.',
    "csv" : "data-sets",
    "tpl" : "templates",
    "mqp" : "model-paper",
}

#templates-map
tpls = {
    "SS": "SS_Template.docx",
}

# GET some inputs from GUI <std, whichLessonsToFocus...>
context = {
    "year" : inputs['year'],
    "std" : "Senior 1",
}

doc = DocxTemplate(f'{myDirs["tpl"]}/{tpls["SS"]}')

csv, part_qs = [], []
csv = getPart(f'{myDirs["csv"]}/{context["std"]}/Part_A.csv', 10, 0, 5)
part_qs = getJsonFormat("part_a", "{2}", csv)
updateObject(context, part_qs)

#TODO: PART B

csv, part_qs = [], []
csv = getPart(f'{myDirs["csv"]}/{context["std"]}/Part_C.csv', 10, 1, 1)
part_qs = getJsonFormat("part_c", "{3} ({1} -> {2}) [{0}]", csv)
updateObject(context, part_qs)


csv, part_qs = [], []
csv = getPart(f'{myDirs["csv"]}/{context["std"]}/Part_D.csv', 6, 1, 1)
part_qs = getJsonFormat("part_d", "{3} ({1} -> {2}) [{0}]", csv)
updateObject(context, part_qs)


csv, part_qs = [], []
csv = getPart(f'{myDirs["csv"]}/{context["std"]}/Part_E.csv', 3, 1, 1)
part_qs = getJsonFormat("part_e", "{3} ({1} -> {2}) [{0}]", csv)
updateObject(context, part_qs)


csv, part_qs = [], []
csv = getPart(f'{myDirs["csv"]}/{context["std"]}/Part_F.csv', 2, 1, 1)
part_qs = getJsonFormat("part_f", "{3} ({1} -> {2}) [{0}]", csv)
updateObject(context, part_qs)


csv, part_qs = [], []
csv = getPart(f'{myDirs["csv"]}/{context["std"]}/Part_G.csv', 1, 1, 1)
part_qs = getJsonFormat("part_g", "{1} [{0}]", csv)
updateObject(context, part_qs)


doc.render(context)

newFileName = saveFile(doc, myDirs["mqp"], inputs['prefix_tpl'])

openDoc(newFileName, myDirs["mqp"])
