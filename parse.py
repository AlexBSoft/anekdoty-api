import json

def filter_json(filename):
    with open(filename, 'r', encoding="utf8") as file:
        data = json.load(file)
    messages = data['messages']
    filtered_data = []
    for obj in messages:
        if obj.get('type') != "message":
            continue
        if obj.get('photo') is not None and obj.get('text') != "":
            continue
        if obj.get('text') is not None and not isinstance(obj.get('text'), str):
            obj['text']=obj['text'][0]
            #continue
        filtered_data.append(obj)

    return filtered_data

# Usage example
filename = 'sets/4.json'
filtered_json = filter_json(filename)
#print(filtered_json)
with open('4_.json', 'w', encoding='utf-8') as f:
    json.dump(filtered_json, f, ensure_ascii=False, indent=4)