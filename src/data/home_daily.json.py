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
# Iterate and merge them before collecting in main dataframe to save space.
main_df=pd.DataFrame()
for r_db, p_db in zip(raids_list, players_list):
    raids=pd.read_parquet(r_db)
    players=pd.read_parquet(p_db)
    raids=raids[raids["statusCode"]==200].reset_index(drop=True)
    rp_raw=raids.merge(players, how="left", on=["raidId"])
    rp_raw["serverdate"]=rp_raw["timestamp"].apply(lambda x: dt.datetime.fromtimestamp(int(x/1000)).date()).astype("str")
    # Calculate aggregates
    def calc_aggs(row):
        aggs={}
        aggs["logs"]=row["raidId"].nunique()
        aggs["ap_active"]=row["arkPassiveActive"].sum()
        aggs["all_data"]=row["raidId"].count()
        return pd.Series(aggs, index=["logs","ap_active","all_data"])
    df=rp_raw.groupby(["serverdate"]).apply(calc_aggs)
    # conn=sqlite3.connect("src/data/databases/{}".format(db))
    # query="""
    # SELECT DATE(ROUND(r.timestamp / 1000), 'unixepoch') AS serverdate,
    # COUNT(DISTINCT r.raidId) AS logs,
    # COUNT(CASE WHEN arkPassiveActive THEN 1 END) AS ap_active,
    # COUNT(1) AS all_data
    # FROM raids AS r
    # LEFT JOIN players AS p ON r.raidId=p.raidId
    # WHERE r.statusCode=200
    # GROUP BY serverdate
    # """
    # df=pd.read_sql_query(query, conn) 
    if df.shape[0]>0:
        main_df=pd.concat([main_df,df.reset_index()]).reset_index(drop=True)

# Final aggregate
main_df=main_df.groupby(["serverdate"]).sum().reset_index()
# Calculate apa %
def safe_div(n,d):
    try:
        return n/d
    except:
        return 0
# Apply
main_df["arkactive"]=pd.Series([round(safe_div(n,d)*100,1) for n,d in zip(main_df["ap_active"],main_df["all_data"])])

# Turn to dict records style
df_json=main_df.to_dict("records")
# Dump
json.dump(df_json, sys.stdout)