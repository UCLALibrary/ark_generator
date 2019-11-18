import csv
import os
import subprocess
import pandas as pd


#creates a mappings file that provides metadata to EZID
def create_mappings():

    title = row['P_number']
    mappings_file = open("mappings.txt", "w+")
    string = 'erc.who: UCLA Library', ('\nerc.what: '+str(title))
    for s in string:
        mappings_file.write(s)


works_file = raw_input('File:')
ark_shoulder = raw_input('ARK shoulder:')
ezid_input = raw_input('EZID username and password:')
parent_ark_list = []
output_file = 'ark_export.csv'
works_cursor = csv.DictReader(open(works_file),
    delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)

for row in works_cursor:
    create_mappings()
    cmd_ezid = ['python', 'ezid.py', ezid_input, 'mint', ark_shoulder, '@', 'mappings.txt']
    parent_ark = subprocess.Popen(cmd_ezid, stdout=subprocess.PIPE).communicate()[0]
    parent_ark = (str(parent_ark)).replace('success: ', '')
    parent_ark_list.append(parent_ark)
    
data= pd.read_csv(works_file, sep=',', delimiter=None, header='infer')
data = data.drop("ark_number", axis=1)
data.insert(2,'ark_number', parent_ark_list)
data.to_csv(path_or_buf=output_file, sep=',', na_rep='', float_format=None, index=False)
