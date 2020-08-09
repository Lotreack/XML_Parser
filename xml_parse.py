import os
import sys
import xml.etree.ElementTree as ET


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


script_path = os.path.abspath(os.path.dirname(sys.argv[0]))


path_to_XML = script_path + "\\XML"
files_list = os.listdir(path_to_XML)


all_batch_Names = []
for filename in files_list:
    all_batch_Names.append(getBatchNameFromXml(path_to_XML + "\\" + filename))

print(all_batch_Names)

