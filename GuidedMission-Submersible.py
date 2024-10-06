
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

    

    # Forward - 30 inches
    await move_forward(31)


    # Sleep - 1 sec
    time.sleep( 1 )

    # Turn - 90 degrees
    await spin_turn(-180)

    # Sleep - 1 sec
    time.sleep( 1 )

    # Move foward - 25 inches 
    await move_forward(25)

    # Sleep - 1 sec
    time.sleep(1)

    # Turn - 60 degrees
    await spin_turn(60)

    # Sleep - 1 sec
    time.sleep(1)

    # Move forward - 3 inches
    await move_forward(2.2)

    # Make the robots arm move up
    await motor.run_for_degrees(port.E, -850, 200)



    # Stop
    motor_pair.stop
    
    # End of code 
runloop.run(main())
