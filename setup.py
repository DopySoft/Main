import sys

from cx_Freeze import setup, Executable

base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(
        name = "simple_PyQt4",
        version = "0.1",
        description = "yolz",
<<<<<<< HEAD
        executables = [Executable(r"C:\Users\Rohit\Downloads\DOPY\soft work\new code\soft\fresh\latest oasis\mainWindow.py", base = base)])
=======
        executables = [Executable(r"C:\Users\Rohit\Desktop\soft work\new code\soft\fresh\mainWindow.py", base = base)])
>>>>>>> 088001604e17d143ebc21dcd1aced053e32305bf
        #executables = [Executable(r"C:\Users\Rohit\Desktop\soft work\new code\soft\fresh\mainWindow.py")])
