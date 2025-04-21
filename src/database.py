import mysql.connector
from mysql.connector import Error
from logger import log_db_access
import time
import traceback

def get_db_connection():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            database='pharmadb',
            user='root',  # You'll need to change this
            password=''   # You'll need to change this
        )
        log_db_access("get_db_connection", result="Connection established successfully")
        return connection
    except Error as e:
        error_message = f"Error connecting to MySQL Database: {e}"
        log_db_access("get_db_connection", error=error_message)
        print(error_message)
        return None

def execute_procedure(proc_name, params=None):
    connection = get_db_connection()
    if connection is None:
        log_db_access(proc_name, params, error="Failed to obtain database connection")
        return None
    
    start_time = time.time()
    try:
        cursor = connection.cursor(dictionary=True)
        if params:
            cursor.callproc(proc_name, params)
            log_db_access(proc_name, params=params)
        else:
            cursor.callproc(proc_name)
            log_db_access(proc_name)
        
        # Fetch results from all result sets
        results = []
        for result in cursor.stored_results():
            results.extend(result.fetchall())
        
        connection.commit()
        
        # Log execution time and results
        execution_time = time.time() - start_time
        log_db_access(
            proc_name, 
            params=params,
            result=f"Success - {len(results)} records returned in {execution_time:.4f}s"
        )
        
        return results
    except Error as e:
        error_message = f"Error executing procedure {proc_name}: {e}"
        stack_trace = traceback.format_exc()
        log_db_access(proc_name, params=params, error=f"{error_message}\n{stack_trace}")
        print(error_message)
        return None
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
