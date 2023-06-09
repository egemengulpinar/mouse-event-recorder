########################################
##                                    ##
##      Author : Egemen Gulpinar      ##
##  Mail : egemengulpinar@gmail.com   ##
##     github.com/egemengulpinar      ##
##                                    ##
########################################
import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
INCLUDES = []
build_exe_options = {"build_exe": "Mouse Event Recorder"}

base = None
if sys.platform == "win32":
    base = "Console" #Console previous

EXE = Executable(script="event.py",
                 base=base,
                 targetName="Mouse Event Recorder.exe",
                 initScript=None,
                 copyright="Egemen Gulpinar"
                 )


# base="Win32GUI" should be used only for Windows GUI app


setup(
    name = "Mouse Event Recorder",
    version = "1.0",
    description = "Created by Egemen Gulpinar",
    options = {"build_exe": build_exe_options},
    executables = [EXE]

)

#python setup_main.py build -b .