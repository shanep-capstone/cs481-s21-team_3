# CS481 - Senior Design Project

TODO:[CI Lab](https://shanep.github.io/capstone/labs/ci/)

## Project Epic
&nbsp;  
*What we are building:*  
***Raspberry Pi 3 - Front Door Security*** 
&nbsp;  

The main intent of our project is to utilize a Raspberry Pi 3 in order to monitor front door visitors. This will be accomplished by using a motion sensor to detect someone’s presence, which will then trigger a camera to document this occurrence. These instances of someone at the front door will be recorded and sent as web requests to the homeowner. These notifications will have the option of email or text message configuration to alert the homeowner when they are triggered. One of the primary goals for this project is to allow for video recording, but there is wiggle room in stretch goals that will increase the overall functionality of the device beyond its primary function. 
  
On the physical side, we need to secure the necessary hardware pieces. Links have been included as possible options for some of the hardware components. **These include...**

_Required Hardware Overview:_
* [Raspberry Pi 3](https://www.amazon.com/Raspberry-Pi-MS-004-00000024-Model-Board/dp/B01LPLPBS8/ref=sr_1_4?dchild=1&keywords=raspberry+pi+3&qid=1612218605&s=electronics&sr=1-4)  
* [Motion Sensor(s)](https://www.amazon.com/gp/product/B07KBWVJMP/ref=ppx_yo_dt_b_asin_title_o07_s00?ie=UTF8&psc=1)  
* [Raspberry Pi Camera](https://www.amazon.com/Camera-Module-Raspberry-Supports-Compatible/dp/B073183KYK/ref=sr_1_4?dchild=1&keywords=raspberry+pi+3+camera&qid=1612218684&s=electronics&sr=1-4)
* [Micro SD card(8GB minimum)](https://www.amazon.com/SanDisk-Ultra-microSDHC-Memory-Adapter/dp/B08GY9NYRM/ref=sr_1_3?dchild=1&keywords=micro+sd+card+32gb&qid=1612218327&sr=8-3)  
* [Mobile Battery pack(optional: for extra portability)](https://www.amazon.com/gp/product/B07YCR7FR9/ref=ppx_yo_dt_b_asin_title_o00_s00?ie=UTF8&psc=1)  

_Strech Goal Hardware:_  
* Raspi Button
* Breadboard(possibly needed to integrate the button)
* Small Speaker
* Microphone
  

Once the hardware is acquired, then it’ll be necessary to make individual connections to our program, and test their functionality. Python, specifically [Python 3.6 or higher](https://www.python.org/downloads/), will be required for making the individual connections as well as testing each component's functionality. 
  

_Required Software Overview:_  
At a lower level, Python will be used to implement the logic behind these processes. The Pi Camera package is a solid module for us to start, as it has plenty of options for retrieving video clips and a robust, well supported library. The remaining elements connected to the raspberry pi can easily be interfaced through Python as well and have their inputs fed into our program. For example, the motion sensors can be connected to the raspberry pi by using python’s general purpose input/output(GPIO) pins. Plus, as a reference point the raspberry pi offers a terminal tool called [pinout](https://www.raspberrypi.org/documentation/usage/gpio/). Pinout provides the pi’s hardware layout schematic for the GPIO pins. Which will be needed to make sure the required sensor cables are connected correctly.

A stretch goal would be to add a button to the device, providing doorbell functionality. As an additional stretch goal, implementing some sort of user interface that allows the user to determine the functionality of the device (such as video save locations for example) would help make the device more robust. Another stretch goal would be to implement a microphone to allow for audio capture in addition to the video stream for added security. 

The operating system to power our project will be [Raspbian](https://www.raspbian.org/). Raspbian is a free linux distro that is optimized for the Raspberry Pi. Additionally, Rasbian comes preloaded python installed and ready to go. Therefore, at which point, we should simply need to make sure we have the necessary python packages installed. For example, some of the required python modules will be the [Pi Camera module](https://picamera.readthedocs.io/en/release-1.13/install.html) and the [GPIO module](https://pypi.org/project/RPi.GPIO/). Required python modules will act as our glue between hardware and software. **These include...**

&nbsp;  
Assuming Rasbian and Python 3 are already installed make sure the following software packages are also...
&nbsp;  
*Check if Pi Camera module is installed:*
```sh
$ python3 -c "import picamera"
```  
*Install Pi Camera module:*
```sh
$ sudo apt update
$ sudo apt -y install python-picamera python3-picamera
$ sudo apt update && sudo apt -y upgrade
```  
*Check if GPIO module is installed:*
```sh
python3 -c "import RPi.GPIO"
```
*Install GPIO module:*
```sh
$ pip3 install RPi.GPIO
```

### Feedback from Shane

Very nice project idea. The cool part about this project is with the raspberry pi this can stand alone and doesn’t need a subscription like the ring or nest doorbell camera. In fact you can host the webserver right on the pie that is accessible on your local network. I think this is a perfect fit for Senior design!

I am excited to see the finished project! 

  
&nbsp;  
### Tech lab

TODO:[Tech Lab](https://shanep.github.io/capstone/labs/tech/)

## Planning Lab

TODO:[Planning Lab](https://shanep.github.io/capstone/labs/planning/)

<!--
Left the markdown below as a comment to be a reference point for when we hyperlink our plans.  

- [Jane's Plan](planning/janedoe@u.boisestate.edu.md) 
-->
- Kyle Epperson's Plan
- Ryan Thompson's Plan
- Tanner Halcumb's Plan  

&nbsp;  
&nbsp;         
*Presentation Date:*  
*April 22<sup>nd</sup> Thursday 1:40-1:55*
