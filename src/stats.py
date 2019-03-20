from flask import Flask
app = Flask(__name__)
import json
import subprocess

# call calculation
#TODO post level runes items champ
@app.route('/stats', methods=['GET'])
def stats():
    champ_name = "Aatrox"
    level = 18
    runes = {}
    items = {}
    champ = json.loads(open("./champions/Aatrox.json").read())
    champ = level_up_stats(champ, level)
    return json.dumps(champ)

def level_up_stats(input_champ, level):
    output_champ = {
    "armor":"armorperlevel", 
    "attackdamage":"attackdamageperlevel",
    "hp":"hpperlevel",
    "mp":"mpperlevel", 
    "spellblock":"spellblockperlevel", 
    "hpregen":"hpregenperlevel", 
    "mpregen":"mpregenperlevel", 
    "movespeed":None,
    "crit":None,
    "attackspeed":None
    } 
    # stats that level up
    level_stats = ["armor", "hp", "attackdamage", "mp", "spellblock", "mpregen", "hpregen", "attackspeed"]
    for attribute in input_champ.keys(): 
        if attribute in level_stats:
            scaling = attribute + "perlevel"
            output_champ[attribute] = input_champ[attribute] + (input_champ[scaling] * (level-1))
        else:
            output_champ[attribute] = input_champ[attribute]

    return output_champ
            