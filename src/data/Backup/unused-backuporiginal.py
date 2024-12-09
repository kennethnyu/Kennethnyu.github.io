import pandas as pd
import sqlite3
import sys
import json
from General import Config
spec_to_color={"Berserker Technique":"#EE2E48","Mayhem":"#EE2E48",
               "Gravity Training":"#7B9AA2","Rage Hammer":"#7B9AA2",
               "Combat Readiness":"#E1907E","Lone Knight":"#E1907E", "Princess Maker":"#E1907E",
               "Predator":"#DB6A42","Punisher":"#DB6A42",
               "Order of the Emperor":"#B38915","Grace of the Empress":"#B38915",
               "Communication Overflow":"#22AA99","Master Summoner":"#22AA99",
               "Igniter":"#66AA00","Reflux":"#66AA00",
               "Esoteric Skill Enhancement":"#AAAA11","First Intention":"#AAAA11",
               "Ultimate Skill: Taijutsu":"#990099","Shock Training":"#990099",
               "Energy Overflow":"#316395","Robust Spirit":"#316395",
               "Control":"#F6DA6A","Pinnacle":"#F6DA6A",
               "Deathblow":"#994499","Esoteric Flurry":"#994499",
               "Asura's Path":"#4DE3D1","Brawl King Storm":"#4DE3D1",
               "Remaining Energy":"#A91A16","Surge":"#A91A16",
               "Demonic Impulse":"#0099C6","Perfect Suppression":"#0099C6",
               "Hunger":"#109618","Lunar Voice":"#109618",
               "Full Moon Harvester":"#C16ED0","Night's Edge":"#C16ED0",
               "Death Strike":"#DD4477","Loyal Companion":"#DD4477",
               "Enhanced Weapon":"#4442A8","Pistoleer":"#4442A8",
               "Barrage Enhancement":"#33670B","Firepower Enhancement":"#33670B",
               "Arthetinean Skill":"#3B4292","Evolutionary Legacy":"#3B4292",
               "Peacemaker":"#6BCEC2","Time to Hunt":"#6BCEC2",
               "Drizzle":"#084BA3","Wind Fury":"#084BA3"}

conn=sqlite3.connect("src/data/Snow_Argeos.db")
query="""
SELECT spec, dps FROM players
WHERE class NOT IN ('Artist','Bard','Paladin')
AND spec!='Princess'
AND gearScore<1680
"""
df=pd.read_sql_query(query, conn)
# Display in millions, rounded to 2 decimals
df["dps"]=(df["dps"].astype(int)/1000000).round(2)
# Add 1st and 99th percentile
df=df.groupby(["spec"])["dps"].describe(percentiles=[0.01,0.25,0.75,0.99]).reset_index()
# Add color
df["color"]=df["spec"].map(spec_to_color)
# Create index
df["spec"]=df["spec"]+" ("+df["count"].astype(int).astype("str")+")"
# Rename some columns
df.rename(columns={"1%":"q01",
                   "25%":"q25",
                   "50%":"median",
                   "75%":"q75",
                   "99%":"q99"
                   },inplace=True)
# Sort
df.sort_values("median", inplace=True)


df_json=df.to_dict("records")

json.dump(df_json, sys.stdout)