import os
import numpy as np
import pandas as pd
import sqlite3
import sys
import json
from General import Config
# Find databases and sort so we can zip them and join/merge
databases=[name for name in os.listdir("src/data/databases") if "Snow_" in name]
raids_list=["src/data/databases/{}".format(db) for db in databases if "_raids_" in db]
players_list=["src/data/databases/{}".format(db) for db in databases if "_players_" in db]
raids_list.sort()
players_list.sort()
# Relevant databases
curr_boss=os.path.basename(__file__).split("_")[1]
raids_list=[rdb for rdb in raids_list if curr_boss in rdb]
players_list=[pdb for pdb in players_list if curr_boss in pdb]
# Get configs
configs=Config()
whitelisted=configs.whitelist
spec_to_color=configs.spec_to_color
# Iterate
main_df=pd.DataFrame()
filters=[("class","not in",['Artist','Bard','Paladin']),
("spec","!=","Princess"),
("isDead","=",0)]
for pdb in players_list:
      temp_df=pd.read_parquet(pdb,filters=filters).rename(columns={"arkPassiveActive":"arkPsvActv"})
      main_df=pd.concat([main_df,temp_df])
# Clean up
main_df["dps"]=main_df["dps"].astype(int)
main_df["gearScore"]=main_df["gearScore"].astype(float).round(2)
main_df["arkPsvActv"]=main_df["arkPsvActv"].fillna(-1).astype(int).map({-1:"All",0:"Off",1:"On"})
main_df.drop(columns=["hash"],inplace=True)
# Subset
filenum=int(os.path.basename(__file__).split("_")[2].split(".")[0])
lower=(filenum-1)*100000
upper=filenum*100000
main_df=main_df[lower:upper].reset_index(drop=True)
# Turn to dict records style
if main_df.shape[0]>0:
      main_df.set_index("raidId").to_csv(sys.stdout)