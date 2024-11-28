import os
import numpy as np
import pandas as pd
import sqlite3
import sys
import json
from General import Config
database="src/data/databases/Snow_BehemothG2.db"

configs=Config()
whitelisted=configs.whitelist
spec_to_color=configs.spec_to_color

conn=sqlite3.connect(database)
query="""
SELECT p.raidId, p.spec, p.dps, p.boss, p.difficulty, p.gearscore, p.arkPassiveActive AS arkPsvActv
FROM players AS p
LEFT JOIN raids AS r ON p.raidId=r.raidId
WHERE p.class NOT IN ('Artist','Bard','Paladin')
      AND p.spec!='Princess'
      AND p.isDead=0
ORDER BY p.raidId, p.name
"""
# Read
main_df=pd.read_sql_query(query, conn)
# Clean up
main_df["dps"]=main_df["dps"].astype(int)
main_df["gearscore"]=main_df["gearscore"].astype(float).round(2)
main_df["arkPsvActv"]=main_df["arkPsvActv"].fillna(-1).astype(int).map({-1:"All",0:"Off",1:"On"})
# Subset
main_df=main_df[100000:].reset_index(drop=True)
# Turn to dict records style
if main_df.shape[0]>0:
      main_df.set_index("raidId").to_csv(sys.stdout)