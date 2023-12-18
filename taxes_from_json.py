# Read inputs from json file. Generate federal and california state
# tax lines and print.
# Add the desired year tax directory to the PYTHONPATH

import sys
import json
# If the following import fails, add the appropriate year directory to the
# PYTHONPATH
from f1040 import F1040
from ca540 import CA540

# Get the filename from the first argument
try:
    filename = sys.argv[1]
except IndexError:
    print("Error: Please provide a JSON file path as the first argument.")
    sys.exit(1)

# Read the JSON file
try:
    with open(filename, 'r') as f:
        data = json.load(f)
except FileNotFoundError:
    print(f"Error: File '{filename}' not found.")
    sys.exit(1)

fm = F1040(data)
fm.printAllForms()
print('')
ca = CA540(data, fm)
ca.printAllForms()
