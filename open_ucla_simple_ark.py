import csv
import os
import subprocess
import pandas as pd

works_file = input('File:')
ark_shoulder = input('ARK shoulder:')
parent_ark_list = []
output_file = 'ark_export.csv'
cmd_ezid = ['python', 'batch-register3.py', '-c', 'ucla-library', '-s', ark_shoulder, 'mint', 'mappings.txt', works_file]
parent_ark = subprocess.Popen(cmd_ezid, stdout=subprocess.PIPE).communicate()[0]
parent_ark = (str(parent_ark))
items_list = parent_ark.split(',')
for i in items_list:
    if 'ark:/' in i:
        parent_ark_list.append(i)
df_list = parent_ark_list[1:]
data= pd.read_csv(works_file, sep=',', delimiter=None, header='infer')
#remove any existing item ARK columns, plus other for open UCLA collections
cols_to_drop = ['ark_number', 'Item Ark', 'Item ARK', 'Parent ARK', 
                'Rights.copyrightStatus', 'Type.typeOfResource']
for col in cols_to_drop:
    if col in data:
        data = data.drop(col, axis=1)
data['Parent ARK'] = None
data['Rights.copyrightStatus'] = None
data['Type.typeOfResource'] = None
data['Item Ark'] = df_list	
data.to_csv(path_or_buf=output_file, sep=',', na_rep='', float_format=None, index=False)
