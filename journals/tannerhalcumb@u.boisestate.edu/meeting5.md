# Meeting 5

- Attendance: Everyone present

With a working build system established, we needed to take the next step and provide testing. We
implemented PyTest to check the initialization of our tkinter gui. Ultimately, we need to be thinking
about how we can accomplish the Continuous Integration lab. With GitHub actions not having our precise
OS in Raspbian, we will have to get creative. Some initial thoughts we shared included having our 
embedded code partitioned from the rest of our gui work. This way we can compartmentalize our 
continuous integration and isolate hardware tests if necessary. Another component to this process will
be compiling our Python script into byte code. While import statements implicitly create .pyc files, they
do not carry out this process for the script itself. We will need to use something like the library I found at https://www.geeksforgeeks.org/generate-byte-code-file-python/ . 

Tasks for the week:
- Research the best option for Continuous Integration
- Implement a GitHub Action that will work for us 
