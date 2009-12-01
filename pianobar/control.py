
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

from os import path

class Control:
	"""
	Object for controlling a running pianobar instance via fifo.
	"""

	def __init__(self, fifo="~/.config/pianobar/ctl"):
		self.fifo = open(path.abspath(path.expanduser(fifo)), "w")

	def play(self):
		self.fifo.write("p\n")
		self.fifo.flush()

	def pause(self):
		self.fifo.write("p\n")
		self.fifo.flush()

	def stop(self):
		self.fifo.write("q\n")
		self.fifo.flush()

	def next(self):
		self.fifo.write("n\n")
		self.fifo.flush()

	def previous(self):
		# currently not possible with pandora/pianobar
		pass

	def mediakey(self, *keys):
		"""
		Interprets signals from org.gnome.SettingsDaemon.MadiaKeys to pass
		the appropriate commands to pianobar.
		"""

		for key in keys:
			if key == "Play":
				self.play()

			if key == "Stop":
				self.stop()

			if key == "Next":
				self.next()

			if key == "Previous":
				self.previous()

