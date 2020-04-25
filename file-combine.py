# Email List Merger
# Ryan Geddes, Quadrant Media, 2020

data = data2 = ""

# Reading data from file1
with open('17-out.txt') as fp:
    data = fp.read()

# Reading data from file2
with open('18-out.txt') as fp:
    data2 = fp.read()

# Merging 2 Files With New Line
data += "\n"
data += data2

with open ('1718combined.txt', 'w') as fp:
    fp.write(data)