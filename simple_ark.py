import csv
import os
import subprocess
import pandas as pd

works_file = raw_input('File:')
ark_shoulder = raw_input('ARK shoulder:')
parent_ark_list = []
output_file = 'ark_export.csv'
cmd_ezid = ['python', 'batch-register.py', '-c', 'ucla-library', '-s', ark_shoulder, 'mint', 'mappings.txt', works_file]
parent_ark = subprocess.Popen(cmd_ezid, stdout=subprocess.PIPE).communicate()[0]
parent_ark = (str(parent_ark))
items_list = parent_ark.split(',')
for i in items_list:
    if 'ark:/' in i:
        parent_ark_list.append(i)
df_list = parent_ark_list[1:]
empty_column = []

data= pd.read_csv(works_file, sep=',', delimiter=None, header='infer')
data = data.drop("Parent ARK", axis=1)
data = data.drop("Rights.copyrightStatus", axis=1)
data = data.drop("Type.typeOfResource", axis=1)
data = data.drop("ark_number", axis=1)
data["Parent ARK"] = None
data["Rights.copyrightStatus"] = None
data["Type.typeOfResource"] = None
data.insert(6,'Item Ark', df_list)
data.to_csv(path_or_buf=output_file, sep=',', na_rep='', float_format=None, index=False)
