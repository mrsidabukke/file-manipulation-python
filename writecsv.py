import csv

rows = {'Nama': 'Andi', 'skill': 'Python', 'power': 100},





with open('person.csv','a') as csvfile:
    fields = ['Nama', 'skill', 'power']
    writer = csv.DictWriter(csvfile, fieldnames=fields)

    writer.writeheader()
    writer.writerows(rows)