from _Framework.ControlSurface import ControlSurface

class AbletonScripts(ControlSurface):
	def __init__(self, c_instance):
		ControlSurface.__init__(self, c_instance)
		self.show_message("AbletonScripts Connected")
