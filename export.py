#! /usr/bin/python

import json
import urllib
import requests

elasticsearch_url="http://127.0.0.1:9200"
kibana_url="http://127.0.0.1:5601"
search_result_size=100
saved_objects={ "dashboard": [], "index-pattern": [], "search": [], "visualization": [] }

for object_type, object_list in saved_objects.iteritems():
   object_search_url = elasticsearch_url + "/.kibana/_search?q=type:" + object_type + "&size=" + str(search_result_size)
   response = requests.get(url=object_search_url)
   json_data = response.json()
   object_search_data=json_data['hits']['hits']
   for item in object_search_data:
       object_list.append(item['_id'].split(":")[1])
   for object_id in object_list:
       object_url = kibana_url + "/api/saved_objects/" + object_type + "/" + object_id
       response = urllib.urlopen(object_url)
       object_data = json.loads(response.read())
       object_data_file = object_type + ":" + object_id + ".json"
       with open(object_data_file, 'w') as outfile:  
           json.dump(object_data, outfile)
