# Kyle Epperson

### Raspberry Pi Security Camera Funcationality  
&nbsp;   

## User Story

As a user of the raspberry pi security camera I need to be able to utilize
the camera to record and store videos so that the device can be used as a
security camera.

## Tasks

1. I will construct the logic to determine paramaters of video recording such as recording time based off GUI values.
2. I will add the option based of GUI info for file storage location.
3. I will setup the saving process of video files after they are created.
4. I will connect the camera to the motion sensor interface to recieve recording start signals.
5. I will create an interface for the GUI to use for viewing current camera footage.


### Time estimation method

As we are still learning working with the hardware and getting used to Python, I estimate that each task
will take between 3 to 5 hours to design, code, and test. There is the possibility that any given task
could require more underlying work so my total estimation for work time is anywhere between 15 to 30 hours.
This estimate considered by own ability to complete these tasks and time needed to complete research for implementation.

## Definition of Done

- Task 1 DOD - Task 1 will be complete when the camera is able to read GUI values such as recording time and modify the recording paramaters to match those constraints (ie. if specified to record for 30 seconds, the camera will record for 30 seconds). Additionally, there will be atleast 1 test for any non-hardware reliant methods that I create for this task. 
- Task 2 DOD - Task 2 will be complete when the camera interface will have the ability to change storage location based off user input. Testing for this method does not require hardware therefore will be present. 
- Task 3 DOD - Task 3 will be complete when the video file is saved to a location specified by the user. A test will be created that can run locally on the pi to ensure funcationality.
- Task 4 DOD - Task 4 will be complete when the camera is triggered by signals sent from the motion sensor, starting the recording process.
- Task 5 DOD - Task 5 will be complete when the video signal is available through the camera interface so it can be used in the GUI.
