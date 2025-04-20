import mysql.connector
from mysql.connector import Error

def get_db_connection():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            database='pharmadb',
            user='root',  # You'll need to change this
            password=''   # You'll need to change this
        )
        return connection
    except Error as e:
        print(f"Error connecting to MySQL Database: {e}")
        return None

def execute_procedure(proc_name, params=None):
    connection = get_db_connection()
    if connection is None:
        return None
    
    try:
        cursor = connection.cursor(dictionary=True)
        if params:
            cursor.callproc(proc_name, params)
        else:
            cursor.callproc(proc_name)
        
        # Fetch results from all result sets
        results = []
        for result in cursor.stored_results():
            results.extend(result.fetchall())
        
        connection.commit()
        return results
    except Error as e:
        print(f"Error executing procedure {proc_name}: {e}")
        return None
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
