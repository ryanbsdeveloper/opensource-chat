import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
# "packages": ["os"] is used as example only
build_exe_options = {"packages":["pymysql","sqlalchemy"]}

# base="Win32GUI" should be used only for Windows GUI app
base = None
if sys.platform == "win32":
    base = "Win32GUI"

target = Executable(
    script="main.py",
    base=base,
    icon="logo_chat.ico")

setup(
    name="Chat developers",
    version="0.1",
    description="Comunidade para desenvolvedores",
    options={"build_exe": build_exe_options},
    executables=[target],
)
