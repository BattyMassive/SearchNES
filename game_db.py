from dbpedia import fetch_results


def system_games():
    system = "dbr:Nintendo_Entertainment_System"
    
    query = f"""
    SELECT ?game, ?title, ?releaseDate
    WHERE {{
        ?game dbo:computingPlatform {system} .
        ?game dbp:title ?title .
        ?game dbo:releaseDate ?releaseDate .
        
    }}
    LIMIT 10000
"""
    return fetch_results(query)
#?genre rdfs:label ?genre_label .
#?publisher dbp:name ?publisher_name .

def game_info(game_uri):
    query = f"""
    SELECT ?title, ?releaseDate, ?abstract, ?genre, ?publisher
WHERE {{
<{game_uri}> dbp:title  ?title .
<{game_uri}>  dbo:releaseDate ?releaseDate .
<{game_uri}> dbo:abstract ?abstract .
<{game_uri}> dbo:genre ?genre .
<{game_uri}> dbo:publisher ?publisher .
}}
"""
    #print(query)
    # returns only the first item
    items = fetch_results(query)
    if len(items) == 0:
        return None
    else:
        return items[0]

def publisher_info(uri):
    query = f"""
    SELECT ?name
WHERE {{
<{uri}> dbp:name  ?name .
}}
"""
    # returns only the first item
    return fetch_results(query)[0]

def game_designers(game_uri):
    query = f"""
    SELECT ?designer, ?name, ?abstract
WHERE {{
<{game_uri}> dbo:designer ?designer .
?designer dbp:name ?name
?designer dbo:abstract ?abstract
}}
"""
    return fetch_results(query)


def demo():
    games = system_games()
    for g in games:
        print("Title: %s" % (g["title"]["value"]))
        i = game_info(g["game"]["value"])
        print("  Release: %s" % (i["releaseDate"]["value"]))
        print("  Abstract: %s" % (i["abstract"]["value"]))

        print("======================================")
        
