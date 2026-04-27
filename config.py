# Name: Mubbasher Ahmed
# Date: 2026-04-27
import os

class Config:
    MYSQL_HOST = os.environ.get('MYSQL_HOST', 'db-primary')
    HEALTH_CHECK_INTERVAL = int(os.environ.get('HEALTH_CHECK_INTERVAL', '10'))