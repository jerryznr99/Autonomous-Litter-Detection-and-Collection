import serial

import time

ssc32 = serial.Serial('/dev/tty.usbserial-AB0NBQKD', 9600)

def robot_arm_reset():
    print("reset")
    servo1 = 1 
    servo2 = 2
    servo3 = 3
    servo4 = 4

    pulse_width1 = 1500 #1000
    pulse_width2 = 1500 #1200
    pulse_width3 = 1500 #800
    pulse_width4 = 1500 #800

    delay = 1250

    command1 = f"#{servo1} P{pulse_width1} T{delay}\r"
    command2 = f"#{servo2} P{pulse_width2} T{delay}\r"
    command3 = f"#{servo3} P{pulse_width3} T{delay}\r"
    command4 = f"#{servo4} P{pulse_width4} T{delay}\r"

    ssc32.write(command4.encode())

    time.sleep(0.03)

    ssc32.write(command3.encode())

    time.sleep(0.03)

    ssc32.write(command1.encode())
    ssc32.write(command2.encode())

    time.sleep(0.03)

def robot_arm_move():
    servo1 = 1 
    servo2 = 2
    servo3 = 3
    servo4 = 4

    pulse_width1 = 1000 #1000
    pulse_width2 = 1200 #1200
    pulse_width3 = 800 #800
    pulse_width4 = 800 #800

    delay = 1250

    command1 = f"#{servo1} P{pulse_width1} T{delay}\r"
    command2 = f"#{servo2} P{pulse_width2} T{delay}\r"
    command3 = f"#{servo3} P{pulse_width3} T{delay}\r"
    command4 = f"#{servo4} P{pulse_width4} T{delay}\r"

    ssc32.write(command4.encode())

    time.sleep(0.05)

    ssc32.write(command3.encode())

    time.sleep(0.05)

    ssc32.write(command1.encode())
    ssc32.write(command2.encode())

    time.sleep(2)

    robot_arm_reset()

    time.sleep(3)

def robot_test():
    servo1 = 1
    servo2 = 2
    servo3 = 3 
    servo4 = 4
    servo5 = 5
    
    pulse_width1 = 1100
    pulse_width2 = 1650
    pulse_width3 = 1950
    pulse_width4 = 500

    delay = 1250

    command1 = f"#{servo1} P{pulse_width1} T{delay}\r"
    command2 = f"#{servo2} P{pulse_width2} T{delay}\r"
    command3 = f"#{servo3} P{pulse_width3} T{delay}\r"
    command4 = f"#{servo4} P{pulse_width4} T{delay}\r"

    ssc32.write(command1.encode())
    ssc32.write(command2.encode())
    ssc32.write(command3.encode())
    ssc32.write(command4.encode())

    time.sleep(2)

    pulse_width1 = 800
    pulse_width2 = 1100
    pulse_width3 = 1800

    command1 = f"#{servo1} P{pulse_width1} T{delay}\r"
    command2 = f"#{servo2} P{pulse_width2} T{delay}\r"
    command3 = f"#{servo3} P{pulse_width3} T{delay}\r"

    ssc32.write(command1.encode())
    ssc32.write(command2.encode())
    ssc32.write(command3.encode())

    time.sleep(2)

    pulse_width4 = 1500

    command4 = f"#{servo4} P{pulse_width4} T{delay}\r"

    ssc32.write(command4.encode())

    time.sleep(2)

    robot_arm_reset()

    time.sleep(2)

    pulse_width1 = 1650
    pulse_width2 = 700
    pulse_width3 = 1900

    command1 = f"#{servo1} P{pulse_width1} T{delay}\r"
    command2 = f"#{servo2} P{pulse_width2} T{delay}\r"
    command3 = f"#{servo3} P{pulse_width3} T{delay}\r"

    ssc32.write(command1.encode())
    ssc32.write(command2.encode())
    ssc32.write(command3.encode())

    time.sleep(2)

    pulse_width4 = 500
    pulse_width5 = 1500

    command4 = f"#{servo4} P{pulse_width4} T{delay}\r"
    command5 = f"#{servo5} P{pulse_width5} T{delay}\r"
    
    ssc32.write(command4.encode())
    ssc32.write(command5.encode())

    time.sleep(2)

robot_test()

robot_arm_reset()