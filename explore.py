import os
import json
import re
def get_trailing_number(s):
    m = re.search(r'\d+$', s)
    return int(m.group()) if m else None

path = 'outputs/'
listing = os.listdir(path)

entity_data = {}
key_phrases_data = {}
key_phrase_sentiment = {}
for infile in listing:
    try:
        print(infile)
        data = json.load(open('outputs/' + infile))
        file_minus_json_exe = infile[:-5]
        print(file_minus_json_exe)
        num = get_trailing_number(file_minus_json_exe)
        sentiment_data = json.load(open('outputs/sentiment' + str(num) + '.json'))
        if "Entities" in data:
            for entity in data["Entities"]:
                text = entity["Text"].replace("@","")
                text = text.replace("RT ","")
                if text not in entity_data:
                    entity_data[text] = 1
                else:
                    entity_data[text] = entity_data[text] + 1

                if text not in key_phrase_sentiment.keys():
                    key_phrase_sentiment[text] = sentiment_data['Sentiment']
                else:
                    key_phrase_sentiment[text] += ' ' + sentiment_data['Sentiment']

        '''elif "KeyPhrases" in data:
            for key_phrase in data["KeyPhrases"]:
                if key_phrase["Text"] not in key_phrases_data:
                    key_phrases_data[key_phrase["Text"]] = 1
                else:
                    key_phrases_data[entity["Text"]] = key_phrases_data[entity["Text"]] + 1'''
    except:
        print('error')

filt = {k: v for k, v in entity_data.items() if v > 5}
print(json.dumps(filt, sort_keys=True, indent=4))
print('-----------')
print(json.dumps(key_phrase_sentiment, sort_keys=True, indent=4))
