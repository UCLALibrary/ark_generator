# ark_generator

## Purpose of script:
Mints an ARK for items in the csv file. The script dynamically generates another file to populate metadata and form the structure of the ARK.

## Initial setup
### 1.Make a new directory on your computer
  $ mkdir arks
### 2.Navigate into that directory
  $ cd arks
### 3.Clone the github repo above into that directory
  $ git clone https://github.com/UCLALibrary/ark_generator.git
### 4. Navigate into ark_generator directory
  $ cd ark_generator
### 5.Use pip2 to create a virtual environment
  $ pip2 install virtualenv### Activate virtual environment
   $ virtualenv venv
### 6.Activate the virtual environment
  $ source venv/bin/activate
### 7.Confirm the python version is 2.7 by running 
  $ python --version
### 8.Install the requirements
  $ pip2 install -r requirements.txt

## How to run the script
### 1.Navigate into the script directory
  $ cd arks
### 2.Activate the virtual environment
  $ source venv/bin/activate
### 3.Run the script to generate ARKS for all items in youer csv file
  $ python simple_ark.py
### 4.You will be prompted for the file path that contains the csvs for the manuscripts
  $ [path to file]
### 5.You will be prompted for the ARK shoulder (this is a dummy ark)
  $ ark:/99999/fk
### 6.You will be prompted for the password for EZID
  $ see confluence
You can replace ark:/99999/fk with whatever ARK shoulder you want to use 
The script will now generate the ARKs and NOIDs. Once the script is finished running there will be another export file in the directory.
