# Branch: Add Healthcheck
import os
class Config:
    MYSQL_HOST = 'db-primary'
    HEALTH_CHECK_INTERVAL = 10