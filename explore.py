import os
import json

path = 'outputs/'
listing = os.listdir(path)

entity_data = {}
key_phrases_data = {}

for infile in listing:
    try:
        #print(infile)
        data = json.load(open('outputs/' + infile))
        if "Entities" in data:
            for entity in data["Entities"]:
                text = entity["Text"].replace("@","")
                text = text.replace("RT ","")
                if text not in entity_data:
                    entity_data[text] = 1
                else:
                    entity_data[text] = entity_data[text] + 1
        elif "KeyPhrases" in data:
            for key_phrase in data["KeyPhrases"]:
                if key_phrase["Text"] not in key_phrases_data:
                    key_phrases_data[key_phrase["Text"]] = 1
                else:
                    key_phrases_data[entity["Text"]] = key_phrases_data[entity["Text"]] + 1

        #print(data)
    except:
        print('error')
print(entity_data)
