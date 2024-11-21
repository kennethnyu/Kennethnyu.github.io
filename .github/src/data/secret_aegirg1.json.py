import os
import numpy as np
import pandas as pd
import sqlite3
import sys
import json
from General import Config
database="src/data/databases/Snow_AegirG1.db"

configs=Config()
whitelisted=configs.whitelist
spec_to_color=configs.spec_to_color
boss_order_dict=configs.boss_order_dict

conn=sqlite3.connect(database)
query="""
SELECT p.raidId, p.spec, p.dps, p.boss, p.difficulty, p.gearscore, p.arkPassiveActive AS arkPsvActv,
       p.name || ' - ' || r.region AS char, p.isDead, DATE(ROUND(r.timestamp / 1000), 'unixepoch') AS serverdate
FROM players AS p
LEFT JOIN raids AS r ON p.raidId=r.raidId
WHERE p.class NOT IN ('Artist','Bard','Paladin')
      AND p.spec!='Princess'
ORDER BY p.raidId, p.name
"""
# Read
main_df=pd.read_sql_query(query, conn)
# Clean up
main_df["dps"]=main_df["dps"].astype(int)
main_df["gearscore"]=main_df["gearscore"].astype(float).round(2)
main_df["arkPsvActv"]=main_df["arkPsvActv"].fillna(-1).astype(int).map({-1:"All",0:"Off",1:"On"})
main_df["boss"]=main_df["boss"].map(boss_order_dict)
# Create new final dataframe
def get_parse(dps,arr):
      return int((arr<dps).mean() * 100)
final_df=pd.DataFrame()
for i,row in main_df[["difficulty","spec"]].drop_duplicates().iterrows():
      step_df=main_df[(main_df["difficulty"]==row["difficulty"])&(main_df["spec"]==row["spec"])].reset_index(drop=True)
      # Calculate parse
      array=step_df["dps"]
      step_df["score"]=step_df["dps"].apply(lambda x: get_parse(x,array))
      final_df=pd.concat([final_df,step_df])
# Remove useless
final_df=final_df[final_df["char"].apply(lambda x: True if "#" not in x else False)].reset_index(drop=True)
# Turn to dict records style
if final_df.shape[0]>0:
      final_df.set_index("raidId").to_csv(sys.stdout)