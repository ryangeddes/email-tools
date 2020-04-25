# Email Domain Suppression And Remover
# Ryan Geddes, Quadrant Media, 2020
# Takes list of E-amils and runs it against list of domains
# Removes addresses from list it domains match.


clean_outfile = open("03240401crubbed-domains-out.txt", "w+")
final_list = open("03240401-emailsonly-out.txt", "r")
results = set(final_list)
bad_domain = open("domain_suppression.txt", "r")
remove_domain = []
r_domain = []
for i in bad_domain:
    remove_domain += [i]
    domain_list = [item.strip() for item in remove_domain]
    set(domain_list)
for row in results:
    row_domain = row[row.find("@"):]
    r_domain = [row_domain[1:]]
    edomain_list = []
    edomain_list += [item.strip() for item in r_domain]
    for i in edomain_list:
        if i in domain_list:
#           matches.append(x)
            pass

        else:
            clean_outfile.write(str(row))
