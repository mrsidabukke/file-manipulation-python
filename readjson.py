import json

with open('people.txt', 'r') as peoplefile:
    data = json.load(peoplefile)

    for people in data['people']:
        print('Name: ' + people['name'])
        print('Website: ' + people['website'])
        print('From: ' + people['from'])
        print('')
