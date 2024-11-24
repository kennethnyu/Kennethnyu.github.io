import os
import pandas as pd
import sqlite3
import sys
import json
from General import Config
databases=[name for name in os.listdir("src/data/databases") if "Snow_" in name]

main_df=pd.DataFrame()
for db in databases:
    conn=sqlite3.connect("src/data/databases/{}".format(db))
    query="""
    SELECT name, spec, MAX(gearScore) AS maxgear
    FROM players
    WHERE raidId IN (SELECT raidId FROM raids WHERE timestamp/1000 >= (TIME('NOW')-(7*86400)))
          AND name NOT LIKE '%#%'
    GROUP BY name, spec
    """
    df=pd.read_sql_query(query, conn) 
    if df.shape[0]>0:
        main_df=pd.concat([main_df,df]).reset_index(drop=True)

# Group by name and spec
main_df=main_df.groupby(["name","spec"]).max().reset_index()
# Sort by most gear
main_df=main_df.sort_values("maxgear",ascending=False).reset_index(drop=True)

# Turn to dict records style
df_json=main_df[["maxgear"]].to_dict("records")
# Dump
json.dump(df_json, sys.stdout)