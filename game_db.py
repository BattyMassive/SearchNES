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
    LIMIT 1
"""
    return fetch_results(query)


def game_info(game_uri):
    query = f"""
    SELECT ?title, ?releaseDate, ?abstract
WHERE {{
<{game_uri}> dbp:title  ?title .
<{game_uri}>  dbo:releaseDate ?releaseDate .
<{game_uri}> dbo:abstract ?abstract
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
        
