# CFD_software
##INTERFACE FOR CFD MODELLING

##TABLE OF CONTENTS
* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)
* [Run](#run)
* [Issue](#issue)

## General info
Computational fluid dynamics (CFD) is a branch of fluid mechanics that uses numerical analysis and data structures to analyze and solve problems that involve fluid flows. Our project aims to aggregate the existing open source softwares and unify it to one by giving the abstraction of a GUI.

## Technologies
* Python version 3.5+
* tkinter version 8.6
* logging
* os
* time
* errno

##Setup
The following software will be needed:
     
* Gmsh 
  * sudo apt-get install gmsh
* Fluidity
  * sudo apt-add-repository -y ppa:fluidity-core/ppa
  * sudo apt-get update
  * sudo apt-get -y install fluidity
* Paraview
  * sudo apt-get install paraview
* openFOAM
  * sudo apt-get install openfoam

##Run
Double Click on the application launcher.

##Issue
* If fluidity installation doesn't work properly, try executing without ppa command.
* Multi-threads and aren't enabled yet, so multiple stages won't run simultaneously.
* If application doesn't launch properly, run `chmod u+x pr.py` after opening terminal inside the github repository.

