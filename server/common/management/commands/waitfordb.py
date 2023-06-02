import time

from django.core import management

class Command(management.base.BaseCommand):
    help = 'Wait for db to be available'

    def handle(self, *args, **options):
        attempts = 5
        for _ in range(attempts):
            try:
                management.call_command('makemigrations')
                management.call_command('migrate')
                return
            except:
                time.sleep(10)
                continue

        raise management.CommandError('Database not yet available!')