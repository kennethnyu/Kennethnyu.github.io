import os
import pandas as pd
import sqlite3
import sys
import json
from General import Config
databases=[name for name in os.listdir("src/data/databases") if ".db" in name]

main_df=pd.DataFrame()
for db in databases:
    conn=sqlite3.connect("src/data/databases/{}".format(db))
    query="""
    SELECT DATE(ROUND(r.timestamp / 1000), 'unixepoch') AS serverdate,
    COUNT(DISTINCT r.raidId) AS logs,
    COUNT(CASE WHEN arkPassiveActive THEN 1 END) AS ap_active,
    COUNT(1) AS all_data
    FROM raids AS r
    LEFT JOIN players AS p ON r.raidId=p.raidId
    WHERE r.statusCode=200
    GROUP BY serverdate
    """
    df=pd.read_sql_query(query, conn) 
    if df.shape[0]>0:
        main_df=pd.concat([main_df,df]).reset_index(drop=True)

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