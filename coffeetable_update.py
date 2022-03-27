# -*- coding: utf-8 -*-
"""
Created on Wed Jan 19 13:46:06 2022

@author: Arellano


idea!!
i = 0
for i to len(df):
    if df1[3,i] == df[2,i];
    
    
Notes:
-Make sure trades data is complete (data1)
-Refer the "partners" from trades table  (data2)
-Export available!
    
"""


import pandas as pd

print(" \n\n#############################################\n Running Code \n#######################################")
#load table
trades_df = (pd.read_csv('Brazil_coffee_trades_final.csv', encoding = 'unicode_escape'))
print(trades_df.head)


#load coord source
#use iat or at [[row,column]]
coord_df = (pd.read_csv('country_coord.csv', encoding = 'unicode_escape'))
print(coord_df.head)
# print("lat US",coord_df.iat[1,1])


#check for duplicates and missing values/NaN
print(" \n #Data Checking    -------------------------------------")
print(" \nCheck Duplicates in Latitude : \n\n",
      coord_df.duplicated(subset=["Partner_lat"]))
print(" \nCheck Duplicates in Longitude : \n\n",
      coord_df.duplicated(subset=["Partner_lon"]))
print(" \nCount total NaN at each column of Trades dataframe : \n\n",
      trades_df.isnull().sum())
print(" \nCount total NaN at each column of Coords dataframe : \n\n",
      coord_df.isnull().sum())


#get column
country = trades_df["Partner"]
country_source = coord_df["Partner"]
reporter = trades_df["Reporter"].str.strip()
print("\nnumber of countries:",len(country))
print("number of unique countries from source coord:",len(country_source))
#print(countries[0]==country_source[0])


#index = returns RangeIndex (Start, Stop, Increment)
#print(trades_df.index)
#shape: shape[0]==no of rows  shape[1]==no of cols
#print(trades_df.shape[1])
#len: return no of rows, not including the header
#print(len(trades_df))
#example
# unique_index = pd.Index(list('abc'))
# print(unique_index)
# print(unique_index.get_loc('b'))


#loop Partner!
x=0
y=0
count =1
list_lat = []
list_lon = []
for x in range(0,len(country)):
    # print("---- new Country iteration --------", count)
    # print(list_lat)
    for y in range(0,len(country_source)):
        # print("x",x)
        # print("y",y)
        if country[x] == country_source[y]:
            #ref = country_source.get_loc(y)
            #print("index", ref)
            # print("x", country[x])
            # print("y", country_source[y])
            # print("MATCH")
            list_lat.append(coord_df.at[y,"Partner_lat"])
            list_lon.append(coord_df.at[y,"Partner_lon"])
            x =x+1
            # print("#")
            break
            #y = 0
        else:
            # print("x", country[x])
            # print("y", country_source[y])
            # print("need to increment y")
            continue
    count = count +1

# print("lat",list_lat)
# print("lon",list_lon)
print("length list_lat", len(list_lat))
print("length list_lon", len(list_lon))


#loop reporter!
x=0
y=0
count =1
rep_lat = []
rep_lon = []
for x in range(0,len(reporter)):
    # print("---- new Country iteration for Reporter --------", count)
    # print(rep_lat)
    for y in range(0,len(country_source)):
        # print("x",x)
        # print("y",y)
        if reporter[x] == country_source[y]:
            # print("x", reporter[x])
            # print("y", country_source[y])
            # print("MATCH")
            rep_lat.append(coord_df.at[y,"Partner_lat"])
            rep_lon.append(coord_df.at[y,"Partner_lon"])
            x =x+1
            # print("#")
            break
            #y = 0
        else:
            # print("x", reporter[x])
            # print("y", country_source[y])
            # print("need to increment y")
            continue
    count = count +1
        
# print("rep lat",rep_lat)
# print("rep lon",rep_lon)  


#backup df
new_df = trades_df.copy()
new_df = new_df.assign(Partner_lat=list_lat)
new_df = new_df.assign(Partner_lon=list_lon)
new_df = new_df.assign(Reporter_lat=rep_lat)
new_df = new_df.assign(Reporter_lon=rep_lon)

#see new df
print(new_df[["Reporter","Partner","Partner_lat","Partner_lon"]])

#export
# new_df.to_csv("updated_trades_sample7.csv",encoding='utf-8-sig', index=False)
# print(" \n\n ### -- New Table exported!  --  ### \n")
print("\n\n                    --- (end) --- ")