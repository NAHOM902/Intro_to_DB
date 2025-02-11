import mysql.connector
from mysql.connector import Error

def create_database():
    try:
        mydb =mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "password",
            port = "3306"
        )

        if mydb.is_connected():
            cursor = mydb.cursor()
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("DATABASE 'alx_book_store' created successfully or already eXists.")

            cursor.close()
    except mysql.connector.Error as e:
        print(f"Error: {e}")
    finally:

        if mydb.is_connected():
            mydb.close()
            print("MYSQL CONNECTION CLOSED.")

if __name__ == "__main__":
    create_database()
