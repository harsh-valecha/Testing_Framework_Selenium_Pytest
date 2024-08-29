import json

def read_json(file):
    with open(file,mode='r') as f:
        data = json.load(f)
    return data


# for unit testing
print(read_json('data/json/MOCK_DATA.json'))