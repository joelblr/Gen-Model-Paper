import os
import sys
import csv
import random
from datetime import datetime


""" partName: str, freq: int, unique-KeyIndex|ValueIndex: int, limit: int = 1"""
def getPart(fileName, freq, uniKeyIdx, uniValIdx, limit, used_ids, partId) :

    """
    TODO: make unique based on multi-Column
            like, year + chapter + pgNum

    #XXX: handle Errors
    """
 
    with open(fileName) as csvf :
        """ (year, chapter, question) """
        lines = [tuple(line) for line in csv.reader(csvf)]

    used_ids["total"][partId] = len(lines)-1
    counter = {line[uniKeyIdx] : [] for line in lines}
    res = []
    for i in range(freq) :

        flag = True
        while flag :

            ques = random.choices(lines[1:])[0]
            key1 = ques[uniKeyIdx]
            key2 = ques[uniValIdx]

            if (len(counter[key1]) >= limit) :
                counter[key1] = []

            if (len(used_ids[partId]) == used_ids["total"][partId]) :
                used_ids[partId] = set()
                used_ids["done"][partId] = True

            if (key2 not in used_ids[partId]) :
                res.append(ques)
                used_ids[partId].add(key2)
                counter[key1].append(key2)
                flag = False

    # for i, t in enumerate(res) :
    #     print(i, t)

    if (len(used_ids[partId]) == used_ids["total"][partId]) :
        used_ids[partId] = set()
        used_ids["done"][partId] = True

    # List[tuple(str, str, str), ]
    return res


""" placeholder_prefix: str, val_format_type: str, csv_object: List[List[str, str]]
    -> List[List[str, str]]
"""
def getJsonFormat(placeholder_prefix, val_format_type, csv_object) :
    json_res = []

    for idx, row in enumerate(csv_object) :
        json_res.append([
            f"{placeholder_prefix}{idx+1}",
            val_format_type.format(*row)
        ])

    # for key, val in json_res :
    #     print(key, val)

    return json_res


""" relative_path: str -> str """
def resource_path(relative_path) :

    try :
        base_path = sys._MEIPASS
    except Exception :
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


""" relative_path: str, prefix_dir: str """
def openDoc(relative_path, prefix_dir) :

    file_path = resource_path(f'{prefix_dir}/{relative_path}')
    print(file_path)

    if os.path.exists(file_path) :
        if os.name == "nt":  # Windows
            os.startfile(file_path)
        elif os.name == "posix":  # Linux or macOS
            os.system("xdg-open " + file_path)
    else :
        print("File not found")


""" obj: dict(str: str), new_obj: dict(str: str) """
def updateObject(obj, new_obj) :
    for key, val in new_obj :
        obj[key] = val


""" doc: DocxTemplate, folder_path: str, prefix_tpl: str -> str """
def saveFile(doc, folder_path, prefix_tpl) :

    newfile = prefix_tpl + datetime.now().strftime("%S%M") + ".docx"
    newfile = resource_path(folder_path +"/" + newfile)

    if not os.path.exists(folder_path) :
        os.system("mkdir -p " + folder_path)
    doc.save(newfile)

    return newfile


""" folder_path: str -> None """
def open_file_explorer(folder_path) :

    if os.path.exists(folder_path) :
        if os.name == "nt":  # Windows
            os.system("start explorer " + folder_path)
        elif os.name == "posix":  # Linux or macOS
            os.system("xdg-open " + folder_path)
    else :
        print("File not found")