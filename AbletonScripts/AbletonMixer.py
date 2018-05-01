from _Framework.ButtonElement import ButtonElement
from _Framework.InputControlElement import *
from _Framework.MixerComponent import MixerComponent
from _Framework.SliderElement import SliderElement

from AbletonChannelStrip import AbletonChannelStrip
from Consts import *

class AbletonMixer(MixerComponent):

	def __init__(self):
		MixerComponent.__init__(self, NUM_TRACKS)
		self._strips = [ AbletonChannelStrip(i) for i in range(NUM_TRACKS) ]
		self._sliders = [SliderElement(CC_TYPE, MIDI_CHANNEL, (FADER_START + i)) for i in range(NUM_TRACKS) ]
		self._strip_offset = 0
		self._assigned_tracks = []
		self.song().add_tracks_listener(self.__on_tracks_added_or_deleted)
		self._reassign_strips()

	def _reassign_strips(self):
		track_index = self._strip_offset
		self._assigned_tracks = []
		all_tracks = (self.song().tracks + self.song().return_tracks)
		count = 0
		for strip in self._strips:
			btc = count * 2
			if(track_index < len(all_tracks)):
				track = all_tracks[track_index]
				strip.set_track(track)
				strip.set_volume_control(self._sliders[count])
				self._assigned_tracks.append(track)
			else:
				strip.set_track(None)
				strip.set_volume_control(None)
			track_index += 1
			count += 1

	def __validate_strip_offset(self):
		all_tracks = (self.song().tracks + self.song().return_tracks)
		self._strip_offset = min(self._strip_offset, (len(all_tracks)-1))
		self._strip_offset = max(0,self._strip_offset)

	def __on_tracks_added_or_deleted(self):
		self.__validate_strip_offset()
		self._reassign_strips()