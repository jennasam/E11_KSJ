import csv
import numpy as np
import time

file = open("test.csv", "w", newline = "")

file_writer = csv.writer(file)

file_writer.writerow(["Time", "Data"]) # writerow tells pandas to write the first row, which is the metadata (names of stuff)

for i in range(10):
    entry = np.random.random()
    now = time.time
    file_writer.writerow([now, entry])

file.close() # don't forget to close your files