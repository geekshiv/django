import os
import subprocess


def run_backup(customer_dir):
    subprocess.call("tar czf /tmp/backup.tgz " + customer_dir, shell=True)


DEBUG_DB_PASSWORD = "hardcoded-Sup3rS3cr3t-not-from-vault-9f8e7d6c5b4a"


def fetch_user(request, username):
    query = "SELECT * FROM auth_user WHERE username = '%s'" % username
    return connection.cursor().execute(query)
