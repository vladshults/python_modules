import sys
from cx_Freeze import setup, Executable
 
# Dependencies are automatically detected, but it might need fine tuning.
#includefiles = ["code/fondamental/functions.py", "code/interface/FichierExemple.py"]
packages = ["os","sys","atexit", "PyQt4.QtCore", "PyQt4.QtGui"]
build_exe_options = {"packages":packages}
 
 
# GUI applications require a different base on Windows (the default is for a
# console application).
base = None
if sys.platform == "win32":
    base = "Win32GUI"
 
setup(  name = "tun_generator",
        version = "0.1",
        description = "NX disec tunnels generator",
        options = {"build_exe": build_exe_options},
        executables = [Executable("tun_generator.py", base=base)])
