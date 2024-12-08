import datetime as dt
import json
import os
import pandas as pd
import sqlite3
import sys
from General import Config
# Find databases and sort so we can zip them and join/merge
databases=[name for name in os.listdir("src/data/databases") if "Snow_" in name]
raids_list=["src/data/databases/{}".format(db) for db in databases if "_raids_" in db]
players_list=["src/data/databases/{}".format(db) for db in databases if "_players_" in db]
raids_list.sort()
players_list.sort()
# Iterate and add together
main_df=pd.DataFrame()
for r_db, p_db in zip(raids_list, players_list):
    raids=pd.read_parquet(r_db)
    players=pd.read_parquet(p_db)
    # Filter recent 7 days and those with names so it's unique
    raids=raids[raids["timestamp"]>=(dt.datetime.timestamp(dt.datetime.now())-(7*86400))*1000].reset_index()
    players=players[players["raidId"].isin(list(raids["raidId"].unique()))].reset_index(drop=True)
    players=players[players["name"].apply(lambda x: True if "#" not in x else False)].reset_index(drop=True)
    print(players.shape[0])
    print(players)
    if players.shape[0]>0:
        df=players.groupby(["name","spec"])["gearscore"].max().reset_index().rename(columns={"gearscore":"maxgear"})
        main_df=pd.concat([main_df,df]).reset_index(drop=True)

# Group by name and spec
main_df=main_df.groupby(["name","spec"]).max().reset_index()
# Sort by most gear
main_df=main_df.sort_values("maxgear",ascending=False).reset_index(drop=True)

# Turn to dict records style
df_json=main_df[["maxgear"]].to_dict("records")
# Dump
json.dump(df_json, sys.stdout)