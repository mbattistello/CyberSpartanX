from hub import light_matrix, motion_sensor, port
import runloop, motor_pair, motor, math


#global variables to hold distance to move and degress to turn to
MOVE_DISTANCE = 10
LEFT_TURN_ANGLE = 90


#setup variables for movement
velocity_value = 550  #-1100 - 1100
stop_value = motor.HOLD   # motor.BRAKE, BRAKE, HOLD, CONTINUE, SMART_COAST, SMART_BRAKE
acceleration_value = 5000# 0-10000
deceleration_value = 5000# 0-10000

#setup wheels
WHEEL_DIA_INCHES = 2.2

#convert distance to degress rotation
def degrees_for_distance():
    wheel_circumference_in = math.pi * WHEEL_DIA_INCHES
    return int( ( MOVE_DISTANCE / wheel_circumference_in ) * 360 )

#function to move forward a specific distance
def move_forward():
    print( "relative dist: " + str( abs( motor.relative_position( port.A ) ) ) + " > " + str(degrees_for_distance()) )

    return abs( motor.relative_position( port.A ) ) > degrees_for_distance()

#function to turn a specific angle
def turn_left():

    print( "yaw: " + str( abs( motion_sensor.tilt_angles()[0] * -0.1 ) ))

    return abs( motion_sensor.tilt_angles()[0] * -0.1 ) > LEFT_TURN_ANGLE

async def main():
    '''
    c <-- b
    |    /\
    \/    |
    d --> a - start/end
    '''

    #initialize motor pair
    motor_pair.pair( motor_pair.PAIR_1, port.A, port.B )

    #initialize motion sensor and make sure stable
    motion_sensor.reset_yaw( 0 )

    await runloop.until( motion_sensor.stable )  #turns until its true

    #move forward - a to b
    motor.reset_relative_position( port.A, 0 )

    motor_pair.move( motor_pair.PAIR_1, 0, 
                        velocity=velocity_value, acceleration=acceleration_value )

    await runloop.until( move_forward )

    motor_pair.stop( motor_pair.PAIR_1 )


    #turn left - b turning to c
    #initialize motion sensor and make sure stable
    motion_sensor.reset_yaw( 0 )

    await runloop.until( motion_sensor.stable )#turns until its true

    motor_pair.move( motor_pair.PAIR_1, -100)  #turn left

    await runloop.until( turn_left )

    motor_pair.stop( motor_pair.PAIR_1 )


    #move forward  - b to c
    motor.reset_relative_position( port.A, 0 )

    motor_pair.move( motor_pair.PAIR_1, 0,
                        velocity=velocity_value, acceleration=acceleration_value )

    await runloop.until( move_forward )

    motor_pair.stop( motor_pair.PAIR_1 )

    #turn left - c turning to d
    motion_sensor.reset_yaw( 0 )

    await runloop.until( motion_sensor.stable )#turns until its true

    motor_pair.move( motor_pair.PAIR_1, -100)#turn left

    await runloop.until( turn_left )

    motor_pair.stop( motor_pair.PAIR_1 )


    #move forward - c to d
    motor.reset_relative_position( port.A, 0 )

    motor_pair.move( motor_pair.PAIR_1, 0,
                        velocity=velocity_value, acceleration=acceleration_value )

    await runloop.until( move_forward )

    motor_pair.stop( motor_pair.PAIR_1 )


    #turn left - at d and point to a
    motion_sensor.reset_yaw( 0 )

    await runloop.until( motion_sensor.stable )#turns until its true

    motor_pair.move( motor_pair.PAIR_1, -100)#turn left

    await runloop.until( turn_left )

    motor_pair.stop( motor_pair.PAIR_1 )

    #move forward - d to a
    motor.reset_relative_position( port.A, 0 )

    motor_pair.move( motor_pair.PAIR_1, 0,
                        velocity=velocity_value, acceleration=acceleration_value )

    await runloop.until( move_forward )

    motor_pair.stop( motor_pair.PAIR_1 )

    #turn left - at a and point to b
    motion_sensor.reset_yaw( 0 )

    await runloop.until( motion_sensor.stable )#turns until its true

    motor_pair.move( motor_pair.PAIR_1, -100)#turn left

    await runloop.until( turn_left )

    motor_pair.stop( motor_pair.PAIR_1 )

runloop.run(main())
