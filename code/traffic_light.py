class TrafficLight:
    def __init__(self):
        self.state = "Red"

    def next(self):
        if self.state == "Red":
            self.state = "Green"
        elif self.state == "Green":
            self.state = "Yellow"
        elif self.state == "Yellow":
            self.state = "Red"

    def current_state(self):
        return self.state

# Simulate Traffic Light
if __name__ == "__main__":
    light = TrafficLight()
    for _ in range(5):
        print("Current Light:", light.current_state())
        light.next()
