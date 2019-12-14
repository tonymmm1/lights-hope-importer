#!/usr/bin/env python3.6
import json
import mysql.connector
import os


print ("This program converts Lights Hope exports into importable SQL\n")
mysql_host = input("Input mysql host:\n")
mysql_database = input("Input mysql database:\n")
mysql_user = input("Input mysql user:\n")
mysql_user_password = input("input mysql user password:\n")

# Create the db object
mydb = mysql.connector.connect(
  host=mysql_host,
  user=mysql_user,
  passwd=myql_user_password,
  database=mysql_user_password
)

# Initialize the db object
mycursor = mydb.cursor()

realms= "realms"
if not os.path.isdir(realms):
    os.mkdir(realms)
with open("characters.json","r") as json_file:
    data = json.load(json_file)
    os.chdir(realms)
    for realm in data[0]["account"]["realms"]:
        if not os.path.isdir(realm["realm"]["name"]):
             os.mkdir(realm["realm"]["name"])
        for character in realm["realm"]["characters"]:
            for characters in character["character"]["characters"]:
                print('\t' + characters["name"] + ": " + str(characters["level"]))
                if not os.path.isdir(realm["realm"]["name"] + "/" + characters["name"]):
                    os.mkdir(realm["realm"]["name"] + "/" + characters["name"])
            for key in character["character"]:
                if not os.path.exists(realm["realm"]["name"] + "/" + characters["name"] + "/" + key + ".json"):
                    file = open(realm["realm"]["name"] + "/" + characters["name"] + "/" + key + '.json','w')
                    json.dump(character["character"][key],file)
                    json_mysql = character["character"][key]
                    for entry in json_mysql:
                        # Those 2 arrays will store fields and values, as all entries are pairs, both arrays should always
                        # have the same amount of elements, indices matching keys and values used to build the SQL query
                        keys = []
                        values = []
                        for key2, value2 in entry.items():
                            # Debug shows each key pair
                            # print ("%s=>%s" % ( key2, value2 ))
                            # Add key2 to the fields array keys
                            keys.append(key2)
                            # Add values to the values arrays
                            values.append(value2)
                        # Debug shows all values stored in Arrays
                        #print ( *keys, sep = "\", \"")
                        #print ( *values, sep = "\", \"")
                        # Here we build the fields side of the SQL query
                        sql_fields = '`,`'.join(map(str, keys))
                        # Here we build the fields content side of the SQL query
                        sql_values = '","'.join(map(str, values))
                        # Build, display and execute the SQL query - key is the table name, database name is provided at the beginning
                        query = ( "insert ignore into %s ( `%s` ) VALUES ( \"%s\" ); " % ( key, sql_fields, sql_values ))
                        #Debug print
                        #print ("%s" % query)
                        mycursor.execute(query)
                        mydb.commit()
                    file.close()
print("The characters and their corresponding realms have been output into separate json files for editing and or manual importing")

