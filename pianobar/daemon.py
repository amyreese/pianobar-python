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


import dbus
import dbus.service
import dbus.mainloop.glib

import gobject

from control import Control

class Daemon:
	"""
	Basic daemon designed to receive signals from Gnome media keys via dbus,
	and deliver those to the cotrol fifo that pianobar is listening to.  Currently
	requires that the pianobar control fifo is already created, and that pianobar
	has been started and a station selected.
	"""

	def __init__(self):
		dbus.mainloop.glib.DBusGMainLoop(set_as_default=True)
		self.control = Control()
		self.bus = dbus.SessionBus()

	def run(self):
		mediakey_object = self.bus.get_object("org.gnome.SettingsDaemon","/org/gnome/SettingsDaemon/MediaKeys")
		mediakey_object.connect_to_signal("MediaPlayerKeyPressed", self.control.mediakey)

		mainloop = gobject.MainLoop()
		print "daemon started."
		mainloop.run()

if __name__ == "__main__":
	Daemon().run()

