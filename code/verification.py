from z3 import *

# Define Traffic Light States
Red, Green, Yellow = Ints('Red Green Yellow')
states = [Red, Green, Yellow]

# Z3 Solver
solver = Solver()

# Initial State: Red
current_state = Int('current_state')
solver.add(current_state == Red)

# Transition Rules
transition = Function('transition', IntSort(), IntSort())
solver.add(transition(Red) == Green)
solver.add(transition(Green) == Yellow)
solver.add(transition(Yellow) == Red)

# Safety Rule - Prevent Red to Yellow Directly
invalid_transition = And(current_state == Red, transition(Red) == Yellow)
solver.add(Not(invalid_transition))

# Check if Constraints Hold
if solver.check() == sat:
    print("Traffic Light System is Correct. No Invalid States Detected.")
else:
    print("Invalid State Detected. Review Transition Rules.")
