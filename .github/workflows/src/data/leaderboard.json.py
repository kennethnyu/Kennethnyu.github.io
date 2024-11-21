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
    SELECT p.name, p.spec, r.region, MAX(p.gearScore) AS maxgear
    FROM players AS p
    LEFT JOIN raids AS r ON p.raidId=r.raidId
    WHERE r.timestamp/1000 >= (TIME('NOW')-(7*86400))
          AND p.name NOT LIKE '%#%'
    GROUP BY p.name, p.spec, r.region
    """
    df=pd.read_sql_query(query, conn) 
    if df.shape[0]>0:
        main_df=pd.concat([main_df,df]).reset_index(drop=True)

# Group by name and spec
main_df=main_df.groupby(["name","spec"]).max().reset_index()
# Sort by most gear
main_df=main_df.sort_values("maxgear",ascending=False).head(30000).reset_index(drop=True)
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