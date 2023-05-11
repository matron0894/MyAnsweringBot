# write your code here
import json

with open("users.json", "r") as json_file:
    user_dict_from_json = json.load(json_file)
    count_users = len(user_dict_from_json["users"])
    print(count_users)



