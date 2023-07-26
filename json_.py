import json
import pandas as pd
import os

df = pd.read_csv('response.txt',encoding='ANSI',sep='\t')
for index,row in df.iterrows():
    _json = row['response'].split("', '")
    for one in _json:
        new_df = pd.DataFrame()
        new_df['response'] = [one.replace('{','').replace("'",'').replace('}','')]
        new_df['text'] = [row['text']]
        # new_df.to_csv('new_response.txt',sep='\t')
        file = 'new_response.txt'
        if os.path.isfile(file):
            new_df.to_csv(file, sep='\t', index=False, header=False, mode='a')
        else:
            new_df.to_csv(file, sep='\t', index=False)
exit(1)

# json_file = (open('data/LCCC-base_train.json','r',encoding="utf-8"))
file = 't.txt'
with open('data/LCCC-base_train.json','r',encoding="utf-8") as f:
    d = f.read().replace(' ', '').replace('",','').replace('"','').replace('],\n[','')
with open(file,'w') as ff:
    ff.write(d)
# print(type(json_file))