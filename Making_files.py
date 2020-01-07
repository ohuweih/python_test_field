#!/usr/bin/python
import json
from pprint import pprint
data= { 
    "name": ["name1", "name_2", "name_3"], 
    "endpoint": ["endpoint_1", "endpoint_2", "endpoint_3"], 
    "uri": ["uri_1" ,"url_2", "uri_3"], 
    "uri2": ["uri2_1" ,"url2_2", "uri2_3"], 
    "parents1": ["parents1_1", "parents1_2", "parents1_3"], 
    "parents2": ["parents2_1", "parents2_2", "parents2_3"], 
    "parents3": ["parents3_1", "parents3_2", "parents3_3"] 
    }


feeds = []

for i in range(3):
    feed_data = {
        "name": data["name"][i],  
        "encoder": {
            "output_group_index": 0, 
            "live_endpoint": data["endpoint"][i],  
            "input_uri": data["uri"][i], 
            "secondary_input": {
                "input_uri": data["uri2"][i], 
                "input_interface": "bond1"
            }, 
            "live_service_endpoint": data["endpoint"][i], 
            "packager_whitelist_ip": [
                "255.111.111.111", 
                "255.111.111.111", 
                "255.111.111.111"
            ]
        }, 
        "encoding_settings": {
            "input_interface": "eth_Something", 
            "output_groups": [
                {
                    "cdn": "CDN_URL", 
                    "connection_retry_interval": 1, 
                    "num_retries": 3 
                }, 
                {
                    "cdn": "CDN_URL", 
                    "connection_retry_interval": 1, 
                    "num_retries": 3 
                }
            ]
        }, 
        "emp": {
            "channel_arn": "null"
        }, 
        "monitor": {
            "hls_live_monitor": "http://monitor_url", 
            "dash_live_monitor": "http://monitor_url"
        }, 
        "_parents": [
            data["parents1"][i], 
            data["parents2"][i], 
            data["parents3"][i]
        ]
    }
    feeds.append(feed_data)

with open("new_mlb_feeds.txt", "w") as f:
    json.dump(feeds, f)

pprint(feeds)
