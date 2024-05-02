import csv


# cara membaca file csv
with open('data.csv', 'r') as file:
    #anda juga bsa menggunakan Dictreader
    reader = csv.reader(file)
    # for row in reader:
    #     row.append(row)
    rows = list(reader) 
    print('total data: ', reader.line_num)

for row in rows[:5]:
    print(row[0] + "-" + row[2]) 