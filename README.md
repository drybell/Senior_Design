# FALL 2021 Senior Design Project 
## **EasyShop!**
### **Team Members:** Daniel Ryaboshapka, Taylor Korte, Rebecca Shen, Stephanie Bentley
### Amazon Robotics Sponsored Project
## **Problem Statement:** *Reduce the difficulty of stocking and picking grocery items in an aisle*

![demo_day](images/demodaygroupphoto.jpg)

# Table Of Contents
0. [Project Description](#project-description)
1. [Page Layout](#page-layout)
2. [Planning Phase](#check-out-the-planning-phase)
3. [Design Phase](#check-out-the-design-phase)
4. [Code & Electronics](#code-&-electronics)
5. [Demo](#demo)

# Project Description
For our Senior Design class, we set out attempting to assist in the general automation of the grocery shopping experience. Through careful design iteration and concept generation, we found a solution that we could implement in a month in order to generate a MVP during a demo presentation on Monday, December 6th. Our product, EasyShop, is a fully modular and easily scale-able vending machine that can hold various fresh produce and healthy options inside or outside of a grocery store. 

# Page Layout
This repository is split up into two sections: code and team documents. The code exists in the root location, with JS, CSS, and images in `static` and HTML in `templates`. The code is split into multiple python scripts, along with a flask server app (within `app.py`). The `planning`, `presentations`, and `design` folders contain seperate README files that explain the inner workings of each file, as well as how the team utilized each file when working on the project. 
## `planning` 
In this folder, there exists `.pdf` and original file-type versions of each document created during our planning phase
## `presentations`
Here lie `.pdf` versions of our presentations presented to our classmates, Amazon sponsors, and instructors
## `design` 
An in-depth commentary on our design phase, how we worked together to create the final product, and the intermediary steps involved during the design process.
## `demo`
Media and commentory during our final presentation and demos on December 6th! 
## `static`
This folder contains three subfolders: `css`, `js`, and `images` which are used within the server to host stylesheets, internal scripts, and images
## `templates`
This holds various `html` files which the server renders
# [Check out the Planning Phase](https://github.com/drybell/Senior_Design/tree/master/planning)
# [Check out the Design Phase](https://github.com/drybell/Senior_Design/tree/master/design)
# Code & Electronics

![home](images/ez-shop.png)

Home Page for the Pi-hosted webpage

![shopping](images/shopping-cart.png)

Shopping Cart View

![checkout](images/checkout.png)

Checkout View
---

### Code Layout
The code is split up in the following scripts:
- `app.py`: the main driver and server code
- `arduino_comm.py`: focuses on the Pi communicating with the Arduino
- `vending.py`: implements a high-level vending machine abstraction
- `pca9685.py`: is a low-level servo hat I2C script for running servos
- `dc_motor.py`: implements low-level GPIO outputs for the L298N motor driver
- `servo.py`: utilizes `pca9685` to send servo angle commands
- `static/css/style.css`: CSS styling for the entire webpage and all routes
- `static/js/home.js`: Frontend script for populating the home page of the server
- `static/js/checkout.js`: Frontend logic for checkout view
- `static/js/shopping_cart.js`: Frontend logic for the shopping cart view

All JS communicates with the server in order to get up-to-date inventory items, costs, etc. The `app.py` script also contains an inventory class that assists in tracking current user inventory and shop inventory, and can be easily modified depending on the vendor's needs. Once the user clicks on checkout, the Pi then sends the necessary commands to the Arduino and other electronics to move the system to the correct location, perform an extension and retraction, and drop off the item(s) to a "conveyor belt".

# Demo

[Here](https://drive.google.com/file/d/1jwLgcZQVQoNJhB84unmDqcdiakTV3B3j/view?usp=sharing) you can view a video of the demo presentation and my thoughts on the semester-long project.
