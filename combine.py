import json

# List of JSON file names
json_files = ['1_.json', '2_.json', '3_.json', '4_.json']

# Function to merge JSON files
def merge_json_files(json_files):
    merged_data = []
    
    # Read each JSON file and append its data to the merged_data list
    for file in json_files:
        with open(file , encoding="utf8") as f:
            data = json.load(f)
            merged_data.extend(data)
    
    # Write the merged data to a new JSON file
    with open('merged_file.json', 'w', encoding='utf-8') as f:
        json.dump(merged_data, f, ensure_ascii=False, indent=4)
    
    print("JSON files merged successfully!")

# Call the merge_json_files function
merge_json_files(json_files)