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
### 5. Install virtualenv with pip
  $ pip install virtualenv
  ### Install virtual environment in the directory
  $ python3 -m virtualenv venv
### 6.Activate the virtual environment
  $ source venv/bin/activate
### 7.Confirm the python version is 3.8+ by running 
  $ python --version
### 8.Install the requirements
  $ pip install -r requirements.txt

## How to run the script
### 1.Navigate into the script directory
  $ cd arks
### 2.Activate the virtual environment
  $ source venv/bin/activate
### 3.Run the script to generate ARKS for all items in your csv file
  $ python simple_ark.py
### 4.You will be prompted for the file path that contains the csvs for the manuscripts
  $ [path to file]
### 5.You will be prompted for the ARK shoulder (this is a dummy ark reserved for testing)
  $ ark:/99999/fk4
### 6.You will be prompted for the password for EZID
  $ see confluence
You can replace ark:/99999/fk with whatever ARK shoulder you want to use 
The script will now generate the ARKs. Once the script is finished running there will be another export file in the directory.
