https://www.elastic.co/guide/en/elasticsearch/reference/current/search-uri-request.html#_parameters_4

https://stackoverflow.com/questions/47017583/how-to-import-export-a-dashboard-in-kibana-using-a-restful-api

curl -s 'http://localhost:9200/.kibana/dashboard/_search?pretty=true&q=_source=dashboard'

curl -XPOST 'http://127.0.0.1:9200/.kibana/_search?q=type:visualization&pretty=true' | jq '.hits.hits'

https://air.ghost.io/kibana-4-export-and-import-visualizations-and-dashboards/
https://quangphamsoft.wordpress.com/2017/03/23/importing-a-json-file-into-elasticsearch/

