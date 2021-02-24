import pytest
import sys
sys.path.append("./src")
import hello_tk_world as gui
#########################################
# Quick test for the initializaion of 
# the tkinter gui framework.
#
# Successful test exits with 0
# Unsuccessful test exits with 1
#
# Usage:
#   $ make check
#########################################

# Gui init testing function
def test_gui_init():
    try:
        gui.init()
        assert True # 0
    except:
        assert False # 1

test_gui_init()