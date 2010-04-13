#!/usr/bin/env python

# Copyright (C) 2009 John Reese, LeetCode.net
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

import pynotify
import sys

class Event:
	"""
	Basic pianobar event handler to interpret event_command output to actions
	useful to the rest of the python wrapper, including libnotify messages.
	"""

	def __init__(self):
		"""
		Initialize the pianobar event handler and pynotify
		"""

		if not pynotify.init("pianobar-python"):
			raise Exception("error initializing pynotify")

	def execute(self, type, params={}):
		"""
		Read event parameters from stdin and handle events appropriately.
		"""

		# Error from pianobar -- generate a notification and stop event handling
		if params["pRet"] != "1":
			print "error #%s: '%s'" % (params["pRet"], params["pRetStr"])
			pynotify.Notification("pianobar error #%s" % params["pRet"], params["pRetStr"]).show()
			return

		# Handle specific events
		if type == "songstart":
			pynotify.Notification(params["title"], "by %s from %s"%(params["artist"], params["album"])).show()


if __name__ == "__main__":
	# Read event type from command arguments
	if len(sys.argv) < 2:
		print "error reading event type from command arguments"

	type = sys.argv[1]

	# Read parameters from input
	params = {}
	for s in sys.stdin.readlines():
		param, value = s.split("=", 1)
		params[param.strip()] = value.strip()

	# Call the event handler
	Event().execute(type, params)

