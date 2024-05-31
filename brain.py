""" partName: str, freq: int, uniIdx: int, limit: int = 1"""
def getPart(fileName, freq, uniIdx, limit=1) :

    """
    TODO: make unique based on multi-Column
            like, year + chapter + pgNum
    """

    import csv
    import random

    #XXX: handle Errors
    with open(fileName) as csvf :
        """ (year, chapter, question) """
        lines = [tuple(line) for line in csv.reader(csvf)]


    counter = {line[uniIdx] : 0 for line in lines}
    res = []
    for i in range(freq) :

        flag = True
        while flag :
            ques = random.choices(lines[1:])[0]
            key = ques[uniIdx]

            # if Chapter Undefined or not Repeated
            if key == "" or counter[key] < limit :
                res.append(ques)
                counter[key] += 1
                flag = False

    for i, t in enumerate(res) :
        print(i, t)

    # List[tuple(str, str, str), ]
    return res


""" placeholder_prefix: str, val_format_type: str, csv_object: List[List[str, str]] """
def getJsonFormat(placeholder_prefix, val_format_type, csv_object) :
    json_res = []

    for idx, row in enumerate(csv_object) :
        json_res.append([
            f"{placeholder_prefix}{idx+1}",
            val_format_type.format(*row)
        ])

    for key, val in json_res :
        print(key, val)

    return json_res


""" newfile: str, prefix_dir: str """
def openDoc(newfile, prefix_dir) :
    import os
    os.system(f'open "{prefix_dir}/{newfile}" &')
    # os.system("open " + prefix_dir + newfile + " &")


""" obj: dict(str: str), new_obj: dict(str: str) """
def updateObject(obj, new_obj) :
    for key, val in new_obj :
        obj[key] = val


""" doc: DocxTemplate, prefix_dir: str, dirName: str """
def saveFile(doc, prefix_dir, prefix_tpl) :
    from datetime import datetime

    newfile_name = prefix_tpl + datetime.now().strftime("%S%M")
    newfile_extn = ".docx"

    newfile = newfile_name + newfile_extn
    try :
        doc.save(f'{prefix_dir}/{newfile}')
    except :
        import os
        os.system("mkdir " + prefix_dir)
        doc.save(f'{prefix_dir}/{newfile}')

    return newfile
