# Name: Mubbasher Ahmed
# Date: 2026-04-27
# Description: Unified configuration file resolving conflicts between 
# database host updates and health check interval additions.
# small comment

import os

class Config:
    """Base configuration class for the Sakila Flask application.
    Handles database connection strings and system timeouts.
    """
    # Use environment variables first, then fall back to defaults
    MYSQL_HOST = os.environ.get('MYSQL_HOST', 'db')
    MYSQL_USER = os.environ.get('MYSQL_USER', 'root')
    MYSQL_PASSWORD = os.environ.get('MYSQL_PASSWORD', 'admin')
    MYSQL_DB = os.environ.get('MYSQL_DB', 'sakila')

    # Important: Include BOTH variables from the merge conflict
    CONNECTION_TIMEOUT = int(os.environ.get('CONNECTION_TIMEOUT', '30'))
    HEALTH_CHECK_INTERVAL = int(os.environ.get('HEALTH_CHECK_INTERVAL', '10'))

    SECRET_KEY = os.environ.get('SECRET_KEY', 'your-secret-key-here-change-this-in-production')