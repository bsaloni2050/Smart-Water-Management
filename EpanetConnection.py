import csv, sqlite3
import pandas



con = sqlite3.connect("epanet.db")
cur = con.cursor()
#cur.execute("CREATE TABLE node (Node_id, Elevation,Base_Demand,Initial Quality,Demand,Head,Pressure,Quality);") # use your column names here


path = '/Users/salonibindra/Desktop/output1.csv'
# with open(path,'rb') as fin: # `with` statement available in 2.5+
#     # csv.DictReader uses first line in file for column headings by default
#     dr = csv.DictReader(fin) # comma is default delimiter
#     to_db = [(i['col1'], i['col2']) for i in dr]

df = pandas.read_csv(path)
df.to_sql('epanet', con, if_exists='append', index=False)
#cur.executemany("INSERT INTO t (col1, col2) VALUES (?, ?);", to_db)
x = cur.execute("Select Elevation,Time from epanet where Time between '1:00' and '3:00'")
#
# for i in x:
#     print (i)
# print (x)
#cur.execute("PRAGMA table_info(epanet)")
print(cur.fetchall())
con.commit()
con.close()