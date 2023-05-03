# ♨️ Warmup Project - Automotive Toy Car with Obstacle Avoidance

## Itroduction
This project implements an automotive toy car that can avoid obstacles using two HC-SR04 sonar sensors, an Arduino, and an L298N motor driver. The car is equipped with one sensor mounted on the front and one on the back. The logic of the project is as follows:

Initially, the car is set to move forward. As long as the distance of the front ultrasonic sensor is higher than a threshold, the car will continue in the same direction. However, the moment the sensor reads a value lower than the threshold, it changes direction until the back ultrasonic sensor is sensing an obstacle below the threshold distance. At this point, the car should turn back and go forward again, repeating this logic.

## Prerequisites
To use this project, you will need:

- An Arduino board (tested on Arduino Uno)
- Two HC-SR04 ultrasonic sensors
- An L298N motor driver
- A DC motor
- Jumper wires
- A toy car
- A breadboard
- A power source for the DC motor
- Arduino IDE installed on your computer


## Installation
To install the project, follow these steps:

1. Connect the L298N motor driver to the breadboard and connect the DC motor to the motor driver using jumper wires.
2. Connect the Arduino board to your computer.
3. Connect the HC-SR04 ultrasonic sensors to the breadboard and connect the breadboard to the Arduino board using jumper wires.
4. Connect the motor driver to the Arduino board using jumper wires.
5. Attach the ultrasonic sensors to the front and back of the toy car using adhesive.
6. Download and open the Arduino IDE on your computer.
7. Copy the code provided in this project and upload it to your Arduino board using the Arduino IDE.

One can clone this reposetory using:
```bash
git clone https://github.com/eitanste/67546-warmup-project.git
```


## Usage
To run the project, follow these steps:

1. Power the DC motor and the Arduino board.
2. Place the toy car on a flat surface.
3. Make sure the HC-SR04 ultrasonic sensors are positioned properly on the front and back of the car.
4. Observe the car moving forward.
5. Once an obstacle is detected by the front sensor, the car will turn until the back sensor detects an obstacle below the threshold distance.
6. The car will then turn back and move forward again, repeating this logic.

*Note: If the car is not responding to the sensors, check the connections between the sensors, breadboard, and Arduino board. You can also adjust the threshold distance by changing the value of the variable "dist_trash_hold" in the code.


## The instructions for this project were:
## 🤖 Option-3: Build a Physical I/O Device
### Motivation:
Many projects require physical solutions that can manipulate the real world and must interact with users outside a screen. This assignment can represent such a project which has more interesting outputs and inputs beyond a mouse, keyboard and monitor.
### Mission:
Build a circuit which has at least one sensor (e.g. microphone, light sensor) and at least one actuator (e.g. servo motor, LED lights).

The sensor should be able to collect/receive data as input. The Actuator needs to manipulate something in the real world as response to that input. For example, this can be some feedback to the user or a chain-reaction / automata that is triggered by the input to the system. You can use the template from the Arduino lesson or one of the many examples in the Arduino IDE.
### Recommended Resources:
* https://www.arduino.cc/en/Guide 
* https://drive.google.com/file/d/1pf5l1svseRHQln9ttoO1wiMw1DxOB0Jk/view?usp=sharing 
* https://mars1980.github.io/resources/making_things_move.pdf 

