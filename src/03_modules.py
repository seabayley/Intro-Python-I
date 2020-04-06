"""
In this exercise, you'll be playing around with the sys module,
which allows you to access many system specific variables and
methods, and the os module, which gives you access to lower-
level operating system functionality.
"""

import os
import sys
# See docs for the sys module: https://docs.python.org/3.7/library/sys.html
# Print out the command line arguments in sys.argv, one per line:
# Print out the OS platform you're using:
# Print out the version of Python you're using:
# See the docs for the OS module: https://docs.python.org/3.7/library/os.html
# Print the current process ID
# Print the current working directory (cwd):
# Print out your machine's login name

label_list = ["OS Platform", "Python Version",
              "Process ID", "Current Directory", "Login ID"]
value_list = [sys.platform, sys.version,
              os.getpid(), os.getcwd(), os.getlogin()]


def print_list_box(title, labels, width, values):
    print("\n|" + title.center(width, "-") + "|" + "\r")
    for index, value in enumerate(values):
        label = labels[index] if isinstance(labels, list) else labels
        stout = "{}: {}".format(label, value).ljust(width-1, ' ')
        print("| " + stout + "|" + "\r")
    print("|" + "-"*width + "|\n")


print_list_box("Command Line Arguments", "Argument", 40, sys.argv)
print_list_box("System Information", label_list, 120, value_list)
