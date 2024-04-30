class BaseException(Exception):
	"""A base class exception for app_name exceptions."""

class ConfigError(Exception):
	def __init__(self, message):
		self.message = message
