import pytest
import sys
sys.path.append("./src")
import hello_tk_world as gui
#########################################
# Quick test for the main portion of
# our tkinter gui framework.
#
# Successful test exits with 0
# Unsuccessful test exits with 1
#
# Usage:
#   $ make check
#########################################

# Gui main testing function.
def test_gui_main():
    try:
        gui.test_exit()
        assert True # 0
    except:
        assert False # 1

test_gui_main()
