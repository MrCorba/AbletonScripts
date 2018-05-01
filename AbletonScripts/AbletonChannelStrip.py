from _Framework.ChannelStripComponent import ChannelStripComponent

class AbletonChannelStrip(ChannelStripComponent):

    def __init__(self, id):
        ChannelStripComponent.__init__(self)
        self._track_id = id
