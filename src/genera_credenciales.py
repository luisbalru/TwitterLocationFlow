import json
import sys

C_URL = sys.argv[1]
C_USER = sys.argv[2]
C_PASS = sys.argv[3]

data = {'C_URL': C_URL, 'C_USER' : C_USER, 'C_PASS' : C_PASS}

with open('data.txt', 'w') as outfile:
	json.dump(data,outfile)
