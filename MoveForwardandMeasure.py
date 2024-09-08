from hub import light_matrix
from hub import motion_sensor
import motor_pair
import motor
from hub import port
import runloop
import math
import hub
import time
from app import linegraph
import color
import sys
import distance_sensor

#setup variables for movement
velocity_value = 1100  #-1100 - 1100
stop_value = motor.HOLD  # motor.BRAKE, BRAKE, HOLD, CONTINUE, SMART_COAST, SMART_BRAKE
acceleration_value = 10001  # 0-10000
deceleration_value = 1000  # 0-10000

WHEEL_DIA_INCHES = 2.2

DIST_TO_MOVE = 36

#init motor pair & distance snsor
motor_pair.pair( motor_pair.PAIR_1, port.A, port.B )
distance_sensor.distance(port.F)

#cacluation the degress to turn based on number of inches to travel
def degrees_for_distance( distance_in ):
    wheel_circumference_in = math.pi * WHEEL_DIA_INCHES
    return int( ( distance_in / wheel_circumference_in ) * 360 )

async def main():

    #move forward - pair, degress, steering, velocity, stop, acceleration, deceleration
    await motor_pair.move_for_degrees( motor_pair.PAIR_1, degrees_for_distance( DIST_TO_MOVE ), 0, 
                                    velocity=velocity_value, 
                                    stop=stop_value,
                                    acceleration=acceleration_value,
                                    deceleration=deceleration_value )


    #pause after moving to log stable points
    await runloop.sleep_ms(2000)

    #exit program
    sys.exit()
    


async def print_accel():  

    #setup the line graph
    linegraph.show( False )
    linegraph.clear_all()

    #orient the motion sensor
    motion_sensor.FRONT

    #counts x values
    x_count = 0

    while True:
        #setup acceleration and velocity
        acc = motion_sensor.acceleration( False )
        vel = motion_sensor.angular_velocity( False )

        acc_x = acc[0]  
        acc_y = acc[1]
        acc_z = acc[2]

        #add lines to plot
        linegraph.plot( color.BLUE, x_count, acc_y )
        linegraph.plot( color.RED, x_count, acc_x )
        linegraph.plot( color.GREEN, x_count, distance_sensor.distance( port.F ) )

        #this is needed when multiple runloops called
        await runloop.sleep_ms(5)

        #increment the x axis value for plot
        x_count += 1

#this starts the program and tells both main() and print_accel() to run in parallel
runloop.run( main() , print_accel() )
