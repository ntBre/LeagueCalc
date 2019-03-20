from flask import Flask
app = Flask(__name__)
import json

# call calculation
#TODO post level runes items champ
@app.route('/stats', methods=['GET'])
def stats():
    champ_name = "Aatrox"
    level = 13
    runes = {}
    items = {}
    
    champ = json.loads(open("../champions/Aatrox.json").read())
    champ = level_up_stats(champ, level)
    return json.dumps(champ)

def level_up_stats(input_champ, level):
    output_champ = {}
    # stats that level up
    level_stats = ["armor", "hp", "attackdamage", "mp", "spellblock", "mpregen", "hpregen", "attackspeed"]
    if attribute in level_stats:
        for attribute in input_champ.keys(): 
            output_champ[attribute] = input_champ[attribute] + (input_champ[dict[attribute]]*level)
            
{
    "armor":"armorperlevel", 
    "attackdamage":"attackdamageperlevel",
    "hp":"hpperlevel",
    "mp":"mpperlevel", 
    "spellblock":"spellblockperlevel", 
    "hpregen":"hpregenperlevel", 
    "mpregen":"mpregenperlevel", 
    "movespeed":None,
    "crit":None,
    "attackspeed":}

    "armorperlevel": 3.25,
    "hpperlevel": 80,
    "attackdamage": 60,
    "mpperlevel": 0,
    "spellblockperlevel": 1.25,
    "armor": 33,
    "hp": 580,
    "hpregenperlevel": 0.75,
    "spellblock": 32.1,
    "attackrange": 175,
    "movespeed": 345,
    "attackdamageperlevel": 5,
    "mpregenperlevel": 0,
    "mp": 0,
    "attackspeed": 0.651,
    "crit": 0,
    "mpregen": 0,
    "attackspeedperlevel": 2.5,
    "hpregen": 8,
    "critperlevel": 0

    return output_champ["armor"] 
