from tinydb import TinyDB
import pandas as pd
import json

db_content1 = TinyDB("db_240123.json")
db_content2 = TinyDB("db_250423.json")

df1 = pd.DataFrame(db_content1) # cria dataframe a partir do conteudo do arquivo do banco de dados
df2 = pd.DataFrame(db_content2)

df = pd.concat([df1, df2], sort=False)

df.to_json("df_pd.json", orient="records")

j = open('df_pd.json',)
json_array = json_list = json.load(j)

json_dict = {}
for index, line in enumerate(json_array):
    json_dict[f"{index+1}"] =  line

json_dict = {"_default": json_dict}

with open('db.json', 'w') as fp:
    json.dump(json_dict, fp)
