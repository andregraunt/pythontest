from tabulate import tabulate

table=[['name','telephone'],['alis','0523528340'],['bob','0523528344']]

#headers='firstrow'
#print(tabulate({"Name": ["Alice", "Bob"],
 #"Age": [24, 19]}, headers="keys"))

print(tabulate(table, headers='firstrow'))


