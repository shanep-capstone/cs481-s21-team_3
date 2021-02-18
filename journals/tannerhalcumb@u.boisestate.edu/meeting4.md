# Meeting 4

- Attendance: Everyone present

After last week establishing a "hello world" program, this week we focused on the build system. We discussed
our options as far as how to handle a build and clean script in Python. Part of the problem is how Python acts
as a programming language. It is unique in that it compiles down to bytecode, in which it is then implicitly 
interpreted by a virtual machine. We landed on a makefile for the mean time that allows us to run our tkinter
library efforts. Looking towards our testing lab, we are considering PyTest. It seems straight forward, and I
intend to step through some of the initial usage steps to get our project aligned for tests down the road. In
addition, I will begin testing the camera and motion sensors to get a feel for their capabilities. 

Tasks for the week:
- Look into PyTest and implement
- Test camera/motion sensors 
