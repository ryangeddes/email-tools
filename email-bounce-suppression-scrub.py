#Email Bounce And Suppression List Remover
#Ryan Geddes, Quadrant Media, 2020
#
suppression = open("suppression.txt", "r")
clean_outfile = open("03240401-emailsonly-out.txt", "w")
final_list = open("03240401-emailsonly-deduped-out.txt", "r")
results = set(final_list) - set(suppression)
for row in results:
    clean_outfile.write(str(row))