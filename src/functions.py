import sys
import argparse
import re


def onlyValidnames(champs):
    '''
    check for valid names imput on command line arguments
    '''
    def wrapper(name):
        if name.lower() == "all" or name == "":
            return "ALL"
        else:
            if name.capitalize() not in champs:
                raise argparse.ArgumentTypeError(f"{name} is an invalid name ")
            else:
                return name.capitalize()
    return wrapper

def onlyValidttag(types):
    '''
    check for valid tag imput on command line arguments
    '''
    def wrapper(style):
        if style.lower() == "all" or style == "":
            return "ALL"
        else:
            if style.capitalize() not in types:
                raise argparse.ArgumentTypeError(f"{style} is an invalid type ")
            else:
                return style.capitalize()
    return wrapper

def onlyvalidhealth(minhelth, maxhealth):
    '''
    check for valid tag imput on command line arguments
    '''
    def wrapper(health):
        try:
            health = int(health)
        except Exception:
            raise argparse.ArgumentTypeError(f"{health} is an invalid positive int value")       
        if health >= minhelth and health <= maxhealth:
            return health
        else:
            raise argparse.ArgumentTypeError(f"year must be between {minhelth} and {maxhealth}")
    return wrapper


def flattener(lists):
    '''
    this function make a set from all the tags of the dataset, to make a faster comparision 
    '''
    final = []
    for item in lists:
        x = re.findall(r'\w+',item)
        #print(type(x))
        for item in x:
            final.append(item)
    return set(final)


def summonerstoDictionary(data):
    '''
    creates a dictionary wuçith the summoner name and summoner id to search
    '''
    dict1={}
    for item in data:
        dict1.update({item["summonerName"]:item["summonerId"]})
    return dict1


def champsmasterytoDictionary(data):
    '''
    creates a dictionary with the champ id and the mastery per champion
    '''
    dict1={}
    for item in data:
        dict1.update({item["championId"]:item["championPoints"]})
    return dict1


def dictinonarytodf(data, dictionary, name):
    '''
    takes the dataframe and the champsmasterytoDictionary to add a colum agregating the champ mastery
    '''
    data[name] = data['key'].map(dictionary)
    return data