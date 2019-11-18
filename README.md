# ark_generator

Purpose of script
Loop through a set of files in a directory
Mints an ARK for items in the csv file
The script dynamically generates another file to populate metadata and form the structure of the ARK.

Initial setup
Make a new directory on your computer
  $ mkdir manuscript_arks
Navigate into that directory
  $ cd manuscript_arks
Clone the github repo above into that directory
  $ git clone 
Use pip2 to create a virtual environment
  $ pip2 install virtualenv
$ virtualenv venv
Activate the virtual environment
  $ source venv/bin/activate
Confirm the python version is 2.7 by running 
  $ python --version
Navigate down into the SLDP_ARK_mint directory
$ cd 
Install the requirements
  $ pip2 install -r requirements.txt

How to run the script
Navigate into the script directory
  $ cd manuscript_arks
Activate the virtual environment
  $ source venv/bin/activate
Navigate down into the SLDP_ARK_mint directory
  $ cd 
Run the script to generate ARKS for all items in youer csv file
  $ python sinai_work_page_ark.py
You will be prompted for the file path that contains the csvs for the manuscripts
  $ [path to file]
You will be prompted for the ARK shoulder
  $ ark:/21198/z1
You will be prompted for the username and password for EZID
  $ see confluence
You can replace ark:/21198/z1 with whatever ARK shoulder you want to use (the example given is the "UCLA Digital Library ARK")
The script will now generate the ARKs and NOIDs. Once the script is finished running the input files will contain Item ARKs and Parent ARKs(for page csvs).
