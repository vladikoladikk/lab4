import time

class TrafficLight:
    def __init__(self):
        self.__color = "red"  # Приватный атрибут

    def running(self):
        while True:
            if self.__color == "red":
                print("Red light. Stop!")
                time.sleep(7)
                self.__color = "yellow"
            elif self.__color == "yellow":
                print("Yellow light. Prepare to move!")
                time.sleep(2)
                self.__color = "green"
            elif self.__color == "green":
                print("Green light. Go!")
                time.sleep(5)
                self.__color = "red"

traffic_light = TrafficLight()
traffic_light.running()
