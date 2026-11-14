# LTASoftware
Software for LTA grpup final project Intro to Engineering Lab at Kent State University

The program helps us keep track of vehicle components, calculate mass and cost, and save different versions of our design as we make changes.

### Features

* Component Management: Add, edit, remove, and view vehicle components.
* Mass Calculations: Calculate total vehicle mass and competition-regulated mass.
* Budget Tracking: Track component costs and remaining budget.
* Revision History: Save previous versions of our design so we can reference them later.
* JSON Storage: Automatically save vehicle data between sessions.

### Project Limits

Requirement	Limit
Maximum Mass	800 g (excluding battery and balloon)
Maximum Budget	900 Gils
Propulsion	3 propellers

### Project Files

LTASoftware-main/
- main.py          # Main menu and program startup
- vehicle.py       # Components, mass, cost, revisions
- physics.py       # Flight calculations 
- testing.py       # Testing and results
- data/
  - vehicle.json
  - flight_tests.csv
- README.md

### Running the Program

Requires Python 3+

Run: `python main.py`

Vehicle data is saved to data/vehicle.json. Test results saved to data/flight_tests.csv for easy analysis.

### Current Progress

* [x]	Component registration and editing
* [x]	Component removal
* [x]	Mass and budget calculations
* [x]	JSON saving and loading
* [x]	Revision tracking
* [x]	Main menu integration and testing
* [x]	Flight physics calculations
* [x]	Testing and analysis functions
