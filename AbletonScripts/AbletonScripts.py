from __future__ import with_statement
from _Framework.ControlSurface import ControlSurface
from AbletonMixer import AbletonMixer
from AbletonTransport import AbletonTransport

from Consts import *
from Sysex import Sysex

import Live

class AbletonScripts(ControlSurface):
	def __init__(self, c_instance):
		ControlSurface.__init__(self, c_instance)
		with self.component_guard():
			self._setup()

		self.show_message("AbletonScripts Connected")

	def _setup(self):
		self._set_suppress_rebuild_requests(True)
		Sysex.set_midi_callback(self._send_midi)
		Sysex.set_log(self.log_message)
		self._transport = AbletonTransport()
		self._mixer = AbletonMixer()
		self._set_suppress_rebuild_requests(False)

	def handle_sysex(self,sysex):
		if(sysex[1] == MIXER_SYSEX):
			self._mixer.handle_sysex(sysex[1:])

	def _do_send_midi(self, midi_event_bytes):
		self._c_instance.send_midi(midi_event_bytes)
		return True
