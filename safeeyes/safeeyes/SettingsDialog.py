# Safe Eyes is a utility to remind you to take break frequently
# to protect your eyes from eye strain.

# Copyright (C) 2016  Gobinath

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk, GdkX11

class SettingsDialog:
	"""docstring for SettingsDialog"""
	def __init__(self, config, language, on_save_settings, glade_file):
		self.config = config
		self.on_save_settings = on_save_settings

		builder = Gtk.Builder()
		builder.add_from_file(glade_file)
		builder.connect_signals(self)

		self.window = builder.get_object("window_settings")
		self.spin_short_break_duration = builder.get_object("spin_short_break_duration")
		self.spin_long_break_duration = builder.get_object("spin_long_break_duration")
		self.spin_interval_between_two_breaks = builder.get_object("spin_interval_between_two_breaks")
		self.spin_short_between_long = builder.get_object("spin_short_between_long")
		self.spin_time_to_prepare = builder.get_object("spin_time_to_prepare")
		self.switch_strict_break = builder.get_object("switch_strict_break")

		builder.get_object("lbl_short_break").set_label(language['ui_controls']['short_break_duration'])
		builder.get_object("lbl_long_break").set_label(language['ui_controls']['long_break_duration'])
		builder.get_object("lbl_interval_bettween_breaks").set_label(language['ui_controls']['interval_between_two_breaks'])
		builder.get_object("lbl_short_per_long").set_label(language['ui_controls']['no_of_short_breaks_between_two_long_breaks'])
		builder.get_object("lbl_time_to_prepare").set_label(language['ui_controls']['time_to_prepare_for_break'])
		builder.get_object("lbl_strict_break").set_label(language['ui_controls']['strict_break'])
		builder.get_object("btn_cancel").set_label(language['ui_controls']['cancel'])
		builder.get_object("btn_save").set_label(language['ui_controls']['save'])

		self.spin_short_break_duration.set_value(config['short_break_duration'])
		self.spin_long_break_duration.set_value(config['long_break_duration'])
		self.spin_interval_between_two_breaks.set_value(config['break_interval'])
		self.spin_short_between_long.set_value(config['no_of_short_breaks_per_long_break'])
		self.spin_time_to_prepare.set_value(config['pre_break_warning_time'])
		self.switch_strict_break.set_active(config['strict_break'])


	def show(self):
		self.window.show_all()

	def on_window_delete(self, *args):
		self.window.destroy()

	def on_save_clicked(self, button):
		self.config['short_break_duration'] = self.spin_short_break_duration.get_value_as_int()
		self.config['long_break_duration'] = self.spin_long_break_duration.get_value_as_int()
		self.config['break_interval'] = self.spin_interval_between_two_breaks.get_value_as_int()
		self.config['no_of_short_breaks_per_long_break'] = self.spin_short_between_long.get_value_as_int()
		self.config['pre_break_warning_time'] = self.spin_time_to_prepare.get_value_as_int()
		self.config['strict_break'] = self.switch_strict_break.get_active()

		self.on_save_settings(self.config)	# Call the provided save method
		self.window.destroy()	# Close the settings window

	def on_cancel_clicked(self, button):
		self.window.destroy()
