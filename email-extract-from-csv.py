#Ryan Geddes 2020.  All rights reserved
#Email Address Extract From Source CSV Files
import csv
#Loops Through First Column Of CSV And Writes Output
#Change Column Number To Match Email Data And CSV IN Ad Outfile
with open('0324-401.txt', 'r') as userFile:
    userFileReader = csv.reader(userFile)
    with open('03240401-emailsonly-out.txt', 'w+') as f:
        for row in userFileReader:
            print(row[0], file=f)
