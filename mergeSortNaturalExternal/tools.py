import ntpath
import tkinter as tk
from tkinter import filedialog


def file_len(fname):
    i = -1
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1


def file_choose():
    """
    That's just an easy way to choose test files

    """
    print("Choose a file to sort")
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename()
    tail = ntpath.split(file_path)
    file_name = tail[1]
    return file_name


def copy_to_another_and_split(from_this, to_this):
    """
    delete all comas and rewrite it to a new file

    """
    copy_from = open(from_this, "r")
    copy_to = open(to_this, "w")
    copy_to.truncate()
    data = copy_from.read().split(',')
    for i in range(len(data)):
        copy_to.write(data[i]+'\n')
    copy_from.close()
    copy_to.close()


def read_int(file):
    """
    reads an str from file and convert it to number

    """
    num_str = file.readline()
    if num_str != "`\n" and num_str != '':
        num = int(num_str.replace("\n", ""))
        return num
    return None


def swap_active_files(active_file):
    """
    function to swap file with to write

    """
    if active_file == "f1":
        active_file = "f2"
    else:
        active_file = "f1"
    return active_file


def write_to_active_file(active_file, num, f1, f2):
    """
    Writes to active file

    """
    if active_file == "f1":
        f1.write(str(num)+"\n")
    else:
        f2.write(str(num)+"\n")


def write_to_main_file(f, num):
    """
    writing to main exit file

    """
    f.write(str(num)+"\n")


def end_of_range(num):
    if num is None:
        return True
    else:
        return False
