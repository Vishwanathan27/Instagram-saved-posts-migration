import random
from sys import exc_info
from instagram_private_api import Client, ClientCompatPatch
# from instagram_private_api_extensions import pagination
import json, time  

user_name = 'username'
password = 'password'
api = Client(user_name, password)


# Open the JSON file
with open('final.json', 'r') as f:
    # Load the data from the file
    data = json.load(f)

def save_json(data, filename):
  with open(filename, 'a') as outfile:
    json.dump(data, outfile)
    
def write_json(data, filename):
  with open(filename, 'w') as outfile:
    json.dump(data, outfile)

array_ = []
collection_ids = [17971694668885298]
# filtered_list = [item for item in data if item['is_private']]
count = 654
filtered_list_first_100 = data[count:800]
random.shuffle(filtered_list_first_100)

for i in filtered_list_first_100:
    media_id = i['media']['pk']
    print(media_id)
    count=count+1   
    print(count)
    try:
        response = api.save_photo(media_id=media_id, added_collection_ids=collection_ids)
        print(response);
        dict_m = {'media_id': media_id}
        array_.append(dict_m)
        time.sleep(30)
    except:
        #print the error
        print(exc_info()[1])
        time.sleep(3)

write_json(array_, 'some_1854.json')