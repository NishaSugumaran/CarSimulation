![image](https://github.com/NishaSugumaran/CarSimulation/assets/158027322/00815900-c3ad-42f9-9630-4a1f9b5d1c5e)![scenario1](https://github.com/NishaSugumaran/CarSimulation/assets/158027322/b1079e47-4d24-4a7c-ac8e-51b0e350678b)# CarSimulation
1.	Project overview:

This project is about autonomous car driving simulation, with the aim of competing Tesla. The simulation program is designed to work with a rectangular field specified by width and height. The bottom left co-ordinate of the field is at position (0,0), and the top right position is denoted by (width, height).

For example: a field with dimension 10 X 10 would have its upper right co-ordinates is at position (9,9).

The user is able to add one or more cars to the field, each with unique name, starting position, and direction they are facing. For instance, a car named “A” may be placed at position (1,2) and facing North. A list of commands can be issued to each car, which can be one or three commands:

•	L: rotates the car by 90 degrees to the left
•	R: rotates the car by 90 degrees to the right
•	F: moves forward by 1 grid point
•	Only N, S, E, W will be accepted as valid directions.


If the car moves beyond the boundary of the field, the command is ignored, and the car stays in its current position. 
For example: if a car at position (0,0) is facing south and receives an F command, the command will be ignored as it would take the car beyond the boundary of the field

2.	Pre-requisites:

This code will be executed on Python3

Steps to Execute:
1.	Execute autocarmovement.py file
      a.	python3 autocarmovement.py
2.	Execute pytest using below command
      a.	python3 -m pytest --cov -v test_autocarmovement.py

3.	User Guide:

On executing ‘autocarmovement.py’ module, terminal prompts for boundary values where the 

•	User has to enter boundary values in height, width format (10,10)

•	User has to select option 1 to add any car details. 
        o	Please choose from the following options:
              [1] Add a car to field
              [2] Run Simulation

•	To add a car user has to mention the following
        o	Carname <A>
        o	Current position direction <x y dir>
        o	Command to simulate <FFRL>

•	To execute simulation user has to select option 2

Note: User can add any number of cars details. 

4.	Application design and Solution:

      1.	Created class ‘Car’ to hold each car details

      2.	Implemented class function ‘move’ to execute autonomous simulation

      3.	Developed unit test cases in PyTest for unit testing and code coverage purpose

