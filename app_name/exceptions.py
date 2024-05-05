class BaseException(Exception):
	"""A base class exception for app_name errors."""

class ConfigError(BaseException):
	def __init__(self, message):
		self.message = message
