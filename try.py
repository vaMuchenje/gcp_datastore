#!/usr/bin/python
import getpass
import sys

# Add the Python SDK to the package path.
# Adjust these paths accordingly.

sys.path.append('~/google_appengine')
sys.path.append('~/google_appengine/lib/yaml/lib')

from google.appengine.ext.remote_api import remote_api_stub
from google.appengine.ext import db
import models

# Your app ID and remote API URL path go here.
APP-ID = 'app-id'
REMOTE_API_PATH = '/remote_api'


def auth_func():
 	email_address = raw_input('Email address: ')
 	password = getpass.getpass('Password: ')
 	return email_address, password

def initialize_remote_api(app-id=APP-ID, path=REMOTE_API_PATH):
 	remote_api_stub.ConfigureRemoteApi(app-id, path, auth_func)
 	remote_api_stub.MaybeInvokeAuthentication()

def main(args):
 	initialize_remote_api()
 	pgs = models.Programs.all().fetch(2)
 	for pg in pgs:
 		print pg.app_name
 		return 0


if __name__ == '__main__':
	 sys.exit(main(sys.argv[1:]))