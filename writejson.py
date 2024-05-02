import json

# data yang akan di tulis ke file json
data = {}
data['people'] = [{
    'name': 'Scott',
    'website': 'stackabuse.com',
    'from': 'Nebraska'
}, {
    'name': 'Larry',
    'website': 'google.com',
    'from': 'Michigan'
}, {
    'name': 'Tim',
    'website': 'apple.com',
    'from': 'Alabama'
}]
# cara menulis file json
with open('people.txt', 'w') as peoplefile:
    json.dump(data, peoplefile)