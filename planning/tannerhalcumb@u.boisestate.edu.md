# Tanner Halcumb

### Raspberry Pi Security Camera Motion Sensor

## User Story

As a user of the raspberry pi security camera motion sensor, I want the motion sensor to detect
a human presence, so that the camera can record the instance and document for users to view in 
our tkinter GUI.

## Tasks

1. I will research optimal GPIO pin setup to connect motion sensor, essentially a smoke test
with focus on raspberry pi motion detection. 
2. I will align the motion sensor to collect motion and turn off after instance is recorded.
3. I will configure motion sensor to detect movement during moments of minimal lighting.
4. I will configure motion sensor to detect movement during moments of strong light exposure.
5. I will document and test the setup of our selected raspberry pi motion sensor.

### Time estimation method

Considering the unantipcated hurdles, we have allocated extra time and imagine between 3 and
4 hours of work for each of these tasks. Accumlative, between 15 and 20 hours of work with anticipation
of new tasks to surface.

## Definition of Done

- Task 1 DOD - I will know that I am done by having a set of unit/system tests that
  exercise my Model class. I can run my tests with the test.sh script and see the results
  of the tests. My tests are ran on every commit with the results shown at https://github.com/example
- Task 1, optimal GPIO pin setup, will be complete by comfirming the motion sensor is plugged in and establishes a non-fatal connection. At this point, the raspberry pi can confirm through our test.sh script that communication between hardware is active.
- Task 2 will be complete when the presence of a human is detectable, then the instance is recorded and the motion sensor turns off.
- Task 3 will be complete when the presence of a human is detectable in the absence of light, then the instance is recorded and the motion sensor turns off.
- Task 4 will be complete when the presence of a human is detectable in the presence of profound light, then the instance is recorded and the motion sensor turns off.
- Task 5 will be complete when the documentation for the motion sensor design is comprehensive and allows someone with all the components to plug in, download our instructions, and properly test the detection of motion through the raspberry pi. 
