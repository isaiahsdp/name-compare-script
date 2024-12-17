# Name Compare Python Script (Excel)

This Python script compares names between two Excel files to check for matches.

- The first Excel file contains the names you want to verify.
- The second Excel file contains the list of names to search for
- The script updates the first Excel file by adding a new column with x for matched names and 0 for unmatched names.

- compareST.py reads names split into two columns, column 0: First Name, column 1: Last Name
- compareCC.py reads names put into a singular column in the format "Last Name, First Name"

# Steps

### Make sure Python 3 is installed
Verify Installation in your terminal: python3 --version

#### Install required Python libraries
Terminal: pip install pandas openpyxl

#### Put your Excel files in the same directory as compareCC.py or compareST.py

#### Update file/Excel destinations in compareCC.py or compareST.py (fields have #CHANGE comments)

#### Open your terminal and cd to the directory
ex. cd Desktop/name-compare-script or cd Downloads/name-compare-script

#### In the terminal run "python3 compareCC.py" or "python3 compareST.py" (depending on what you are using)
