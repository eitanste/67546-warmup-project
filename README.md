# ♨️ Warmup Project - Prototype
### (Deadline 20.04.2023 14:00)

Now you finally get to build an app or a device that does something cool with your data!

**Select one from the 3 following options below.**

**IMPORTANT:** You must upload your code to the repo by the deadline (April 20th at 14:00), however, it does not have to be the final version of your prototype. On the 20th we will meet you for an in-class workshop session to help you solve problems and polish off your projects.

## 👨‍💻 Option-1: Create a WebApp Backend
### Motivation:
Many projects make use of web technologies. This allows building apps that interact with an end user which can provide various inputs to the app. The app then makes a decision and presents suggestions/solutions based on the input (e.g. Show relevant recipes based on pictures of things in your fridge). In this assignment, you will focus on building a web application for your project.
### Mission:
You are provided with a frontend template that you can drag any type of file to, and upload it to the server. Your job is to build the backend server in Flask that accepts this file, validates it, tags it in a database (e.g. a CSV file), and sends a response to the frontend (confirmation or an error). The user should also be able to view the files and the database on the server via the frontend.
The backend should: 
* Check the validity of the data, it should check that the file is not empty, that the file type is as expected and it should check that the file is not above 5Mb.
* Generate a CSV file which the user can download after he finished uploading the file. The CSV should have database information such as the size of each file, the type of each file, the time it was created and so on.
* Lastly we want you to compress the files that the user uploaded. 
### Recommended resources:
* https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-iii-web-forms 
* https://blog.miguelgrinberg.com/post/handling-file-uploads-with-flask 
## 📊 Option-2: Visualize Insights from Your Data
### Motivation:
When building ML and other data-based models, it is often required to be able to visualize the data one is working with. This assignment can represent an intermediate step in the overall problem you set to solve in the ideation session or an independent visualization challenge that is somehow related to your data.
### Mission:
Preprocess the data you collected in a meaningful way and visualize the insights using StreamLit. The idea is to build a tool for you to inspect the data and help you research the problem you are trying to solve. You are provided with a template that uses StreamLit to visualize data, and your mission is to develop the following operator and aggregation functions:
* Operator function - operates on an individual sample and displays an interesting property of the sample.
* Aggregation function - operates on all the uploaded samples, and provides insight about the selected samples.
* Total aggregation function - operates on all the samples in the directory, and provides insight about the dataset as a whole.

The provided templates are designated for uploading audio/image data but can be modified to your liking. The current setting assumes that you have preprocessed your data and stored non-trivial "meta-info" to an individual .txt file, corresponding to each sample in your dataset, in a designated "meta-info" directory. This directory should be pointed to when calling the plot functions in the current setting.
### Recommended Resources:
* Checkout the Streamlit documentation: https://docs.streamlit.io/
* In a nutshell, you can use any plotting function from your favorite python library (matplotlib, plotly,...) and display the figure using a function from the Streamlit library.
* You can also build an interface to interact with your data and [loads of other cool things](https://streamlit.io/gallery).
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

