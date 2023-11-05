import json

def filter_json(filename):
    with open(filename, 'r', encoding="utf8") as file:
        data = json.load(file)
    filtered_data = []
    for obj in data:
       
        filtered_data.append(obj['text'])

    return filtered_data

# Usage example
filename = 'merged_file.json'
filtered_json = filter_json(filename)
#print(filtered_json)
with open('aneks.json', 'w', encoding='utf-8') as f:
    json.dump(filtered_json, f, ensure_ascii=False, indent=4)