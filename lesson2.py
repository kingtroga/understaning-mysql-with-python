"""Creating/Showing a Db"""
from getpass import getpass
from mysql.connector import connect, Error

try:
    with connect(
        host="localhost",
        user=input("Enter Username: "),
        password=getpass("Enter password: "),
    ) as connection:
        create_db_query = "CREATE DATABASE online_movie_rating"
        show_db_query = "SHOW DATABASES"
        with connection.cursor(buffered=True) as cursor:
            #cursor.execute(create_db_query)
            cursor.execute(show_db_query)
            for db in cursor:
                print(db)
            
except Error as e:
    print(e)