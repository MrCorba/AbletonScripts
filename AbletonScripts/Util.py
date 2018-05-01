from _Framework.ButtonElement import ButtonElement

from Consts import *

def momentary_cc_button(midi_id):
    return ButtonElement(IS_MOMENTARY, CC_TYPE, MIDI_CHANNEL, midi_id)
