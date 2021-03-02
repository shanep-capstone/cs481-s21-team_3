#!/bin/bash
#########################################
# Driver script for unit testing.
#
# Our current tests exit with 0 for a
# succesful test, or a 1 for an
# unsuccesful test.
#
# Usage:
#   $ make check
# 
# Note:
#   The tkinter gui tests still
#   currently require the user to close
#   out the graphical windows by manually
#   clicking on them. Updates to come!
#########################################


# Tests the initializaion of 
# the tkinter gui framework.
echo "Running test_gui_init.py"
echo "exit code: "
python3 tests/test_gui_init.py
echo $?
echo ""

# Tests the main method of the
# tkinter hello world program,
echo "Running test_tkinter.py"
echo "exit code: "
python3 tests/test_tkinter.py
echo $?
echo ""


# More testing to come once we 
# get all of our hardware dialed
# in a bit more.

