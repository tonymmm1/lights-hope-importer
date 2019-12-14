<h1>Release 0.1.0</h1>

<h2>Light's Hope Importer</h2>

This program will read in mysql credentials and then extract json information about characters and realms and store them as designated files. Then the program will import all character information into database. The program will only run once since it checks for the existance of ./realms and files inside. Afterwards json files can be edited and or imported manually.

<h2>Requirements:</h2>

- python 3.6
- python pip
- mysql-connector-python

<h2>Installation:</h2>

1. Install python 3.6 on your distro</h3>
2. Install python pip</h3>
3. pip install mysql-connector-python</h3>

<h2>Executing program:</h2>

1. chmod +x lh-import.py (python lh-import.py)
2. ./lh-import.py
