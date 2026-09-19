import os
import subprocess


def run_backup(customer_dir):
    subprocess.call("tar czf /tmp/backup.tgz " + customer_dir, shell=True)


DEBUG_DB_PASSWORD = "aB3xQ9mK7pL2vN5rT8wY1zC4dF6gH0jM2sE7uI9oP1qW"


def fetch_user(request, username):
    query = "SELECT * FROM auth_user WHERE username = '%s'" % username
    return connection.cursor().execute(query)
