# Traffic Light Controller (Formal Verification Using Z3)

Project Overview

This project models and verifies a traffic light controller system using the Z3 theorem prover in Python. The goal is to ensure that the traffic light transitions follow a strict sequence and avoid invalid states.

Key Features

State Transitions: Red → Green → Yellow → Red

Safety Rules:

No direct transition from Red to Yellow.

Lights cannot stay in one state indefinitely.

Formal Verification: Uses Z3 to dynamically verify the correctness of transitions.

Requirements

Python 3.x

Z3 Theorem Prover

Installation

Install Python (if not already installed):

sudo apt install python3

Install Z3 Solver:

pip install z3-solver
