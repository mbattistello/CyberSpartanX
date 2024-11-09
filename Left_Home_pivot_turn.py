from hub import port
import motor_pair
import motor
import runloop
import math
import time


WHEEL_DIA_CM = 4.4

# set up inches
def degrees_for_distance( distance_in ):
    wheel_circumfrence_in = math.pi * WHEEL_DIA_CM
    return int(( distance_in / wheel_circumfrence_in) * 360)

def turn_robot_deg( degr_to_turn ):

    None

# move forward def
async def move_forward(inches_to_move):
    await motor_pair.move_for_degrees(motor_pair.PAIR_1, degrees_for_distance(inches_to_move), 0, velocity=525, stop=motor.CONTINUE)



# SPin TUrn
async def spin_turn(turn_degrees):
    await motor_pair.move_tank_for_degrees(motor_pair.PAIR_1, (turn_degrees), -525, 525 )

# Pivot Turn
async def lpivot_turn(turn_degrees):
    await motor_pair.move_tank_for_degrees(motor_pair.PAIR_1, (turn_degrees), -525, -300 )

async def rpivot_turn(turn_degrees):
    await motor_pair.move_tank_for_degrees(motor_pair.PAIR_1, (turn_degrees), -300, -525 )



async def main():

    # Set up the motor pair
    motor_pair.pair(motor_pair.PAIR_1, port.A, port.E)
    
    
    await motor.run_for_degrees(port.C, 180, 200)
    await lpivot_turn(700)
    time.sleep(1)
    await move_forward(-1)
    await motor.run_for_degrees(port.C, -180, 200)
    await move_forward(-7)
    await lpivot_turn(-500)


    

runloop.run(main())
