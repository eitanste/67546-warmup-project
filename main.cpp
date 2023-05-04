#include <Arduino.h>

int enA = 9;
int in1 = 8;
int in2 = 3;

// // Forward Motor connections
// int enA = 9;
// int in1 = 8;
// int in2 = 7;

// Setup for HC-SR04
// defines pins numbers
const int trigPinFront = 11;
const int echoPinFront = 10;
const int trigPinBack = 13;
const int echoPinBack = 12;

// defines variables
int rotDirection = 0;
int drivingSpeed = 45;
int dist_trash_hold = 60;

#define FRONT 1
#define BACK 0
#define STOP -1

void setup() {
    // Set all the motor control pins to outputs
    pinMode(enA, OUTPUT);

    // 	pinMode(enB, OUTPUT);
    pinMode(in1, OUTPUT);
    pinMode(in2, OUTPUT);
    digitalWrite(in1, LOW);
    digitalWrite(in2, LOW);

    pinMode(trigPinFront, OUTPUT);  // Sets the  trigPinFront as an Output
    pinMode(echoPinFront, INPUT);   // Sets the echoPinFront as an Input
    pinMode(trigPinBack, OUTPUT);   // Sets the  trigPinFront as an Output
    pinMode(echoPinBack, INPUT);    // Sets the echoPinFront as an Input
    Serial.begin(9600);             // Starts the serial communication
}

void adjast_drive(int rotDirection) {
    switch (rotDirection) {
        case FRONT:
            Serial.print("set to FRONT, ");
            // digitalWrite(motorPin, HIGH);
            // Turn on motor A
            digitalWrite(in1, HIGH);
            digitalWrite(in2, LOW);
            analogWrite(enA, drivingSpeed);
            delay(200);
            break;
        case BACK:
            Serial.print("set to BACK, ");
            // digitalWrite(motorPin, HIGH);  // change to drive back
            digitalWrite(in1, LOW);
            digitalWrite(in2, HIGH);
            analogWrite(enA, drivingSpeed);
            delay(200);
            break;

        case STOP:
            Serial.print("set to STOP, ");
            // digitalWrite(motorPin, LOW);
            analogWrite(enA, 0);
            delay(200);
            break;

        default:
            break;
    }
}

int mesure_distence(int sensoreTrig, int sensoreEcho) {
    digitalWrite(sensoreTrig, LOW);
    delayMicroseconds(2);
    // Sets the trigPin on HIGH state for 10 micro seconds
    digitalWrite(sensoreTrig, HIGH);
    delayMicroseconds(10);
    digitalWrite(sensoreTrig, LOW);
    // Reads the echoPinFront, returns the sound wave travel time in
    // microseconds
    long duration = pulseIn(sensoreEcho, HIGH);
    // Calculating the distance
    int distance = duration * 0.034 / 2;
    return distance;
}

void loop() {
    // front
    int distance_front = mesure_distence(trigPinFront, echoPinFront);
    Serial.print("Distance_front: ");
    Serial.println(distance_front);

    while (distance_front > dist_trash_hold) {
        Serial.println("going forwad");
        rotDirection = FRONT;
        adjast_drive(rotDirection);
        distance_front = mesure_distence(trigPinFront, echoPinFront);
        Serial.print("Distance_front: ");
        Serial.println(distance_front);
        // delay(1000);
    }

    Serial.println("stoping");
    rotDirection = STOP;
    adjast_drive(rotDirection);
    delay(500);

    // back
    int distance_back = mesure_distence(trigPinBack, echoPinBack);
    rotDirection = BACK;
    adjast_drive(rotDirection);
    while (distance_back > 20) {
    // while (distance_back > dist_trash_hold) {
        Serial.println("going backwards");
        rotDirection = BACK;
        adjast_drive(rotDirection);
        distance_back = mesure_distence(trigPinBack, echoPinBack);

        Serial.print(", Distance_back: ");
        Serial.println(distance_back);
        // delay(1000);
    }

    Serial.println("stoping");
    rotDirection = STOP;
    adjast_drive(rotDirection);
    delay(500);

    // else if (distance_front < dist_trash_hold &&
    //            distance_back > dist_trash_hold) {
    //     rotDirection = BACK;
    // }
}
