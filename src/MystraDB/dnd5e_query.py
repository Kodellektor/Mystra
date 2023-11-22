import requests
import json
import os

def dataObtainer(desired_endpoint = "/api/magic-items/"):
    URL = "https://www.dnd5eapi.co"

    endpoint_data = requests.get(URL + desired_endpoint).json()
    results = endpoint_data["results"] 

    endpoint_urls = []
    for item in results:
        endpoint_urls.append(URL + item['url'])

    endpoint_objects = []
    for item in endpoint_urls:
        endpoint_objects.append(requests.get(item).json())
    
    file_name = desired_endpoint
    file_name = file_name.replace("/api/", "").lower()
    file_name = file_name.replace("/", "")
    
    if os.path.exists(f"{file_name}.json"):
        with open(f"{file_name}.json", 'w') as f:
            f.write(json.dumps(endpoint_objects, indent=4))
    else:
        f = open(f"{file_name}.json", "x")
        with open(f"{file_name}.json", 'w') as f:
            f.write(json.dumps(endpoint_objects, indent=4))
        
    
dataObtainer()