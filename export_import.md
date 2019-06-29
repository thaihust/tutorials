https://www.elastic.co/guide/en/elasticsearch/reference/current/search-uri-request.html#_parameters_4

https://stackoverflow.com/questions/47017583/how-to-import-export-a-dashboard-in-kibana-using-a-restful-api

curl -s 'http://localhost:9200/.kibana/dashboard/_search?pretty=true&q=_source=dashboard'

curl -XPOST 'http://127.0.0.1:9200/.kibana/_search?q=type:visualization&pretty=true' | jq '.hits.hits'
