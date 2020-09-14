import pandas as pd   
import matplotlib.pyplot as plt 

#df = pd.read_csv('cleanedchamps.csv')

def namesdf(data, names):
    '''
    given a dataframe, search for all the names in the dataframe and returns them
    '''
    if names == 'ALL':
        return data
    else:
        return data[data.id.isin(names)]


def typesdf(data,types):
    if types == 'ALL':
        return data
    else:
        return data[data.partype == types]


def stylessdf(data,style):
    '''
    given a dataframe, search for all the tags in the dataframe and returns them
    '''
    if style == 'ALL':
        return data
    elif len(style) < 3:
        if len(style) == 1:
            return data[data.tags.str.contains(style[0])]
        elif len(style) == 2:
            return data[data.tags.str.contains(style[0])|data.tags.str.contains(style[1])]
    else:
        return "champion oly can have up to 2 styles"

def healthdf(data,health):
    '''
    given a dataframe, search for champions health and return the ones above it
    '''
    return data[data["stats.hp"] >= health]

def barplotchamps(data):
    '''
    function to plot a bar plot to show some of the most used champsfor each summoner and their mastery
    '''
    data = data.set_index("id").sort_values(by='mean')
    data = data.drop(["mean","std"], axis=1)
    if "key" in data.columns:
        data = data.drop(["key"], axis=1)
    data.T.sum().plot.bar()
    plt.title("acc. mastery by champ")
    plt.xlabel("champs")
    plt.ylabel("mastery")
    return plt.show()

def barplotsummoner(data):
    '''
    function to plot a bar plot to show some of the most used champsfor each summoner and their mastery
    '''
    data = data.set_index("id").sort_values(by='mean')
    data = data.drop(["mean","std"], axis=1).head(20)
    if "key" in data.columns:
        data = data.drop(["key"], axis=1)
    data.T.plot.bar(figsize= (20,10))
    plt.title("mastery by summoner")
    plt.xlabel("Summoners")
    plt.ylabel("Mastery")
    return plt.show()
