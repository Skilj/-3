import json

from example_from_lesson.test_data.read_write_files.files import JSON_FILE, JSON_FILE_W

with open(JSON_FILE, "r") as f:
    users = json.loads(f.read())
    # users = json.load(f)

users_list = users['users']

for user in users_list:
    print(user)

print(100 * "+")  # Write
data = {
    "users": [
        {"login": "Alisa", "email": "alisa.april.one@gmail.ru"},
        {"login": "Plaksa", "email": "cat@gmail.ru"},
        {"login": "MMayers", "email": "fromhellwithlove@gmail.com"},
    ]
}

with open(JSON_FILE_W, "w") as f:
    s = json.dumps(data, indent=4)
    f.write(s)



