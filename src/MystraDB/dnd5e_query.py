import requests
import json
import os
import sys

def dataObtainer(desired_endpoint = "/api/magic-items/"):
    URL = "https://www.dnd5eapi.co"
    
    _endpoint_data = requests.get(URL + desired_endpoint).json()
    if _endpoint_data.status_code != 200:
        sys.exit(f'Failed to get endpoint: {_endpoint_data}')
    results = _endpoint_data["results"]
    
    endpoint_urls = []
    for item in results:
        endpoint_urls.append(URL + item['url'])

    endpoint_objects = []
    for item in endpoint_urls:
        endpoint_objects.append(requests.get(item).json())
    
    file_name = desired_endpoint
    file_name = file_name.lower().replace("api", "").replace("/", "")
    
    if os.path.exists(f"{file_name}.json"):
        pass
    else:
        f = open(f"{file_name}.json", "x")
        with open(f"{file_name}.json", 'w') as f:
            f.write(json.dumps(endpoint_objects, indent=4))
        
dataObtainer()