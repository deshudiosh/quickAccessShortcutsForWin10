import ctypes
import os
import sys
from pathlib import Path
from tkinter import Tk, simpledialog
from tkinter.filedialog import askdirectory


def main():
    tk_instance = Tk()
    tk_instance.withdraw()

    shortcuts = askdirectory(title="Select shortcuts directory", initialdir="C:/QuickAccess")
    if not shortcuts:
        return

    target = askdirectory(title="Select shortcut target directory", initialdir="X:/SKYBAR UNIT GHELAMCO/3D")

    if not target:
        return

    name = simpledialog.askstring("name", tk_instance)

    if not name:
        return

    shortcuts = Path(shortcuts)
    target = Path(target)

    symlink = Path(shortcuts) / (name + " symlink")
    junction = Path(shortcuts) / name

    symlink_cmd = f'cmd /C mklink /D "{symlink}" "{target}"'
    print(symlink_cmd)
    os.system(symlink_cmd)

    junction_cmd = f'cmd /c mklink /J "{junction}" "{symlink}"'
    print(junction_cmd)
    os.system(junction_cmd)


#  run elevated from here: https://stackoverflow.com/a/41930586
def elevated():
    def is_admin():
        try:
            return ctypes.windll.shell32.IsUserAnAdmin()
        except:
            return False

    if is_admin():
        main()
    else:
        # Re-run the program with admin rights
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)


if __name__ == '__main__':
    elevated()
