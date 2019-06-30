#! /usr/bin/python

import os
import sys
import json
import urllib
import requests
import glob

elasticsearch_url = "http://127.0.0.1:9200"
object_templates_dir = sys.argv[1]
object_templates = glob.glob(object_templates_dir + "/*.json")

#add_object_cmd = "curl -u elastic:changeme -k -XPOST 'http://"+kibana_url+"kibana/dashboards/import' -H 'Content-Type: application/json' -H \"kbn-xsrf: true\" -d @"

for template in object_templates:
   object_id = template.replace(" ", "%20").split("/")[-1].split(".json")[0]
   add_object_cmd = 'curl -H "Content-Type: application/json" -XPUT "' + elasticsearch_url + '/.kibana/doc/' + object_id + '" -d "@' + template + '"'
   os.system(add_object_cmd)
