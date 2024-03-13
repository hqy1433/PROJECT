from multi_robomaster import multi_robot
from robomaster import led
import time

def stand_by(robot_group):
    robot_group.led.set_led(led.COMP_ALL, 255, 1, 1, led.EFFECT_OFF)
    robot_group.blaster.set_led(brightness=255, effect='off')
    robot_group.gimbal.moveto(0, 0, 90, 90).wait_for_completed()
    robot_group.gimbal.suspend()

sn_list = ['3JKCJ4M00105QR', '3JKCJ1L00105AA', '3JKCJ1L001050K',
            '3JKCJ1L001052N', '3JKDH7G0019VE9', '3JKCJ4M00105P2']
multi_robots = multi_robot.MultiEP()
multi_robots.initialize()
number = multi_robots.number_id_by_sn([0, sn_list[0]], [1, sn_list[1]], [2, sn_list[2]],
                                    [3, sn_list[3]], [4, sn_list[4]], [5, sn_list[5]])

robot_group_all=multi_robots.build_group([0, 1, 2, 3, 4, 5])

multi_robots.run([robot_group_all,stand_by])
multi_robots.close()