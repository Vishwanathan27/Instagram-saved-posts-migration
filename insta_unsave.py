from instagram_private_api import Client, ClientCompatPatch
from instagram_private_api_extensions import pagination
import json, time


user_name = 'username'
password = 'password'


api = Client(user_name, password)

def save_json(data, filename):
  with open(filename, 'a') as outfile:
    json.dump(data, outfile)


items=[]

for results in pagination.page(api.saved_feed, args={
    'count': 100,
}):
   if results.get('items'):
        items.extend(results['items'])
        # json.dumps(items)

        # save_json(items, 'some_1854.json')
        # print("Saved: ", len(items))    


for i,x in enumerate(items):
   z = items[i]['media']['pk']
   api.unsave_photo(media_id=z)
   time.sleep(3)
   print("Unsaved: ", z)

