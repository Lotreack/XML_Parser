import os


def createFolderForTiff(folder_name, path):
    _fold_name = folder_name.replace(":", "").replace(".", "")
    _path = path

    if not (os.path.exists(_path + "/" + folder_name)):
        os.chdir(_path)
        os.mkdir(_fold_name)
    else:
        print("Папка с именем" + folder_name + "уже существует")


folder_names = [
    "2020-07-23 16-25-22 (22:24:14.352)",
    "2020-07-22 16-25-22 (22:24:14.352)",
    "2020-07-25 16-25-22 (22:24:14.352)",
    "2020-07-28 16-25-22 (22:24:14.352)",
    "2020-08-07 16-25-22 (22:24:14.352)",
    "2020-07-29 16-25-22 (22:24:14.352)",
]


path = "D:/temp"

for name in folder_names:
    createFolderForTiff(name, path)
