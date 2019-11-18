# ark_generator

##Purpose of script:
Loop through a set of files in a directory
Mints an ARK for items in the csv file
The script dynamically generates another file to populate metadata and form the structure of the ARK.

##Initial setup
###1.Make a new directory on your computer
  $ mkdir arks
###2.Navigate into that directory
  $ cd arks
###3.Clone the github repo above into that directory
  $ git clone https://github.com/UCLALibrary/ark_generator.git
###4.Use pip2 to create a virtual environment
  $ pip2 install virtualenv
$ virtualenv venv
###5.Activate the virtual environment
  $ source venv/bin/activate
###6.Confirm the python version is 2.7 by running 
  $ python --version
###7.Install the requirements
  $ pip2 install -r requirements.txt

##How to run the script
###1.Navigate into the script directory
  $ cd arks
###2.Activate the virtual environment
  $ source venv/bin/activate
###3.Run the script to generate ARKS for all items in youer csv file
  $ python simple_ark.py
###4.You will be prompted for the file path that contains the csvs for the manuscripts
  $ [path to file]
###5.You will be prompted for the ARK shoulder
  $ ark:/21198/z1
###6.You will be prompted for the username and password for EZID
  $ see confluence
You can replace ark:/21198/z1 with whatever ARK shoulder you want to use (the example given is the "UCLA Digital Library ARK")
The script will now generate the ARKs and NOIDs. Once the script is finished running the input files will contain Item ARKs and Parent ARKs(for page csvs).
