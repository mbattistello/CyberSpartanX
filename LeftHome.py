
from hub import port
import motor_pair
import motor
import runloop
import math
import time


WHEEL_DIA_CM = 2.2

# set up inches
def degrees_for_distance( distance_in ):
    wheel_circumfrence_in = math.pi * WHEEL_DIA_CM
    return int(( distance_in / wheel_circumfrence_in) * 360)

def turn_robot_deg( degr_to_turn ):

    None

# move forward def
async def move_forward(inches_to_move):
    await motor_pair.move_for_degrees(motor_pair.PAIR_1, degrees_for_distance(inches_to_move), 0, velocity=525)



# SPin TUrn
async def spin_turn(turn_degrees):
    await motor_pair.move_tank_for_degrees(motor_pair.PAIR_1, (turn_degrees), -525, 525 )


async def main():

    # Set up the motor pair
    motor_pair.pair(motor_pair.PAIR_1, port.C, port.D)

    await motor.run_for_degrees(port.E, -290, 200)



    # Forward - 30 inches
    await move_forward(34.5)


    # Sleep - 1 sec
    time.sleep( 1 )

    # Turn - 90 degrees
    await spin_turn(170)

    await move_forward(1.5)

    await motor.run_for_degrees(port.E, 230, 200)

    # Sleep - 1 sec
    time.sleep( 1 )

    # turn 90 right
    await spin_turn(-170)

    

    # Move foward - 25 inches
    await move_forward(-34.5)

    time.sleep( 7 )

    # Move forward after returning to red base
    await move_forward(43)

    await spin_turn(180)


    await move_forward(7.5)

    await spin_turn(150)

    # Stop
    motor_pair.stop

    # End of code
runloop.run(main())
