import json

# Load your JSON data from a file
with open('agent_details.json', 'r') as file:
    json_data = json.load(file)

# Print the JSON data with indentation
pretty_json = json.dumps(json_data, indent=4)
print(pretty_json)
