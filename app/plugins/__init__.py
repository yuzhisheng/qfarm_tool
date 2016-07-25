# import importlib
from os.path import dirname, basename, isfile
import glob
modules = glob.glob(dirname(__file__)+"/*.py")
__all__ = [ basename(f)[:-3] for f in modules if isfile(f)]
# import sys
# sys.path.append(".")
# import plugin_config_check
# print sys.stderr, str(plugin_config_check)
# __import__("plugin_config_check.py")
# for f in modules:
# 	if isfile(f):
# 	# if mname.startswith("plugin"):
# 		mod = __import__(f)
# 		print sys.stderr, mod.PLUGIN_NAME
