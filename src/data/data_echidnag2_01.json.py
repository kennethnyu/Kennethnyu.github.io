import os
import numpy as np
import pandas as pd
import sqlite3
import sys
import json
from General import Config
r_db="src/data/databases/Snow_EchidnaG2_raids_01.parquet"
p_db="src/data/databases/Snow_EchidnaG2_players_01.parquet"

configs=Config()
whitelisted=configs.whitelist
spec_to_color=configs.spec_to_color

main_df=pd.read_parquet(p_db,filters=[("class","not in",['Artist','Bard','Paladin']),
                                      ("spec","!=","Princess"),
                                      ("isDead","=",0)]).rename(columns={"arkPassiveActive":"arkPsvActv"})
# Clean up
main_df["dps"]=main_df["dps"].astype(int)
main_df["gearScore"]=main_df["gearScore"].astype(float).round(2)
main_df["arkPsvActv"]=main_df["arkPsvActv"].fillna(-1).astype(int).map({-1:"All",0:"Off",1:"On"})
# Subset
main_df=main_df[:100000].reset_index(drop=True)
# Turn to dict records style
if main_df.shape[0]>0:
      main_df.set_index("raidId").to_csv(sys.stdout)