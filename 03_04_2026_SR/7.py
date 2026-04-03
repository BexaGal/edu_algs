import json

with open('7.json', 'r') as file:
    data = json.load(file)
    cls = list(data.keys())
    for i in range(len(cls)):
        print(data[cls[i]])
        for j in range(len(data[cls[i]])):
            for k in range(j+1, len(data[cls[i]])):
                if data[cls[i]][j]['surname'] == data[cls[i]][k]['surname']:
                    print(cls[i])
                    print(data[cls[i]][k]['surname'])
