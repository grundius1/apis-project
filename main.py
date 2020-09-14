#!/usr/bin/env python3
import pandas as pd
import sys
import argparse
import src.functions as fn
import src.dataframes as fd
import src.apicalls as api
import re
from random import choice



def main():
    champdf = pd.read_csv('inputs/riot_champion.csv')[["key", "id", "name","partype", "title","info.attack","info.defense","stats.attackrange","stats.hp", "tags"]]
    champs=list(champdf.name)
    types= fn.flattener(list(champdf.tags))
    minhealth = champdf["stats.hp"].min()
    maxhealth = champdf["stats.hp"].max()
    champdf.to_csv('outputs/cleanedchamps.csv')

    parser = argparse.ArgumentParser(description='access stats of LOL champs')
    
    parser.add_argument('-n', dest='name',nargs='+', type = fn.onlyValidnames(champs),
                        default='ALL',
                        help='el nombre del campeon/campeones que se veran, all enseña todos')
    parser.add_argument('-t', dest='type',
                        default='ALL', required=False,
                        type=str,
                        help="partype del campeon")
    parser.add_argument('-s', dest='style',nargs='+', type = fn.onlyValidttag(types),
                        default='ALL',required=False,
                        help='el tipo del campeon/campeones que se veran, all enseña todos')

    parser.add_argument('-l', dest='health',nargs='?', type = fn.onlyvalidhealth(minhealth, maxhealth),
                        default=minhealth, required=False,
                        help='los campeones que tienen esa salud o mas')
    parser.add_argument('-p', dest='plot', type = bool,
                        default=False, 
                        required=False,
                        help='si vas a querer ver graficos de barras con los summoners que hayan salido, solo se puede usar si selecionas uno o mas summoners')

    args = parser.parse_args()
    df = champdf
    df = fd.namesdf(df, args.name)
    df = fd.typesdf(df, args.type)
    df = fd.stylessdf(df, args.style)
    df = fd.healthdf(df, args.health)
    df = df.drop_duplicates()

    summoners=fn.summonerstoDictionary(api.get_summoners())
    summonerscount = int(input(f"How many summoners do you want: "))
    names =[]
    if summonerscount != 0:
        for i in range(summonerscount):
            id = choice(list(summoners.values()))
            for k,v in summoners.items():
                if v == id:
                    names.append(k)
            print(f"getting {names[i]} champs mastery",end='\r')
            summonerdict = fn.champsmasterytoDictionary(api.get_champs_mastery(id))
            df = fn.dictinonarytodf(df,summonerdict, names[i])
        df = df[["id","key"]+ names]
        df = df.drop(["key"], axis=1)
        df['mean']= df.mean(axis=1,skipna=False)
        df['std']= df.std(axis=1)
        print(df.columns)
        df = df.dropna(thresh=len(df.columns)-1)
        print(df.sort_values(by='mean',ascending=False))
        df.to_csv('outputs/summoners.csv')
    else:
        print(df)
        args.plot=False
        sys.exit()
    
    if args.plot == True:
        fd.barplotsummoner(df)
        fd.barplotchamps(df)

if __name__ == "__main__":
    main()