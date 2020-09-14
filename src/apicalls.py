import requests
import os
import json
from dotenv import load_dotenv
load_dotenv()





def get_summoners(apiKey=os.getenv("LOL")):
    '''
    allows to get some summoners from riot api from diferent tiers or divisions"
    '''
    url= "https://euw1.api.riotgames.com/lol/league-exp/v4/entries/RANKED_SOLO_5x5/"
    tiers = ["DIAMOND", "PLATINUM","GOLD", "SILVER", "BRONZE", "IRON"]
    divisions = ["I","II","III","IV"]
    tier = input(f"select from {tiers}: ").upper()
    print(tier)
    division = input(f"select from {divisions}: ").upper()
    print(division)
    final_url = url + tier +"/" + division
    print(final_url)
    headers = {
        "X-Riot-Token": f"{apiKey}"
    }
    res = requests.get(final_url, headers=headers)
    if res.status_code != 200:
        raise Exception(f"API failed request result: {res.status_code}.")
    data = res.json()
    return data
#https://euw1.api.riotgames.com/lol/league-exp/v4/entries/RANKED_SOLO_5x5/CHALLENGER/I?page=1

def get_champs_mastery(id,apiKey=os.getenv("LOL")):
    '''
    given a summoner id search for all the champs he used and give bach the mastery with them
    '''
    url = "https://euw1.api.riotgames.com/lol/champion-mastery/v4/champion-masteries/by-summoner/"
    final_url=url+id
    #print(final_url)
    headers = {
        "X-Riot-Token": f"{apiKey}"
    }
    res = requests.get(final_url, headers=headers)
    if res.status_code != 200:
        raise Exception(f"API failed request result: {res.status_code}.")
    data = res.json()
    return data

if __name__ == "__main__":
    apiKey = os.getenv("LOL")
    print("WE HAVE APIKEY") if apiKey else print("NO APIKEY FOUND")
   