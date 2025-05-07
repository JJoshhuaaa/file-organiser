import json

# Step 1: Load existing data from the file
with open("folders.json", "r") as file:
    data = json.load(file)

# Step 2: Define your new domain to add
new_domain = {
    "name": "Fun",
    "types": ["Games", "Memes"]
}

# Step 3: Append the new domain to the "domains" list
data["domains"].append(new_domain)

# Step 4: Save the updated data back to the file
with open("folders.json", "w") as file:
    json.dump(data, file, indent=4)
