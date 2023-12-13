import json
with open("dico.json")  as conf :
    d = json.load(conf)

print(d)