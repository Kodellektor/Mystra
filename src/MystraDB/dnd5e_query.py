import requests
import json
import os

def dataObtainer(desired_endpoint = "/api/magic-items/"):
    URL = "https://www.dnd5eapi.co"

    endpoint_data = requests.get(URL + desired_endpoint).json()
    results = endpoint_data["results"] 

#considering i repeat loops here, i'm considering what to change these to streamline process
    #extract urls from endpoints into list
    endpoint_urls = []
    for item in results:
        endpoint_urls.append(URL + item['url'])

    #creates url list to pass through API
    endpoint_objects = []
    for item in endpoint_urls:
        endpoint_objects.append(requests.get(item).json())
    

    #creates file name based on desired endpoint
    file_name = desired_endpoint
    file_name = file_name.replace("/api/", "").lower()
    file_name = file_name.replace("/", "")
    
    #write results to file in JSON format (could be generators to support lower spec machinery. thinking of turning script into factory)
    if os.path.exists(f"{file_name}.json"):
        with open(f"{file_name}.json", 'w') as f:
            f.write(json.dumps(endpoint_objects, indent=4))
    else:
        f = open(f"{file_name}.json", "x")
        with open(f"{file_name}.json", 'w') as f:
            f.write(json.dumps(endpoint_objects, indent=4))
        
#pass desired urls through 
dataObtainer()