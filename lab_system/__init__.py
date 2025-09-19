# Ensure admin customizations are loaded on Django startup
try:
	from . import admin as _admin  # noqa: F401
except Exception:
	# avoid breaking startup if admin import fails
	_admin = None
