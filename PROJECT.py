from multi_robomaster import multi_robot
from Program_Library import *
from robomaster import led, blaster
import time

sn_list = ['3JKCJ4M00105QR', '3JKCJ1L00105AA', '3JKCJ1L001050K',
            '3JKCJ1L001052N', '3JKDH7G0019VE9', '3JKCJ4M00105P2']
multi_robots = multi_robot.MultiEP()
multi_robots.initialize()
number = multi_robots.number_id_by_sn([0, sn_list[0]], [1, sn_list[1]], [2, sn_list[2]],
                                    [3, sn_list[3]], [4, sn_list[4]], [5, sn_list[5]])

robot_group_all=multi_robots.build_group([0, 1, 2, 3, 4, 5])
robot_group_red=multi_robots.build_group([0,2,4])
robot_group_blue=multi_robots.build_group([1,3,5])
robot_group1=multi_robots.build_group([0, 1])
robot_group2=multi_robots.build_group([2, 3])
robot_group3=multi_robots.build_group([4, 5])
ep0=multi_robots.build_group([0])
ep1=multi_robots.build_group([1])
ep2=multi_robots.build_group([2])
ep3=multi_robots.build_group([3])
ep4=multi_robots.build_group([4])
ep5=multi_robots.build_group([5])
ep_team=multi_robots.build_group([0,1,2,3,4])
print("系统初始化完成")
time.sleep(1)

multi_robots.run([robot_group_all,task_1])
print("task1已完成")
time.sleep(1)

multi_robots.run([robot_group_all,task_2])
print("task2已完成")
time.sleep(1)

multi_robots.run([robot_group_all,task_3])
print("task3已完成")
time.sleep(1)

multi_robots.run([robot_group1,task_4_1])
time.sleep(1)
multi_robots.run([robot_group2,task_4_2])
time.sleep(1)
multi_robots.run([robot_group3,task_4_3])
print("task4已完成")
time.sleep(1)

multi_robots.run([robot_group_red,task_5_red],[robot_group_blue,task_5_blue])
print("task5已完成")
time.sleep(1)

multi_robots.run([robot_group_all,task_6])
print("task6已完成")
time.sleep(1)

multi_robots.run([robot_group_all,task_7])
print("task7已完成")
time.sleep(1)

multi_robots.run([robot_group_red,task_8_red],[robot_group_blue,task_8_blue])
multi_robots.run([robot_group1,task_8_01],[robot_group2,task_8_23],[robot_group3,task_8_45])
print("task8已完成")
time.sleep(1)

multi_robots.run([robot_group_all,task_10])
time.sleep(1)
multi_robots.run([robot_group_red,task_10_red],[robot_group_blue,task_10_blue])
print("task10已完成")
"""
multi_robots.run([robot_group_all,task_11])
print("task11已完成")
time.sleep(1)

multi_robots.run([robot_group_all,task_12])
print("task12已完成")
time.sleep(1)
"""
multi_robots.close()
