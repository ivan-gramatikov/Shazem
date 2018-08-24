import sqlite3

songlist = []
try:
   conn = sqlite3.connect('library.db')
except IOError:
   print("Could not open the database")

cursor = conn.execute("SELECT artist_name, title from track")
for row in cursor:
   singlesong = row[0], row[1]
   songlist.append(singlesong)

# Take the songlist and look at the lines below for a hint ;) You know what to do...

# for element in songlist:
#    youtube-dl "ytsearch1: ......"

conn.close()
