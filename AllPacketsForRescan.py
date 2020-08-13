import io
import ie
import os
import sys
import xml.etree.ElementTree as ET
import ie as regular_expression

script_path = os.path.abspath(os.path.dirname(sys.argv[0]))

path_to_XML = script_path + "\\XML"

files_list = os.listdir(path_to_XML)


def getBatchNameFromXml(XML_path):
    try:
        tree = ET.parse(XML_path)
        importSession = tree.getroot()
        bathes = importSession.find("Bathes")
        batch = bathes[0].attrib
        name = batch.get("Name")
        return name

    except IOError as e:
        print(e)


batch_Names_from_XML = []

for file in files_list:

    batch_Names_from_XML.append(path_to_XML + file)


dictionary = {}
folders_name = []

count_founded_packets = 0

for elem, file in enumerate(files_list):

    tmp = {
        file.replace(".XML", ""): batch_Names_from_XML[elem]
        .replace(":", "")
        .replace(".", "")
    }
    dictionary.update(tmp)
    folders_name.append(file.replace(".XML", ""))


def delete_unnecessary(listdir, folder):

    unnecessary_files = []

    for file in listdir:
        if not regular_expression.search("^ \\d+\\ .tif$", file):
            os.remove(script_path + "TIFFs/" + folder + "/" + file)


for folder in folders_name:

    path_to_search_tiff = script_path + data_directory + "/" + folder + "/200/"

    path_to_copy_tiff = script_path + "TIFFs" + dictionary[folder]

    try:
        shutil.copytree(path_to_search_tiff, path_to_copy_tiff)
        files_for_delete = os.listdir(path_to_copy_tiff + "/")
        delete_unnecessary(files_for_delete, dictionary[folder])

    except IOError as e:
        print("Done ", e)
        continue
