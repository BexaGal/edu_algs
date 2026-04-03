import json

with open('8.json', 'r') as file:
    data = json.load(file)
    curindex = 0
    for i in range(len(data)):
        if data[i]['sunsum'] > data[curindex]['sunsum'] or (data[i]['sunsum'] >= data[curindex]['sunsum'] and data[i]['distance'] < data[curindex]['distance']):
            curindex = i
    print(data[curindex])
