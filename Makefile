.PHONY: help prepare-dev run

.DEFAULT: help
help:
	@echo "make prepare-dev"
	@echo "		Installs missing dependencies required for project"
	@echo "make run"
	@echo "		Run the program"

prepare-dev:
	sudo apt-get -y install python-picamera python3-picamera
	sudo apt-get -y install python3-tk
	pip3 install RPi.GPIO

run:
	python3 ./src/hello_tk_world.py