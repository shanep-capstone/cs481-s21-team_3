.PHONY: help prepare-dev build clean run

.DEFAULT: help
help:
	@echo "make prepare-dev"
	@echo "		Installs missing dependencies required for project"
	@echo "make run"
	@echo "		Run the program"
	@echo "make build"
	@echo "		Builds bytecode .pyc files of program"
	@echo "make clean"
	@echo "		Removes bytecode .pyc files"

prepare-dev:
	sudo apt-get -y install python-picamera python3-picamera
	sudo apt-get -y install python3-tk
	pip3 install RPi.GPIO
	pip3 install -U pytest

build:
	@sh build.sh

clean:
	@sh clean.sh

run:
	python3 ./src/hello_tk_world.py

# check-ci:
# 	@python3 tests/test_ci.py

check:
	@echo "Starting tests..."
	@echo ""
	@pytest tests/test_ci.py
	# @sh test.sh
	# @pytest
