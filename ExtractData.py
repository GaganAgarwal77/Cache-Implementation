import os

# get's the directory in which this file is
abs_path = os.path.dirname(__file__)
traces = "Trace Files/traces"
paths = [""]*5
results = [""]*5
fileNames = ["gcc.trace", "gzip.trace",
             "mcf.trace", "swim.trace", "twolf.trace"]
# getting each of the file's path
for i in range(5):
    paths[i] = os.path.join(abs_path, traces, fileNames[i])

for i in range(5):
    f = open(paths[i], "r")  # opening every file
    rows = f.readlines()
    results[i] = []
    for row in rows:  # going through each row and selecting the terms in the middle column and adding them to the array
        results[i].append(row.split(' ')[1])
    f.close()
  
