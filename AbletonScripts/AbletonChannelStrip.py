from _Framework.ChannelStripComponent import ChannelStripComponent

from Sysex import Sysex

class AbletonChannelStrip(ChannelStripComponent):

	def __init__(self, id):
		ChannelStripComponent.__init__(self)
		self._track_id = id

	def send_init(self):
		self._send_state()

	def _send_state(self):
		sysex = Sysex('TRACK')
		sysex.byte(self._track_id)
		sysex.ascii(self._track is not None and self._track.name or '')
		if self._track in self.song().tracks:
			sysex.ascii(str(list(self.song().tracks).index(self._track) + 1))
		elif self._track in self.song().return_tracks:
			sysex.ascii(
				chr(list(self.song().return_tracks).index(self._track) + 65))
		else:
			sysex.ascii(' ')
		sysex.send()
