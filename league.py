#!/usr/bin/python

import json

jdata = json.loads(open("9.5.1/data/en_US/champion.json").read())
#skip = ['blurb', 'version', 'info', 'title', 'image', 'tags', 'id', 'key', 'partype',
#'name']

def pretty_print():
    for i in jdata['data']:
        print i#, ['Swain']['stats'][i]
        for j in jdata['data'][i]['stats']:
            print j, jdata['data'][i]['stats'][j]
        print ''

def useful_print():
    for i in jdata['data']:
        print i
        print jdata['data'][i]['stats'], '\n'
    
#pretty_print()
useful_print()
