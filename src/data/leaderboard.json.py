import datetime as dt
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
    raids=raids[raids["timestamp"]>=(dt.datetime.timestamp(dt.datetime.now())-(7*86400))*1000].reset_index()[["raidId","region"]]
    df=raids.merge(players,how="left")
    df=df[df["name"].apply(lambda x: True if "#" not in x else False)].reset_index(drop=True)

    if df.shape[0]>0:
        df=df.groupby(["name","spec","region"])["gearScore"].max().reset_index().rename(columns={"gearScore":"maxgear"})
        main_df=pd.concat([main_df,df]).reset_index(drop=True)

# Group by name and spec
main_df=main_df.groupby(["name","spec","region"]).max().reset_index()
# Sort by most gear
main_df=main_df.sort_values("maxgear",ascending=False).head(50000).reset_index(drop=True)
# Obfus te names
def obfuscate_name(name):
    middlename="".join(["*" for n in name[1:-1]])
    return "{start}{middlename}{end} - ({length})".format(start=name[0].upper(),middlename=middlename,end=name[-1],length=len(name))
main_df["name"]=main_df["name"].apply(obfuscate_name)
# Round maxgear
main_df["maxgear"]=main_df["maxgear"].round(2)
# Create ranks
main_df.reset_index(inplace=True)
main_df.rename(columns={"index":"Rank","name":"Name","spec":"Specialization","maxgear":"Gearscore","region":"Region"},inplace=True)
main_df["Rank"]=main_df["Rank"]+1
# Set index
main_df=main_df.set_index("Rank")
cols=["Name","Specialization","Gearscore","Region"]

# Turn to dict records style
main_df[cols].to_csv(sys.stdout)