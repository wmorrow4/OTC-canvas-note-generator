# OTC-canvas-note-generator
Contains code for generating canvassing notes.

REQUIREMENTS:
Python (I'm using version 3, but will likely work on python version 2)
Pandas module for python (to get on ubuntu: 'pip install pandas' or 'pip3 install pandas' if using python3

Using the canvassing note generator (I'm using ubuntu 20.04, but should work on anything that can run python):
-Download the Park at Napoli tenants info as an xlsx file.
-Put the xlsx file in the same directory as 'canvas_gen.py'
-Navigate to the directory of canvas_gen.py in terminal
-python canvas_gen.py '<xlsx filename>'
  
The program will spit out a tenant_info.txt that contains the new note info.
