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
    await motor_pair.move_for_degrees(motor_pair.PAIR_1, degrees_for_distance(inches_to_move), 0, velocity=525)



# SPin TUrn
async def spin_turn(turn_degrees):
    await motor_pair.move_tank_for_degrees(motor_pair.PAIR_1, (turn_degrees), -525, 525 )

# Start at third black line

async def main():

    # Set up the motor pair
    motor_pair.pair(motor_pair.PAIR_1, port.A, port.E)
    

    motor.run_for_degrees(port.C, 90, 100)
    await move_forward(-37)
    await spin_turn(105)
    await motor.run_for_degrees(port.C, -140, 200)
    await motor.run_for_degrees(port.C, 140, 200)
    await move_forward(3)
    await spin_turn(-150)
    await move_forward(-4)
    await motor.run_for_degrees(port.C, -160, 200)
    await motor.run_for_degrees(port.C, 160, 200)
    await move_forward(5)
    await spin_turn(100)
    await move_forward(5)
    await spin_turn(-180)
    await move_forward(3)
    await move_forward(-2)
    await spin_turn(180)
    await move_forward(25)

    await time.sleep(9)

    await move_forward(6)
    await spin_turn(-180)
    await move_forward(-25)
    await motor.run_for_degrees(port.C, -160, 200)
    await move_forward(-30)
    await spin_turn(-180)
    await move_forward(-10)
    

    await time.sleep(12)

    await move_forward(3)
    
runloop.run(main())
