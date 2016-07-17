##########################################################################################
# I/O functions
##########################################################################################

import csv
import numpy as np

def readTrainFile(filepath):
	data = []
	with open(filepath, 'rb') as dataFile:
		dataReader = csv.reader(dataFile, delimiter = ',')
		dataReader.next()
		for row in dataReader:
			data.append(row)
		data = np.array(data)
		return data.astype(np.int)