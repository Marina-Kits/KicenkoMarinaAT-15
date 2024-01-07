import json
import requests

def search_for_starship(name_of_starship):
    link=f"https://swapi.dev/api/starships/?search={name_of_starship}"
    response=requests.get(link)
    data=response.json()
    starship=data["results"][0]
    return starship

def search_for_pilot_info(pilot_link):
    information=requests.get(pilot_link)
    pilot=information.json()
    return {
        "name": pilot["name"],
        "height": pilot["height"],
        "mass": pilot["mass"],
        "homeworld": requests.get(pilot["homeworld"]).json()["name"],
        "homeworld_url": pilot["homeworld"],
    }

def generating_output(starship_info):
    max_atmosphering_speed=starship_info["max_atmosphering_speed"]
    pilots=[]
    for pilot_link in starship_info["pilots"]:
        pilots.append(search_for_pilot_info(pilot_link))
    name_of_starship=starship_info["name"]
    starship_class=starship_info["starship_class"]
    res={
        "max_atmosphering_speed": max_atmosphering_speed,
        "pilots": pilots,
        "ship_name": name_of_starship,
        "starship_class": starship_class,
    }
    return res

pilots_Millennium_Falcon = search_for_starship("Millennium Falcon")
if pilots_Millennium_Falcon:
    res=generating_output(pilots_Millennium_Falcon)
    print(json.dumps(res, indent=2, separators=(",", ": ")))
    with open("pilots_Millennium_Falcon.json", "w") as json_file:
        json.dump(res, json_file, indent=2, separators=(",", ": "))