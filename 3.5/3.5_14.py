import json

input_file = input()
update_file = input()
with open(input_file) as f:
    users_data = json.load(f)
with open(update_file) as f:
    updates_data = json.load(f)
key_name = 'name'
result_dict = {}
for update in updates_data:
    for user in users_data:
        if update[key_name] == user[key_name]:
            for field in update.keys():
                if update[field] > user.get(field, ''):
                    user[field] = update[field]
for user in users_data:
    name = user.pop(key_name)
    result_dict[name] = user
with open(input_file, 'w') as f:
    json.dump(result_dict, f, sort_keys=False, indent=4, ensure_ascii=False)