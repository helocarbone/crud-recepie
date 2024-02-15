""""
Django command to wait for db connection to be available
"""
import time

from psycopg2 import OperationalError as Psycopg20pError

from django.db.utils import OperationalError
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """Django command to wait for db connection"""

    def handle(self, *args, **options):
        self.stdout.write('Waiting for db connection...')
        db_up = False
        while db_up is False:
            try:
                self.check(databases=['default'])
                db_up = True
            except (OperationalError, Psycopg20pError):
                self.stdout.write('Db unavailable waiting for 1sec')
                time.sleep(1)
        self.stdout.write(self.style.SUCCESS('Db available'))
