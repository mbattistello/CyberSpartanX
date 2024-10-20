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
    await motor_pair.move_for_degrees(motor_pair.PAIR_1, degrees_for_distance(inches_to_move), 0, velocity=425)



# SPin TUrn
async def spin_turn(turn_degrees):
    await motor_pair.move_tank_for_degrees(motor_pair.PAIR_1, (turn_degrees), -525, 525 )

async def main():

    # Set up the motor pair
    motor_pair.pair(motor_pair.PAIR_1, port.C, port.D)

    await move_forward( 4 )
    await spin_turn(290)
    await move_forward( -20)
    await move_forward(3)
    await spin_turn(-70)
    await motor.run_for_degrees(port.E, -200, 200)
    '''  await move_forward(4)
    await spin_turn(353)
    await move_forward(10)
    await spin_turn(90)
    await move_forward(14)'''

runloop.run(main())
