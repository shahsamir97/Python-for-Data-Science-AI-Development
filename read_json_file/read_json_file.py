import json
data = {
    "first_name" : "Mark",
    "last_name" : "abc",
    "age" : 27,
    "address": {
        "streetAddress": "21 2nd Street",
        "city": "New York",
        "state": "NY",
        "postalCode": "10021-3100"
    }
}

with open("read_json_file/person_info.json", "r+") as file:
    if file.read().strip() == "":
        file.seek(0)
        json_object=json.dumps(data, indent=4)
        file.write(json_object)

    file.seek(0)
    data = json.load(file)
    print(data)
