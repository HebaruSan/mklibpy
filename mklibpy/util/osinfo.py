import platform
import sys

__author__ = 'Michael'

system = platform.system()
LINUX = system == "Linux"
WINDOWS = system == "Windows"
MAC = system == "Darwin"

py_version = sys.version_info
PYTHON2 = py_version.major == 2
PYTHON3 = py_version.major == 3
