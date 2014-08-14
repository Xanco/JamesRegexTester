import sys
from cx_Freeze import setup, Executable

includes = ["re", "Tkinter", "PyV8", "ctypes","RegexSaver"]
excludes = []
packages = []
path = ["libs"]


base = None
if sys.platform == 'win32':
    base = 'Win32GUI'

executables = Executable('mainUI.py', base=base, targetName = "JavaScript Regex Tester.exe", icon="icon.ico")

setup(name='simple_Tkinter',
      version='0.1',
      description='Sample cx_Freeze Tkinter script',
      executables=[executables]
      )