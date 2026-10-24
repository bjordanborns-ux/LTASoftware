# LTASoftware
LSFA — Lighter Than Air Systems & Flight Analysis

LSFA is a Python program we’re developing for our Intro to Engineering lighter-than-air vehicle project, LTA McQueen.

The program helps us keep track of vehicle components, calculate mass and cost, and save different versions of our design as we make changes.

Features

* Component Management: Add, edit, remove, and view vehicle components.
* Mass Calculations: Calculate total vehicle mass and competition-regulated mass.
* Budget Tracking: Track component costs and remaining budget.
* Revision History: Save previous versions of our design so we can reference them later.
* JSON Storage: Automatically save vehicle data between sessions.

Project Limits

Requirement	Limit
Maximum Mass	800 g (excluding battery and balloon)
Maximum Budget	900 Gils
Propulsion	3 propellers

Project Files

LSFA/
├── main.py          # Main menu and program startup
├── vehicle.py       # Components, mass, cost, revisions
├── physics.py       # Flight calculations (planned)
├── testing.py       # Testing and results (planned)
├── data/
│   ├── vehicle.json
│   └── revisions/
└── README.md

Running the Program

Requires Python 3. No additional libraries are needed for the current vehicle management functions.

Once the main menu is complete, run:

python main.py

Vehicle data is saved to data/vehicle.json. Finalized revisions are stored separately in data/revisions/.

Current Progress

* [x]	Component registration and editing
* [x]	Component removal
* [x]	Mass and budget calculations
* [x]	JSON saving and loading
* [x]	Revision tracking
* [ ]	Main menu integration and testing
* [ ]	Flight physics calculations
* [ ]	Testing and analysis functions

Notes

The program is still in development. Calculations are based on the component information we enter, so measurements and costs need to be kept up to date.

The goal is to have one place where we can manage our design and check that LTA McQueen stays within the project requirements.
