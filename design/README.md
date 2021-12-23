# Design Phase 

## Individual CAD Models
After working through our planning and concept generation phase, we pivoted towards actual CAD design and condensing our ideas down to a few to present to our sponsors. We came up with an attachable arm that translates through an aisle, a stand-alone vending machine, a wire-hanging gondola system, and an XZ Plotter attached to the aisle. [Here is the link to the presentation.](https://docs.google.com/presentation/d/10bg_C8RxaWk_3B0-rSAKrKcWvw39FXTsYiPgkwq6Xnk/edit?usp=sharing)

### Concept 1: Attachable Arm
![arm](images/arm.png)

The focus of this system is to provide additional assistance to in-aisle shoppers by grabbing and stocking items at different heights of the aisle. The horizontal range of the system can be scaled to span almost the entire aisle, with vertical scaling limited by the joint lengths of the arm and torque ratings of the servo's driving the arm links.

### Concept 2: Vending Machine
![arm](images/vending.png)

This is the idea that we decided to go with, our sponsors really liked this idea as it is a modern spin to a classic system seen almost everywhere. This modular design allows for almost any realized grocery item to fit within the vending machine. Multiple implementation ideas were thrown around, including a gravity system, magazine-style loading system, and various end effectors utilized to make the system work. 

### Concept 3: Wire System
![arm](images/wire.png)

This was a very creative idea utilizing a wire hanging gondola system that could assist in stocking and grabbing items located in higher parts of the aisle. Grocery store employees can use this system to help prevent injuries involving stocking higher parts of shelves and aisles, while customers can use a UI system to grab hard-to-reach grocery items.

### Concept 4: XY Plotter
![arm](images/xy.png)

The XY or XZ Plotter is a mix of the vending machine and the attachable arm system, as you attach this system to an aisle and use the two degrees of freedom to navigate the end-effector to a specified location within an aisle shelf. We did not fully flush out the desired end effector when presenting this design to our sponsor, which most likely caused some level of confusion as to what this system was supposed to do. Regardless, in order to test and build this system at scale, we would require a budget of $1500 to even reach a 3ft x 3ft system, so we quickly scrapped this idea after the sponsor feedback session.

## Finalizing Product Design
![set-z](images/set-z.png)
In order to transition to fabrication and finalized CAD design, our last activity was a Pugh Chart and final ranking poll. We used these systems in tandem to make sure every member of the group was able to provide input and allow for a minimal-bias score of each concept. The Pugh Chart and the ranking poll both showed that the Vending Machine was clearly ahead in terms of ease of implementation and application. After this, we pivoted completely to finalizing our CAD model of the vending machine and pumping out 3D printed parts for the prototype. 

## Initial Prototype

![prototype](images/prototype.jpg)

The initial design of the XY Plotter used for our vending machine. 

For the first prototype, we focused on getting the XY Plotter system to work with manual and automated modes. The manual mode would utilize two joysticks to drive the linear actuators together to perform a representative movement. The automated mode would keep track of total number of steps in any direction that the steppers have rotated since initialization and navigate towards a specified location. We had some tolerancing issues on some fits, but we had enough time to iterate, reprint, and test new versions of our motor mounts. The next focus was to build the linear actuator mount and test the system. 

## Further Testing and Iteration
![final](images/final.jpg)

Final View of our system

For the final stretch of our project we focused on iterating the linear actuator sub-system, building out the cube and shelves, as well as securing everything to a wood base. I transitioned to working on the code and electronics interfaces, which can be found [here](https://github.com/drybell/Senior_Design#code--electronics).

## Addendum

![parts](images/parts.jpg)
A teardown view of most of the parts utilized in our demo-day build for the vending machine.

## Engineering Drawings
Below is a gallery of engineering drawings done for almost every single designed and 3D-printed or laser cut model used within our final system.

![d1](images/drawings/1inPretty45DegreeMount.JPG)
![d2](images/drawings/1inTSlotFeet.JPG)
![d3](images/drawings/20mmTSlotFeet.JPG)
![d4](images/drawings/BearingHolder.JPG)
![d5](images/drawings/BinStopperv2.JPG)
![d5](images/drawings/BottomMotorMount.JPG)
![d5](images/drawings/ExtraClamp.JPG)
![d5](images/drawings/LinearActuatorMount.JPG)
![d5](images/drawings/Pretty45DegreeMount1in.JPG)
![d5](images/drawings/ScrewAssemblyMotorMount.JPG)
![d5](images/drawings/ServoMountVX4.JPG)
![d5](images/drawings/ShelfAngledMount.JPG)
![d5](images/drawings/ShelfBracket.JPG)
![d5](images/drawings/TShapedFixture.JPG)
![d5](images/drawings/TSlotFixture.JPG)
![d5](images/drawings/bin_bottomv4.JPG)
![d5](images/drawings/topRightv3.JPG)

## Bill Of Materials
*(View BOM.pdf or BOM.xlsx for more details)*

![BOM](images/BOM.png)

After finalizing our design, we constructed a bill of materials in order to track parts and manage our $400 budget. This is the full tracked list of parts ordered from a variety of vendors. 