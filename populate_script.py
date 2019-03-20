#!/usr/bin/python

from sys import argv
import json

jdata = json.loads(open(str(argv[1]) + "/data/en_US/champion.json").read())

def main():
    for champion in jdata['data']:
        print_to_file(str(champion))

def print_to_file(champ_name):
    out_dict = {}
    for stat in jdata['data'][champ_name]['stats']:
        out_dict[stat] = jdata['data'][champ_name]['stats'][stat]
    write_to_file(champ_name, out_dict)

def write_to_file(champ_name, out_dict):
    json.dump(out_dict, open("./champions/" + champ_name + ".json", 'w'))

main()
