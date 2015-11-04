from django.contrib.staticfiles.management.commands.runserver import Command as RunServerCommand

from ._grunt import start_grunt as execute_grunt

class Command(RunServerCommand):
"""
gruntserver starts the Django dev server while starting
a grunt process in the background. Currently just calls 'watch'.
"""


    def get_handler(self, *args, **options):
    	# TODO: get grunt args from manage.py gruntserver call
        self.start_grunt('watch')
        return super(Command, self).get_handler(*args, **options)

    def start_grunt(self, grunt_args=None):
    	grunt_args = 'watch' if not grunt_args
        execute_grunt(self, grunt_args)