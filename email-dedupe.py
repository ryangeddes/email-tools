##Email De-Dupe Python 3##
##Ryan Geddes, Quadrant Media, 2020##
email_seen = set()
outfile = open("03240401-deduped.txt", "w+")
for row in open("03240401-emailsonly-out.txt", "r"):
    if row not in email_seen:
        outfile.write(row)
        email_seen.add(row)
outfile.close()