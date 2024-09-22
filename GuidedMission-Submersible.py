from hub import port
import motor_pair
import motor
import runloop
import math

WHEEL_DIA_CM = 2.2

# set up inches sigma

def degrees_for_distance( distance_in ):
    wheel_circumfrence_in = math.pi * WHEEL_DIA_CM
    return int(( distance_in / wheel_circumfrence_in) * 360)


'''
async def main(cm): 
    #set up motor pair
    motor_pair.pair(motor_pair.PAIR_1, port.A, port.B)
    
    
    #runloop.run(main(25))


async def side():
    #make the robot turn
    motor_pair.move(motor_pair.PAIR_1, 180, velocity= 600, acceleration= 200)
    #stopvalue
    motor_pair.stop(motor_pair.PAIR_1, stop = 0 )

    #runloop.run(main(25))
'''


async def main():

    # Forward - 33 inches 
    motor_pair.pair(motor_pair.PAIR_1, port.C, port.D)

    await motor_pair.move_for_degrees(motor_pair.PAIR_1, degrees_for_distance(30), 0, velocity=550)

    #Spin turn clockwise 90 degrees
    motor_pair.move_tank(motor_pair.PAIR_1, 180, -180)

   # Forward - 23 inches
    await motor_pair.move_for_degrees(motor_pair.PAIR_1, degrees_for_distance(65),0)

    # Spin - 45 degrees
    motor_pair.move_tank(motor_pair.PAIR_1, 90, -90)

    # Lift arm
    motor_pair.pair(motor_pair.PAIR_1, port.E, port.E)
    await motor_pair.move_for_degrees(motor_pair.PAIR_1, degrees_for_distance(100),0)
    
runloop.run( main() )



