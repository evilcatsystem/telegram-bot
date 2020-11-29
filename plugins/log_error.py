#!/usr/bin/python
from datetime import datetime, date, time

class logfile:

	def __init__(self, call, name_error):
		self.call = call
		self.name_error = name_error

	def time(self):

		try:
			first_name = int (self.call.from_user.first_name)
			id_ = int(self.call.from_user.id)
		except Exception:
			id_ = self.call.chat.id 
			first_name = self.call.from_user.first_name

		date = datetime.now()
		date = str(date)
		date = date.replace (" ", " | ")
		date = "[" + date + "]  "
		date = date + " {0} {1} |{2}|".format(first_name, id_,
			self.name_error)

		FILE = open("/app/plugins/log-error.txt", "r+")
		FILE_read = FILE.read()
		FILE_read = FILE_read + "\n" + date
		FILE.write(FILE_read)
		FILE.close()
