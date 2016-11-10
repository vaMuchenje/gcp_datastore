# Copyright 2016 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import webapp2
import csv
from google.appengine.ext import ndb


###### WRITING TO DATASTORE ########

#Define object model as it will leave in the database

class Program(ndb.Model):
	app_name = ndb.StringProperty()
	app_version = ndb.StringProperty()
	app_obtained = ndb.StringProperty()
	app_modified = ndb.StringProperty()
	app_kind = ndb.StringProperty()
	app_is64 = ndb.StringProperty()
	app_signed_by = ndb.StringProperty()
	app_location = ndb.StringProperty()
	app_info_string = ndb.StringProperty()


#Save function
def save_entity(program_name):
    program_key = program_name.put()
    return program_key

#####Individual example #########

# itunes = Program(
# 	app_name='iTunes', app_version='12', app_obtained='Apple', app_modified='8 January 2016', app_kind='Intel', app_is64='Yes', app_signed_by='Software Signing', app_location='Desktop', app_info_string="Copyright Reserved")

# save_entity(itunes)


####External File Example#######

def process_file():
	f = open('file.csv') #File path goes here, alternatively use absolute path to file.
	csv_f = csv.reader(f)

	for row in csv_f:
		 pgrm = Program(
		 	app_name=row[0], app_version=row[1], app_obtained=row[2], app_modified=row[3], app_kind=row[4], app_is64=row[5], app_signed_by=row[6], app_location=row[7], app_info_string=row[8])
		 try:
		 save_entity(pgrm)


process_file()


####Bulk Example (Dump)######
# bulkloader.py --dump --app_id=<app-id> --url=http://<appname>.appspot.com/remote_api --filename=<data-filename>




class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write('Hello, This is a program that stores files from your local files. If you are seeing this message, the file export was successful :)')

app = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)



#####RETRIEVAL FROM DATASTORE#######