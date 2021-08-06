# Decent guide for writing queries:
#  https://medium.com/virtuoso-blog/dbpedia-basic-queries-bc1ac172cc09

# Query GUI:
#  https://dbpedia.org/sparql/

import rdflib
from os import mkdir, listdir
from pathlib import Path
import hashlib
import requests
import pickle

cache_dir = "cache/"

def save_cache(cache_key, data):
    # make a shorter id good for filenames
    cache_id = hashlib.sha224(str(cache_key).encode('utf-8')).hexdigest()[0:15]
    try:
        mkdir(cache_dir)
    except OSError as error:
        None # ignore

    filename = f"{cache_dir}{cache_id}.pickle"
    pickle.dump(data, open(filename, 'wb'))
    return data
    
def get_cache(cache_key):
    # make a shorter id good for filenames
    cache_id = hashlib.sha224(str(cache_key).encode('utf-8')).hexdigest()[0:15]

    filename = f"{cache_dir}{cache_id}.pickle"
    if Path(filename).exists():
        print(f"Cached copy of {filename}")
        return pickle.load(open(filename, 'rb'))
    else:
        print(f"No cache for {filename}")
        return None

# returns something like this:
# {'head': {'link': [], 'vars': ['title', 'date', 'game']},
#  'results': {'bindings': [{'date': {'datatype': 'http://www.w3.org/2001/XMLSchema#date',
#                                     'type': 'typed-literal',
#                                     'value': '1986-03-19'},
#                            'game': {'type': 'uri',
def fetch_query(query):
    response = get_cache(query)
    if response != None:
        return response
    
    params   = {"query": query, "timeout": 20000, "format": "application/sparql-results+json"}
    response = requests.get("https://dbpedia.org/sparql", params)
    return response.json()


# returns just the result items.
def fetch_results(query):
    response = fetch_query(query)
    save_cache(query, response)
    # val_keys = response["head"]["vars"]
    items    = response["results"]["bindings"]
    return items
    
