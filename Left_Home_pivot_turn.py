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
async def continue_move_forward(inches_to_move):
    await motor_pair.move_for_degrees(motor_pair.PAIR_1, degrees_for_distance(inches_to_move), 0, velocity=525, stop=motor.CONTINUE)

#move forward without continue 
async def move_forward(inches_to_move):
    await motor_pair.move_for_degrees(motor_pair.PAIR_1, degrees_for_distance(inches_to_move), 0, velocity=450, acceleration=500)


# SPin TUrn
async def spin_turn(turn_degrees):
    await motor_pair.move_tank_for_degrees(motor_pair.PAIR_1, (turn_degrees), -525, 525 )

# Pivot Turn left
async def lpivot_turn(turn_degrees):
    await motor_pair.move_tank_for_degrees(motor_pair.PAIR_1, (turn_degrees), -525, -300 )

#PIvot TUrn right 
async def rpivot_turn(turn_degrees):
    await motor_pair.move_tank_for_degrees(motor_pair.PAIR_1, (turn_degrees), -300, -525 )



async def main():

    # Set up the motor pair
    motor_pair.pair(motor_pair.PAIR_1, port.A, port.E)

    await move_forward(-6.3)
    await spin_turn(145)
    await move_forward(-34.5)
    await motor.run_for_degrees(port.C, 180, 200)
    await spin_turn(90)
    await move_forward(-3.3)
    await motor.run_for_degrees(port.C, -190, 1110)
    await motor.run_for_degrees(port.F, -200, 200)
    await move_forward( 8.4 )
    await spin_turn(-75)
    await spin_turn(140)
    await spin_turn(-48)
    await move_forward(2.9)
    await motor.run_for_degrees(port.F, 190, 1000)
    '''await motor.run_for_degrees(port.C, 180, 200)
    await lpivot_turn(760)
    await move_forward(-11)
    await motor.run_for_degrees(port.C, -190, 200)
    await continue_move_forward(7)
    await lpivot_turn(-850)
    await motor.run_for_degrees(port.C, 180, 200)
    time.sleep(3)
    await lpivot_turn(1000)
    await move_forward(-9)
    await motor.run_for_degrees(port.C, -190, 200)
    await continue_move_forward(7)
    await lpivot_turn(-900)'''
    




runloop.run(main())
