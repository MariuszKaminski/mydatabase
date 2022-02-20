import os
import pymysql

# Get username from Gitpod workspace
# (modify this variable if runnin on another environment)

username = os.getenv('C9_USER')

# Connect to the database
connection = pymysql.connect(host='localhost',
                            user=username,
                            password='',
                            db='Chinook')

try:
    #Run a query
    with connection.cursor() as cursor:
        list_of_names = ['Fred', 'fred']
        #Prepare a string with the same number of placeholders as in list_of_names
        format_strings = ','.join(['%s']*len(list_of_names))
        cursor.execute("DELETE FROM Friends WHERE name in ({});".format(format_strings), list_of_names)
        connection.commit()
finally:
    # Close the connection, regardelss of wheter the above was successful
    connection.close()