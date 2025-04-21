import logging
import os
import time
from logging.handlers import RotatingFileHandler
from datetime import datetime

# Create logs directory if it doesn't exist
log_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'logs')
if not os.path.exists(log_dir):
    os.makedirs(log_dir)

# Set up the database logger
db_logger = logging.getLogger('database')
db_logger.setLevel(logging.DEBUG)

# Create a rotating file handler for database logs
db_log_file = os.path.join(log_dir, 'database.log')
db_handler = RotatingFileHandler(db_log_file, maxBytes=10485760, backupCount=5)  # 10MB files, keep 5 backups
db_handler.setLevel(logging.DEBUG)

# Create a formatter for the logs
formatter = logging.Formatter('[%(asctime)s] %(levelname)s in %(module)s: %(message)s')
db_handler.setFormatter(formatter)

# Add the handler to the logger
db_logger.addHandler(db_handler)

# Set up the application logger
app_logger = logging.getLogger('app')
app_logger.setLevel(logging.DEBUG)

# Create a rotating file handler for application logs
app_log_file = os.path.join(log_dir, 'app.log')
app_handler = RotatingFileHandler(app_log_file, maxBytes=10485760, backupCount=5)
app_handler.setLevel(logging.DEBUG)
app_handler.setFormatter(formatter)

# Add the handler to the logger
app_logger.addHandler(app_handler)

# Log request/response information
def log_db_access(proc_name, params=None, result=None, error=None):
    """
    Log database access with procedure name, parameters, result, and any errors
    """
    log_message = f"DB CALL: {proc_name}"
    
    if params:
        log_message += f", PARAMS: {params}"
    
    if result is not None:
        # Truncate large results for readability
        result_str = str(result)
        if len(result_str) > 1000:
            result_str = result_str[:1000] + "... [truncated]"
        log_message += f", RESULT: {result_str}"
    
    if error:
        log_message += f", ERROR: {error}"
        db_logger.error(log_message)
    else:
        db_logger.info(log_message)

# Log application requests
def log_request(route, method, params=None):
    """
    Log API requests with route, method, and parameters
    """
    log_message = f"REQUEST: {method} {route}"
    
    if params:
        log_message += f", PARAMS: {params}"
    
    app_logger.info(log_message)

# Log application responses
def log_response(route, status_code, data=None):
    """
    Log API responses with route, status code, and response data
    """
    log_message = f"RESPONSE: {route}, STATUS: {status_code}"
    
    if data:
        # Truncate large responses for readability
        data_str = str(data)
        if len(data_str) > 1000:
            data_str = data_str[:1000] + "... [truncated]"
        log_message += f", DATA: {data_str}"
    
    app_logger.info(log_message) 