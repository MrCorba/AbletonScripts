from _Framework.TransportComponent import TransportComponent

from Consts import *
from Util import momentary_cc_button, toggle_cc_button

class AbletonTransport(TransportComponent):

    def __init__(self):
        TransportComponent.__init__(self)
        self.set_up_controls()

    def set_up_controls(self):
        self.set_play_button(momentary_cc_button(PLAY_BUTTON))
        self.set_stop_button(momentary_cc_button(STOP_BUTTON))
        self.set_seek_forward_button(momentary_cc_button(FFWD_BUTTON))
        self.set_seek_backward_button(momentary_cc_button(RWD_BUTTON))
        self.set_record_button(momentary_cc_button(REC_BUTTON))
        self.set_loop_button(momentary_cc_button(LOOP_BUTTON))
        self.set_metronome_button(toggle_cc_button(METRONOME))
        self.set_tap_tempo_button(toggle_cc_button(TAP_TEMPO))
        self.setup_punch_buttons()
        self.setup_nudge_buttons()

    def setup_punch_buttons(self):
        self.set_punch_in_button(momentary_cc_button(PUNCH_IN))
        self.set_punch_out_button(momentary_cc_button(PUNCH_OUT))

    def setup_nudge_buttons(self):
        self.set_nudge_up_button(momentary_cc_button(NUDGE_UP))
        self.set_nudge_down_button(momentary_cc_button(NUDGE_DOWN))
