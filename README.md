# CS481 - Senior Design Project

![Continous Integration](https://github.com/shanep-capstone/cs481-s21-team_3/actions/workflows/ci.yml/badge.svg)  
  

## Project Epic

### _Raspberry Pi 3 - Front Door Security_
  
The main intent of our project is to utilize a Raspberry Pi 3 in order to monitor front door visitors. This will be accomplished by using a motion sensor to detect someone’s presence, which will then trigger a camera to document this occurrence. These instances of someone at the front door will be recorded and sent as web requests to the homeowner. These notifications will have the option of email or text message configuration to alert the homeowner when they are triggered. One of the primary goals for this project is to allow for video recording, but there is wiggle room in stretch goals that will increase the overall functionality of the device beyond its primary function. 
  
On the physical side, we need to secure the necessary hardware pieces. Links have been included as possible options for some of the hardware components. _These include..._

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
   

### _Required Software Overview:_

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
## Tech lab

### _Overview_

Below is the tech that we plan to use for our project. We attempted to plan ahead and consider all the elements our project would use, and we believe that we covered most of the grounds. This list will be updated if something is determined necessary during development or an extra feature is added from the inclusion of a stretch goal. Some of the hardware options were made to keep cost low without sacrificing too much performance.

### _Software_

[Raspberry Pi OS](https://www.raspberrypi.org/documentation/raspbian/): This operating system is the default and most well rounded operating system for the raspberry pi. Although we could have gone with a more generic option such as Ubuntu, Raspberry Pi OS is designed specifically for the pi therefore there are some, albeit minor, performance improvements due to the knowing the hardware configurations during development.

### _Programming Language and Libraries_

[Python 3](https://docs.python.org/3/): The Raspberry Pi OS by default comes with Python 3 installed. Since Python is a well rounded and respected programming language especially within the raspberry pi community, we decided to go with it as our main programming language. Additionally, there is an abundance of libraries already created in Python that we can leverage when communicating with our additional hardware such as the camera and GPIO ports. As a final point, some of our team members have not worked frequently with Python so we determined it would be a great learning experience. 

[picamera](https://picamera.readthedocs.io/en/release-1.13/) Library: The picamera library allows us to leverage the CSI port on the raspberry pi and connect a camera to it for recording video. There are all sorts of baked-in methods for the camera class in this library and our project can utilize these to initialize the camera to record video.

[RPi.GPIO](https://sourceforge.net/p/raspberry-gpio-python/wiki/Home/): The Raspberry-gpio-python Library (RPi.GPIO) module is installed with the Raspberry Pi OS and allows for the use of the GPIO ports on the raspberry pi board. Our project will utilize motion sensors that connect via the GPIO ports to determine when to start filming.

### _Frameworks_

[TkInter](https://wiki.python.org/moin/TkInter) Framework: TkInter is a Python GUI Framework that allows for the easy creation of GUI interfaces. It is one of the most common Python Interface builder tools that should give us enough utility for our goals in this project.

Our hello world program [hello_tk_world.py](https://github.com/shanep-capstone/cs481-s21-team_3/blob/master/src/hello_tk_world.py) demonstrates a quick and simple use of the framework. The program can be found at src/hello_tk_world.py.  

### _Hardware_

[Raspberry Pi 3 B](https://www.amazon.com/Raspberry-Pi-MS-004-00000024-Model-Board/dp/B01LPLPBS8/ref=sr_1_4?dchild=1&keywords=raspberry+pi+3&qid=1612218605&s=electronics&sr=1-4): Previous generation Raspberry Pi that has CSI and GPIO connectors along with USB and HDMI. ARM quad core processor and 1GB ram more than enough power for this project.

[Stemedu HC-SR501](https://www.amazon.com/gp/product/B07KBWVJMP/ref=ppx_yo_dt_b_asin_title_o07_s00?ie=UTF8&psc=1): Infrared IR motion sensor module allows for motion detection connection through GPIO ports.

[Smraza OV5647 Camera Module](https://www.amazon.com/Camera-Module-Raspberry-Supports-Compatible/dp/B073183KYK/ref=sr_1_4?dchild=1&keywords=raspberry+pi+3+camera&qid=1612218684&s=electronics&sr=1-4): CSI connector camera module that allows for 5MP 1080p video capture with IR lights for adequate night time video recording. 

[SanDisk 32GB microSD SDSQUA4-032G-GN6MA](https://www.amazon.com/SanDisk-Ultra-microSDHC-Memory-Adapter/dp/B08GY9NYRM/ref=sr_1_3?dchild=1&keywords=micro+sd+card+32gb&qid=1612218327&sr=8-3): Micro SD that will act as the hard drive for the Raspberry Pi. Enough storage for holding multiple video files with sufficient write speed for 1080p video.


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
*April 20<sup>nd</sup> Tuesday 1:55-2:05*
