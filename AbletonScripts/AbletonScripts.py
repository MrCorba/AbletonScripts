from __future__ import with_statement
from _Framework.ControlSurface import ControlSurface
from AbletonMixer import AbletonMixer
from AbletonTransport import AbletonTransport

import Live

class AbletonScripts(ControlSurface):
	def __init__(self, c_instance):
		ControlSurface.__init__(self, c_instance)
		with self.component_guard():
			self.setup()

		self.show_message("AbletonScripts Connected")

	def setup(self):
		self._set_suppress_rebuild_requests(True)
		self._transport = AbletonTransport()
		self._mixer = AbletonMixer()
		self._set_suppress_rebuild_requests(False)
