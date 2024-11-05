# Test Rig 1
# GPIO +    : Switch Vcc
# GPIO 0    : Switch Out
# GPIO 1    : LED -ve
# GPIO 2    : LED +ve
# GPIO 3    : 
# GPIO -    : Switch Gnd

# Test Rig 2 - Ultrasonic
# GPIO +    : Vcc
# GPIO 0    : 
# GPIO 1    : Trig
# GPIO 2    : Echo
# GPIO 3    : 
# GPIO -    : Gnd


import robot
import time


TEST_TYPE = 2


R = robot.Robot()



if TEST_TYPE == 1:
    R.gpio[0].mode = robot.INPUT
    R.gpio[1].mode = robot.OUTPUT
    R.gpio[2].mode = robot.OUTPUT
    # R.gpio[3].mode = robot.OUTPUT

    R.gpio[1].digital = False


    while True:
        # Get the switch state. 0 means pressed, 1 means not pressed.
        state = not R.gpio[0].digital

        # Set the LED
        R.gpio[2].digital = state

        # Test Servo
        R.servos[0] = 100 * state

        # Test Motor
        R.motors[0] = (200 * state) - 100



        # Look for markers
        markers = R.see()

        for marker in markers:
            if marker.info.owning_team == robot.TEAM.ARENA:
                print(f"Marker {marker.info.id} is owned by the arena")
            elif marker.info.owning_team == R.zone:
                print(f"I own this marker")
            else:
                print(f"This marker is owned by {marker.info.owning_team}")

            if marker.info.type == robot.MARKER_TYPE.LAIR:
                print(f'This is a Lair belonging to {marker.info.owning_team}')
            elif marker.info.type == robot.MARKER_TYPE.BOX:
                print(f'This is a box belonging to {marker.info.owning_team}')
            else:
                print(f'This is an Arena marker')


elif TEST_TYPE == 2:
    while True:
        sensor = robot.UltrasonicSensor(R.gpio[1], R.gpio[2])
        distance = sensor.read()
        print(f"Distance to sensor is:{distance}")
        time.sleep(1)