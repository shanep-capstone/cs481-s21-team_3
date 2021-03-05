# Meeting 6

- Attendance: Everyone present

This week I spent the majority of my time researching as much as I could about github actions and
working on our project's implementation of the action for CI. Getting the build process to work
for the bytecode was not too difficult but where I struggled was getting the appopriate libraries
installed that allowed for running the compile script and unit tests. Through trial and error, I 
determined that the picamera was throwing issues since our VM that github actions used was not 
raspberry pi hardware which is checked during the install. Unfortunatly, there is no solution as of
yet but luckly this does not affect our project building or unit testing. After CI was implemented
and was checking out with each commit, Ryan was able to get the badge working on the readme which
finished up the (rough) CI section of our project.

My task for this week:

- Create planning around video camera implementation