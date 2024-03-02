from multi_robomaster import multi_robot
from robomaster import led, blaster
import time

def task_1(robot_group):
    robot_group.play_sound(2)
    robot_group.gimbal.resume()
    robot_group.gimbal.recenter(90,90)
    robot_group.led.set_led(led.COMP_BOTTOM_ALL, 255, 1, 1, led.EFFECT_FLASH)
    robot_group.led.set_led(led.COMP_TOP_LEFT, 255, 1, 1, led.EFFECT_SCROLLING)
    time.sleep(0.2)
    robot_group.led.set_led(led.COMP_TOP_RIGHT, 255, 1, 1, led.EFFECT_SCROLLING)
    time.sleep(3)
    robot_group.led.set_led(led.COMP_ALL, 255, 1, 1, led.EFFECT_OFF)
    robot_group.gimbal.moveto(-20, 0, 45, 45).wait_for_completed()
    
def task_2(robot_group):
    media_sound=0x110
    r=0;g=0;b=0
    for robot_id in robot_group._robots_id_in_group_list:
        r+=42;g+=42;b+=42
        robot_obj = robot_group.get_robot(robot_id)
        robot_obj.blaster.fire(fire_type='water', times=1)
        robot_obj.play_sound(media_sound)
        robot_obj.blaster.set_led(brightness=255, effect='on')
        robot_obj.led.set_led(led.COMP_ALL, r, g, b, led.EFFECT_ON)
        robot_obj.gimbal.moveto(20, 0, 45, 45)
        robot_obj.chassis.move(0, 0, -90, 0, 90).wait_for_completed()
        robot_obj.led.set_led(led.COMP_ALL, r, g, b, led.EFFECT_FLASH)
        media_sound += 2
        time.sleep(0.5)
    robot_group.blaster.set_led(brightness=255, effect='off')
    robot_group.chassis.move(0, 0, 90, 0, 90).wait_for_completed()
        
def task_3(robot_group):
    robot_group.gimbal.moveto(-10, 65, 90, 90).wait_for_completed()
    robot_group.blaster.set_led(brightness=255, effect='on')
    robot_group.gimbal.moveto(-10, -65, 15, 15).wait_for_completed()
    robot_group.blaster.set_led(brightness=255, effect='off')
    robot_group.led.set_led(led.COMP_TOP_ALL, 255, 255, 255, led.EFFECT_SCROLLING)
    robot_group.led.set_led(led.COMP_BOTTOM_ALL, 255, 255, 255, led.EFFECT_ON)
    robot_group.gimbal.moveto(0, 0, 90, 90).wait_for_completed()

def task_4_1(robot_group):
    robot_group.led.set_led(led.COMP_ALL, 255, 1, 1, led.EFFECT_OFF)
    robot_group.gimbal.moveto(0, 0, 90, 90).wait_for_completed()
    robot_group.blaster.set_led(brightness=255, effect='on')
    robot_group.led.set_led(led.COMP_ALL, 255, 127, 1, led.EFFECT_ON)
    robot_group.gimbal.moveto(20, 0, 90, 90).wait_for_completed()
    robot_group.blaster.fire(fire_type='water', times=1)
    robot_group.led.set_led(led.COMP_ALL, 255, 127, 1, led.EFFECT_FLASH,5)

def task_4_2(robot_group):
    robot_group.led.set_led(led.COMP_ALL, 255, 1, 1, led.EFFECT_OFF)
    robot_group.gimbal.moveto(0, 0, 90, 90).wait_for_completed()
    robot_group.blaster.set_led(brightness=255, effect='on')
    robot_group.led.set_led(led.COMP_ALL, 1, 255, 127, led.EFFECT_ON)
    robot_group.gimbal.moveto(20, 0, 90, 90).wait_for_completed()
    robot_group.blaster.fire(fire_type='water', times=2)
    robot_group.led.set_led(led.COMP_ALL, 1, 255, 127, led.EFFECT_FLASH,5)

def task_4_3(robot_group):
    robot_group.led.set_led(led.COMP_ALL, 255, 1, 1, led.EFFECT_OFF)
    robot_group.gimbal.moveto(0, 0, 90, 90).wait_for_completed()
    robot_group.blaster.set_led(brightness=255, effect='on')
    robot_group.led.set_led(led.COMP_ALL, 127, 1, 255, led.EFFECT_ON)
    robot_group.gimbal.moveto(20, 0, 90, 90).wait_for_completed()
    robot_group.blaster.fire(fire_type='water', times=3)
    robot_group.led.set_led(led.COMP_ALL, 127, 1, 255, led.EFFECT_FLASH,5)

def task_5_red(robot_group):
    robot_group.set_group_robots_mode(mode="chassis_lead")
    robot_group.led.set_led(led.COMP_ALL, 255, 1, 1, led.EFFECT_FLASH,3)
    robot_group.chassis.move(0,0.25,0,0.5,30).wait_for_completed()
    robot_group.led.set_led(led.COMP_TOP_ALL, 255, 1, 1, led.EFFECT_SCROLLING)
    robot_group.play_sound(0x107)
    time.sleep(0.2)
    robot_group.led.set_led(led.COMP_ALL, 255, 1, 1, led.EFFECT_FLASH,3)
    robot_group.chassis.move(0.5,0,0,0.5,30).wait_for_completed()
    robot_group.led.set_led(led.COMP_TOP_ALL, 255, 1, 1, led.EFFECT_SCROLLING)
    robot_group.play_sound(0x109)
    time.sleep(0.2)
    robot_group.led.set_led(led.COMP_TOP_ALL, 255, 1, 1, led.EFFECT_ON)

def task_5_blue(robot_group):
    robot_group.set_group_robots_mode(mode="chassis_lead")
    robot_group.led.set_led(led.COMP_ALL, 1, 1, 255, led.EFFECT_FLASH,3)
    robot_group.chassis.move(0,-0.25,0,0.5,30).wait_for_completed()
    robot_group.led.set_led(led.COMP_TOP_ALL, 1, 1, 255, led.EFFECT_SCROLLING)
    robot_group.play_sound(0x107)
    time.sleep(0.2)
    robot_group.led.set_led(led.COMP_ALL, 1, 1, 255, led.EFFECT_FLASH,3)
    robot_group.chassis.move(0.5,0,0,0.5,30).wait_for_completed()
    robot_group.led.set_led(led.COMP_TOP_ALL, 1, 1, 255, led.EFFECT_SCROLLING)
    robot_group.play_sound(0x109)
    time.sleep(0.2)
    robot_group.led.set_led(led.COMP_TOP_ALL, 1, 1, 255, led.EFFECT_ON)

def task_6(robot_group):
    robot_group.set_group_robots_mode(mode="free")
    robot_group.led.set_led(led.COMP_ALL, 255, 255, 255, led.EFFECT_OFF)
    robot_group.play_sound(0x11A)
    robot_group.gimbal.moveto(0, -180, 0, 360).wait_for_completed()

    light=0
    for robot_id in range(0,6): # 0 1 2 3 4 5
        light+=42
        robot_obj=robot_group.get_robot(robot_id)
        robot_obj.led.set_led(led.COMP_TOP_ALL, 255, 255, 255, led.EFFECT_ON)
        robot_obj.led.set_led(led.COMP_TOP_ALL, 255, 255, 255, led.EFFECT_SCROLLING)
        robot_obj.blaster.set_led(brightness=light, effect='on')
        robot_obj.gimbal.moveto(0, 180, 0, 360).wait_for_completed()
        robot_obj.play_sound(0x101,time=robot_id+1).wait_for_completed(0.5)
        robot_obj.blaster.fire(fire_type='ir', times=1)
        robot_obj.play_sound(0x101)
        robot_obj.blaster.set_led(brightness=0, effect='off')
        robot_obj.led.set_led(led.COMP_TOP_ALL, 255, 255, 255, led.EFFECT_ON)

    for robot_id in range(0,6): # 0 1 2 3 4 5
        light-=42
        robot_obj=robot_group.get_robot(robot_id)
        robot_obj.led.set_led(led.COMP_TOP_ALL, 255, 255, 255, led.EFFECT_ON)
        robot_obj.led.set_led(led.COMP_TOP_ALL, 255, 255, 255, led.EFFECT_SCROLLING)
        robot_obj.blaster.set_led(brightness=light, effect='on')
        robot_obj.gimbal.moveto(0, -180, 0, 360).wait_for_completed()
        robot_obj.play_sound(0x101,time=robot_id+1).wait_for_completed(0.5)
        robot_obj.blaster.fire(fire_type='ir', times=1)
        robot_obj.play_sound(0x101)
        robot_obj.blaster.set_led(brightness=0, effect='off')
        robot_obj.led.set_led(led.COMP_TOP_ALL, 255, 255, 255, led.EFFECT_ON)

    robot_group.gimbal.moveto(0, 0, 0, 360).wait_for_completed()
    robot_group.led.set_led(led.COMP_TOP_ALL, 255, 255, 255, led.EFFECT_OFF)

def task_7(robot_group):
    robot_group.set_group_robots_mode(mode="gimbal_lead")
    robot_group.led.set_led(led.COMP_ALL, 255, 255, 255, led.EFFECT_FLASH,10)
    robot_group.blaster.set_led(brightness=255, effect='on')
    robot_group.gimbal.moveto(0, 45, 0, 90).wait_for_completed()
    robot_group.gimbal.moveto(0, -45, 0, 90).wait_for_completed()
    robot_group.gimbal.moveto(0, 0, 0, 90).wait_for_completed()
    robot_group.gimbal.moveto(20, 0, 0, 20).wait_for_completed()
    robot_group.blaster.set_led(brightness=255, effect='off')
    robot_group.blaster.fire(fire_type='water', times=3)
    robot_group.gimbal.moveto(0, 0, 0, 20).wait_for_completed()

    r=0;g=0;b=0
    for robot_id in range(0,6): #0 1 2 3 4 5
        robot_obj=robot_group.get_robot(robot_id)
        r+=42;g+=14;b+=4
        robot_obj.led.set_led(led.COMP_ALL, r, g, b, led.EFFECT_BREATH)
        robot_obj.blaster.fire(fire_type='ir', times=1)
        robot_obj.play_sound(0x101)
        time.sleep(0.2)

    music=0x113
    for times in range(0,5,2):# 0 2 4
        robot_group.gimbal.moveto(20, 0, 0, 20).wait_for_completed()
        robot_group.gimbal.moveto(-20, 0, 0, 20).wait_for_completed()
        robot_obj.play_sound(music+2)
        time.sleep(0.5)
    
    robot_group.led.set_led(led.COMP_TOP_ALL, 255, 255, 255, led.EFFECT_OFF)

def task_8_red(robot_group):
    robot_group.set_group_robots_mode(mode="free")
    robot_group.gimbal.suspend()
    robot_group.led.set_led(led.COMP_BOTTOM_ALL, 255, 255, 255, led.EFFECT_BREATH)
    robot_group.led.set_led(led.COMP_TOP_ALL, 255, 255, 255, led.EFFECT_FLASH,5)
    time.sleep(2)
    robot_group.gimbal.resume()
    robot_group.play_sound(0x103)
    robot_group.led.set_led(led.COMP_BOTTOM_ALL, 255, 1, 1, led.EFFECT_BREATH)
    robot_group.led.set_led(led.COMP_TOP_LEFT, 255, 1, 1, led.EFFECT_SCROLLING)
    time.sleep(0.2)
    robot_group.led.set_led(led.COMP_TOP_RIGHT, 255, 1, 1, led.EFFECT_SCROLLING)
    robot_group.gimbal.moveto(20, 0, 0, 20).wait_for_completed()
    robot_group.gimbal.moveto(-20, 0, 0, 20).wait_for_completed()
    robot_group.gimbal.moveto(0, 0, 0, 20).wait_for_completed()
    robot_group.led.set_led(led.COMP_ALL, 255, 1, 1, led.EFFECT_FLASH,10)
    time.sleep(0.2)
    robot_group.led.set_led(led.COMP_ALL, 255, 1, 1, led.EFFECT_ON)

def task_8_blue(robot_group):
    robot_group.set_group_robots_mode(mode="free")
    robot_group.gimbal.suspend()
    robot_group.led.set_led(led.COMP_BOTTOM_ALL, 255, 255, 255, led.EFFECT_BREATH)
    robot_group.led.set_led(led.COMP_TOP_ALL, 255, 255, 255, led.EFFECT_FLASH,5)
    time.sleep(2)
    robot_group.gimbal.resume()
    robot_group.play_sound(0X103)
    robot_group.led.set_led(led.COMP_BOTTOM_ALL, 1, 1, 255, led.EFFECT_BREATH)
    robot_group.led.set_led(led.COMP_TOP_LEFT, 1, 1, 255, led.EFFECT_SCROLLING)
    time.sleep(0.2)
    robot_group.led.set_led(led.COMP_TOP_RIGHT, 1, 1, 255, led.EFFECT_SCROLLING)
    robot_group.gimbal.moveto(20, 0, 0, 20).wait_for_completed()
    robot_group.gimbal.moveto(-20, 0, 0, 20).wait_for_completed()
    robot_group.gimbal.moveto(0, 0, 0, 20).wait_for_completed()
    robot_group.led.set_led(led.COMP_ALL, 1, 1, 255, led.EFFECT_FLASH,10)
    time.sleep(0.2)
    robot_group.led.set_led(led.COMP_ALL, 1, 1, 255, led.EFFECT_ON)

def task_8_01(robot_group):
    ep0=robot_group.get_robot(0)
    ep1=robot_group.get_robot(1)
    robot_group.set_group_robots_mode(mode="free")
    time.sleep(1)
    robot_group.chassis.move(0,0.5,0,0.5,30).wait_for_completed()
    robot_group.led.set_led(led.COMP_ALL, 255, 255, 255, led.EFFECT_FLASH,5)
    time.sleep(0.5)
    ep0.led.set_led(led.COMP_ALL, 255, 1, 255, led.EFFECT_ON)
    ep1.led.set_led(led.COMP_ALL, 1, 1, 255, led.EFFECT_ON)
    robot_group.gimbal.moveto(0, -90, 0, 180)
    robot_group.chassis.move(1,0,0,0.5,30).wait_for_completed()
    robot_group.gimbal.moveto(0, 0, 0, 180)
    robot_group.led.set_led(led.COMP_ALL, 255, 255, 255, led.EFFECT_FLASH,5)
    time.sleep(0.5)
    ep0.led.set_led(led.COMP_ALL, 255, 1, 255, led.EFFECT_ON)
    ep1.led.set_led(led.COMP_ALL, 1, 1, 255, led.EFFECT_ON)
    robot_group.play_sound(0x11c)

def task_8_45(robot_group):
    ep4=robot_group.get_robot(4)
    ep5=robot_group.get_robot(5)
    robot_group.set_group_robots_mode(mode="free")
    robot_group.gimbal.moveto(0, 180, 0, 180)
    robot_group.chassis.move(0,-0.5,0,0.5,30).wait_for_completed()
    robot_group.led.set_led(led.COMP_ALL, 255, 255, 255, led.EFFECT_FLASH,5)
    time.sleep(0.5)
    ep4.led.set_led(led.COMP_ALL, 255, 1, 255, led.EFFECT_ON)
    ep5.led.set_led(led.COMP_ALL, 1, 1, 255, led.EFFECT_ON)
    robot_group.gimbal.moveto(0, 90, 0, 180)
    robot_group.chassis.move(-1,0,0,0.5,30).wait_for_completed()
    robot_group.gimbal.moveto(0, 0, 0, 180)
    robot_group.led.set_led(led.COMP_ALL, 255, 255, 255, led.EFFECT_FLASH,5)
    time.sleep(0.5)
    ep4.led.set_led(led.COMP_ALL, 255, 1, 255, led.EFFECT_ON)
    ep5.led.set_led(led.COMP_ALL, 1, 1, 255, led.EFFECT_ON)
    robot_group.play_sound(0x11c)

def task_8_23(robot_group):
    ep2=robot_group.get_robot(2)
    ep3=robot_group.get_robot(3)
    robot_group.set_group_robots_mode(mode="free")
    time.sleep(1.5)#等待其他机器人相应计时
    robot_group.led.set_led(led.COMP_ALL, 255, 255, 255, led.EFFECT_FLASH,5)
    time.sleep(0.5)
    ep2.led.set_led(led.COMP_ALL, 255, 1, 255, led.EFFECT_ON)
    ep3.led.set_led(led.COMP_ALL, 1, 1, 255, led.EFFECT_ON)
    time.sleep(1.5)#等待其他机器人相应计时
    robot_group.led.set_led(led.COMP_ALL, 255, 255, 255, led.EFFECT_FLASH,5)
    time.sleep(0.5)
    ep2.led.set_led(led.COMP_ALL, 255, 1, 255, led.EFFECT_ON)
    ep3.led.set_led(led.COMP_ALL, 1, 1, 255, led.EFFECT_ON)

def task_9(robot_group):
    kind_one=["0","1,2","3,4","5"]
    kind_two=["1","0,3","2,5","4"]
    robot_group.set_group_robots_mode(mode="free")
    robot_group.led.set_led(led.COMP_ALL, 0, 0, 0, led.EFFECT_OFF)
    robot_group.gimbal.suspend()

    r=0;g=0;b=0
    music=0x11C-2
    for robot_ids in kind_one:
        robot_id_list=robot_ids.split(",")
        r+=16;g+=16;b+=16
        music+=2
        if len(robot_id_list)==1:
            ep=robot_group.get_robot(int(robot_id_list[0]))
            ep.play_sound(music)
            ep.led.set_led(led.COMP_ALL, r, g, b, led.EFFECT_FLASH,5)
            ep.gimbal.resume()
            ep.gimbal.moveto(20, 0, 0, 40).wait_for_completed()
            ep.play_sound(0x101)
            ep.blaster.fire(fire_type='ir', times=1)
            ep.led.set_led(led.COMP_ALL, 0, 0, 0, led.EFFECT_OFF)
            ep.gimbal.suspend()
        else:
            ep_one=robot_group.get_robot(int(robot_id_list[0]))
            ep_two=robot_group.get_robot(int(robot_id_list[1]))
            ep_one.play_sound(music)
            ep_two.play_sound(music)
            ep_one.led.set_led(led.COMP_ALL, r, g, b, led.EFFECT_FLASH,5)
            ep_two.led.set_led(led.COMP_ALL, r, g, b, led.EFFECT_FLASH,5)
            ep_one.gimbal.resume()
            ep_two.gimbal.resume()
            ep_one.gimbal.moveto(20, 0, 0, 40)
            ep_two.gimbal.moveto(20, 0, 0, 40).wait_for_completed()
            ep_one.play_sound(0x101)
            ep_two.play_sound(0x101)
            ep_one.blaster.fire(fire_type='ir', times=1)
            ep_two.blaster.fire(fire_type='ir', times=1)
            ep_one.led.set_led(led.COMP_ALL, 0, 0, 0, led.EFFECT_OFF)
            ep_two.led.set_led(led.COMP_ALL, 0, 0, 0, led.EFFECT_OFF)
            ep_one.gimbal.suspend()
            ep_two.gimbal.suspend()
    music=0x11C-2
    for robot_ids in kind_one[::-1]:
        robot_id_list=robot_ids.split(",")
        r+=16;g+=16;b+=16
        music+=2
        if len(robot_id_list)==1:
            ep=robot_group.get_robot(int(robot_id_list[0]))
            ep.play_sound(music)
            ep.led.set_led(led.COMP_ALL, r, g, b, led.EFFECT_FLASH,5)
            ep.gimbal.resume()
            ep.gimbal.moveto(20, 0, 0, 40).wait_for_completed()
            ep.play_sound(0x101)
            ep.blaster.fire(fire_type='ir', times=1)
            ep.led.set_led(led.COMP_ALL, 0, 0, 0, led.EFFECT_OFF)
            ep.gimbal.suspend()
        else:
            ep_one=robot_group.get_robot(int(robot_id_list[0]))
            ep_two=robot_group.get_robot(int(robot_id_list[1]))
            ep_one.play_sound(music)
            ep_two.play_sound(music)
            ep_one.led.set_led(led.COMP_ALL, r, g, b, led.EFFECT_FLASH,5)
            ep_two.led.set_led(led.COMP_ALL, r, g, b, led.EFFECT_FLASH,5)
            ep_one.gimbal.resume()
            ep_two.gimbal.resume()
            ep_one.gimbal.moveto(20, 0, 0, 40)
            ep_two.gimbal.moveto(20, 0, 0, 40).wait_for_completed()
            ep_one.play_sound(0x101)
            ep_two.play_sound(0x101)
            ep_one.blaster.fire(fire_type='ir', times=1)
            ep_two.blaster.fire(fire_type='ir', times=1)
            ep_one.led.set_led(led.COMP_ALL, 0, 0, 0, led.EFFECT_OFF)
            ep_two.led.set_led(led.COMP_ALL, 0, 0, 0, led.EFFECT_OFF)
            ep_one.gimbal.suspend()
            ep_two.gimbal.suspend()
    music=0x11C-2
    for robot_ids in kind_two:
        robot_id_list=robot_ids.split(",")
        r+=16;g+=16;b+=16
        music+=2
        if len(robot_id_list)==1:
            ep=robot_group.get_robot(int(robot_id_list[0]))
            ep.play_sound(music)
            ep.led.set_led(led.COMP_ALL, r, g, b, led.EFFECT_FLASH,5)
            ep.gimbal.resume()
            ep.gimbal.moveto(20, 0, 0, 40).wait_for_completed()
            ep.play_sound(0x101)
            ep.blaster.fire(fire_type='ir', times=1)
            ep.led.set_led(led.COMP_ALL, 0, 0, 0, led.EFFECT_OFF)
            ep.gimbal.suspend()
        else:
            ep_one=robot_group.get_robot(int(robot_id_list[0]))
            ep_two=robot_group.get_robot(int(robot_id_list[1]))
            ep_one.play_sound(music)
            ep_two.play_sound(music)
            ep_one.led.set_led(led.COMP_ALL, r, g, b, led.EFFECT_FLASH,5)
            ep_two.led.set_led(led.COMP_ALL, r, g, b, led.EFFECT_FLASH,5)
            ep_one.gimbal.resume()
            ep_two.gimbal.resume()
            ep_one.gimbal.moveto(20, 0, 0, 40)
            ep_two.gimbal.moveto(20, 0, 0, 40).wait_for_completed()
            ep_one.play_sound(0x101)
            ep_two.play_sound(0x101)
            ep_one.blaster.fire(fire_type='ir', times=1)
            ep_two.blaster.fire(fire_type='ir', times=1)
            ep_one.led.set_led(led.COMP_ALL, 0, 0, 0, led.EFFECT_OFF)
            ep_two.led.set_led(led.COMP_ALL, 0, 0, 0, led.EFFECT_OFF)
            ep_one.gimbal.suspend()
            ep_two.gimbal.suspend()
    music=0x11C-2
    for robot_ids in kind_two[::-1]:
        robot_id_list=robot_ids.split(",")
        r+=16;g+=16;b+=16
        music+=2
        if len(robot_id_list)==1:
            ep=robot_group.get_robot(int(robot_id_list[0]))
            ep.play_sound(music)
            ep.led.set_led(led.COMP_ALL, r, g, b, led.EFFECT_FLASH,5)
            ep.gimbal.resume()
            ep.gimbal.moveto(20, 0, 0, 40).wait_for_completed()
            ep.play_sound(0x101)
            ep.blaster.fire(fire_type='ir', times=1)
            ep.led.set_led(led.COMP_ALL, 0, 0, 0, led.EFFECT_OFF)
            ep.gimbal.suspend()
        else:
            ep_one=robot_group.get_robot(int(robot_id_list[0]))
            ep_two=robot_group.get_robot(int(robot_id_list[1]))
            ep_one.play_sound(music)
            ep_two.play_sound(music)
            ep_one.led.set_led(led.COMP_ALL, r, g, b, led.EFFECT_FLASH,5)
            ep_two.led.set_led(led.COMP_ALL, r, g, b, led.EFFECT_FLASH,5)
            ep_one.gimbal.resume()
            ep_two.gimbal.resume()
            ep_one.gimbal.moveto(20, 0, 0, 40)
            ep_two.gimbal.moveto(20, 0, 0, 40).wait_for_completed()
            ep_one.play_sound(0x101)
            ep_two.play_sound(0x101)
            ep_one.blaster.fire(fire_type='ir', times=1)
            ep_two.blaster.fire(fire_type='ir', times=1)
            ep_one.led.set_led(led.COMP_ALL, 0, 0, 0, led.EFFECT_OFF)
            ep_two.led.set_led(led.COMP_ALL, 0, 0, 0, led.EFFECT_OFF)
            ep_one.gimbal.suspend()
            ep_two.gimbal.suspend()

def task_10(robot_group):
    robot_group.gimbal.resume()
    robot_group.set_group_robots_mode(mode="free")
    for robot_id in range(0,6):
        robot_obj=robot_group.get_robot(robot_id)
        if robot_id%2==0:
            robot_obj.led.set_led(led.COMP_ALL, 255, 1, 1, led.EFFECT_ON)
            robot_obj.play_sound(0x11F)
        else:
            robot_obj.led.set_led(led.COMP_ALL, 1, 1, 255, led.EFFECT_ON)
            robot_obj.play_sound(0x107)
        robot_group.gimbal.moveto(20, 0, 90, 90).wait_for_completed()
        robot_obj.blaster.fire(fire_type='water', times=1)

    robot_group.gimbal.moveto(0, 0, 180, 180).wait_for_completed()
    robot_group.gimbal.moveto(-10, 65, 90, 90).wait_for_completed()
    robot_group.blaster.set_led(brightness=255, effect='on')
    robot_group.gimbal.moveto(-10, -65, 15, 15).wait_for_completed()
    robot_group.blaster.set_led(brightness=255, effect='off')
    robot_group.led.set_led(led.COMP_TOP_ALL, 255, 255, 255, led.EFFECT_SCROLLING)
    robot_group.led.set_led(led.COMP_BOTTOM_ALL, 255, 255, 255, led.EFFECT_ON)
    robot_group.gimbal.moveto(0, 0, 90, 90).wait_for_completed()

def task_10_red(robot_group):
    robot_group.set_group_robots_mode(mode="free")
    robot_group.led.set_led(led.COMP_BOTTOM_ALL, 255, 255, 255, led.EFFECT_FLASH,5)
    robot_group.chassis.move(0,0,-90,0.5,90)
    robot_group.gimbal.moveto(0, -90, 90, 45).wait_for_completed()
    robot_group.led.set_led(led.COMP_TOP_ALL, 255, 0, 0, led.EFFECT_SCROLLING)
    robot_group.led.set_led(led.COMP_BOTTOM_ALL, 255, 0, 0, led.EFFECT_ON)
    robot_group.gimbal.moveto(20, 0, 180, 180).wait_for_completed()
    for i in range(0,3):
        robot_group.gimbal.moveto(-20, 0, 40, 40).wait_for_completed()
        time.sleep(0.2)
        robot_group.gimbal.moveto(20, 0, 40, 40).wait_for_completed()
    for i in range(0,3):
        robot_group.gimbal.moveto(-20, 0, 40, 40).wait_for_completed()
        robot_group.blaster.set_led(brightness=0, effect='off')
        time.sleep(0.2)
        robot_group.gimbal.moveto(20, 0, 40, 40).wait_for_completed()
        robot_group.blaster.set_led(brightness=255, effect='on')
    for i in range(0,3):
        robot_group.chassis.move(0,0,-45,0.5,90).wait_for_completed(0.5)
        robot_group.gimbal.moveto(-20, 0, 40, 40).wait_for_completed()
        robot_group.blaster.set_led(brightness=0, effect='off')
        time.sleep(0.2)
        robot_group.chassis.move(0,0,90,0.5,90).wait_for_completed(0.5)
        robot_group.gimbal.moveto(20, 0, 40, 40).wait_for_completed()
        robot_group.blaster.set_led(brightness=255, effect='on')

        robot_group.chassis.move(0,0,-45,0.5,90).wait_for_completed()
    robot_group.gimbal.moveto(0, 0, 180, 180).wait_for_completed()
    robot_group.led.set_led(led.COMP_ALL, 255, 0, 0, led.EFFECT_ON)

def task_10_blue(robot_group):
    robot_group.set_group_robots_mode(mode="free")
    robot_group.led.set_led(led.COMP_BOTTOM_ALL, 255, 255, 255, led.EFFECT_FLASH,5)
    robot_group.chassis.move(0,0,90,0.5,90)
    robot_group.gimbal.moveto(0, 90, 90, 45).wait_for_completed()
    robot_group.led.set_led(led.COMP_TOP_ALL, 0, 0, 255, led.EFFECT_SCROLLING)
    robot_group.led.set_led(led.COMP_BOTTOM_ALL, 0, 0, 255, led.EFFECT_ON)
    robot_group.gimbal.moveto(20, 0, 180, 180).wait_for_completed()
    for i in range(0,3):
        robot_group.gimbal.moveto(-20, 0, 40, 40).wait_for_completed()
        time.sleep(0.2)
        robot_group.gimbal.moveto(20, 0, 40, 40).wait_for_completed()
    for i in range(0,3):
        robot_group.gimbal.moveto(-20, 0, 40, 40).wait_for_completed()
        robot_group.blaster.set_led(brightness=0, effect='off')
        time.sleep(0.2)
        robot_group.gimbal.moveto(20, 0, 40, 40).wait_for_completed()
        robot_group.blaster.set_led(brightness=255, effect='on')
    for i in range(0,3):
        robot_group.chassis.move(0,0,45,0.5,90).wait_for_completed(0.5)
        robot_group.gimbal.moveto(-20, 0, 40, 40).wait_for_completed()
        robot_group.blaster.set_led(brightness=0, effect='off')
        time.sleep(0.2)
        robot_group.chassis.move(0,0,-90,0.5,90).wait_for_completed(0.5)
        robot_group.gimbal.moveto(20, 0, 40, 40).wait_for_completed()
        robot_group.blaster.set_led(brightness=255, effect='on')

        robot_group.chassis.move(0,0,45,0.5,90).wait_for_completed()
    robot_group.gimbal.moveto(0, 0, 180, 180).wait_for_completed()
    robot_group.led.set_led(led.COMP_ALL, 0, 0, 255, led.EFFECT_ON)
    
def task_11(robot_group):
    robot_group.set_group_robots_mode(mode="free")
    robot_group.led.set_led(led.COMP_ALL, 0, 0, 0, led.EFFECT_OFF)
    robot_group.gimbal.suspend()
    ep0=robot_group.get_robot(0)
    ep1=robot_group.get_robot(1)
    ep2=robot_group.get_robot(2)
    ep3=robot_group.get_robot(3)
    ep4=robot_group.get_robot(4)
    ep5=robot_group.get_robot(5)
    
    ep0.led.set_led(led.COMP_ALL, 0, 255, 55, led.EFFECT_FLASH,5)#第一组开始
    ep1.led.set_led(led.COMP_ALL, 0, 255, 55, led.EFFECT_FLASH,5)
    time.sleep(0.5)
    ep0.led.set_led(led.COMP_ALL, 255, 0, 0, led.EFFECT_ON)
    ep1.led.set_led(led.COMP_ALL, 0, 0, 255, led.EFFECT_ON)
    ep0.led.set_led(led.COMP_TOP_ALL, 255, 0, 0, led.EFFECT_BREATH)
    ep1.led.set_led(led.COMP_TOP_ALL, 0, 0, 255, led.EFFECT_BREATH)

    ep0.gimbal.resume()
    ep1.gimbal.resume()
    ep0.gimbal.moveto(0, 0, 180, 180)
    ep1.gimbal.moveto(0, 0, 180, 180)
    time.sleep(0.2)

    ep0.chassis.move(0,0,-45,0.5,90)
    ep1.chassis.move(0,0,45,0.5,90)
    time.sleep(0.2)
    ep0.gimbal.moveto(-20, -90, 90, 90)
    ep1.gimbal.moveto(-20, 90, 90, 90).wait_for_completed()
    ep0.led.set_led(led.COMP_TOP_ALL, 255, 0, 0, led.EFFECT_SCROLLING)
    ep1.led.set_led(led.COMP_TOP_ALL, 0, 0, 255, led.EFFECT_SCROLLING)   

    for i in range(0,3):#第一组机器人的动作
        ep0.blaster.set_led(brightness=255, effect='on')
        ep1.blaster.set_led(brightness=255, effect='on')
        ep0.gimbal.moveto(20, -45, 90, 90)
        ep1.gimbal.moveto(-20, 45, 90, 90).wait_for_completed()
        time.sleep(0.5)
        ep0.blaster.set_led(brightness=0, effect='off')
        ep1.blaster.set_led(brightness=0, effect='off')
        ep0.gimbal.moveto(-20, -45, 90, 90)
        ep1.gimbal.moveto(-20, 45, 90, 90).wait_for_completed()
    
    ep0.gimbal.moveto(0, 0, 90, 90)
    ep1.gimbal.moveto(0, 0, 90, 90)
    ep0.chassis.move(0,0,45,0.5,90)
    ep1.chassis.move(0,0,-45,0.5,90)#底盘归位

    robot_group.led.set_led(led.COMP_ALL, 0, 255, 55, led.EFFECT_FLASH,5)
    time.sleep(0.5)
    robot_group.led.set_led(led.COMP_ALL, 0, 255, 55, led.EFFECT_OFF)

    ep2.led.set_led(led.COMP_ALL, 255, 0, 0, led.EFFECT_BREATH)
    ep3.led.set_led(led.COMP_ALL, 0, 0, 255, led.EFFECT_BREATH)   
    ep0.gimbal.moveto(0, 90, 180, 180)
    ep1.gimbal.moveto(0, -90, 180, 180).wait_for_completed()

    ep0.chassis.move(1,0,0,0.5,90)
    ep1.chassis.move(-1,0,0,0.5,90).wait_for_completed()

    ep0.gimbal.moveto(0, 180, 180, 180)
    ep1.gimbal.moveto(0, -180, 180, 180).wait_for_completed()

    ep0.chassis.move(0,-1,0,0.5,90)#调整余下机器人位置
    ep1.chassis.move(0,-1,0,0.5,90).wait_for_completed(0.5)
    ep2.chassis.move(0,0.5,0,0.5,90)
    ep3.chassis.move(0,0.5,0,0.5,90)
    ep4.chassis.move(0,0.5,0,0.5,90)
    ep5.chassis.move(0,0.5,0,0.5,90).wait_for_completed()

    ep0.chassis.move(-0.5,0,0,0.5,90)#调整01机器人
    ep1.chassis.move(0.5,0,0,0.5,90)
    ep0.gimbal.suspend()
    ep1.gimbal.suspend()
    ep0.led.set_led(led.COMP_TOP_ALL, 0, 0, 0, led.EFFECT_OFF)
    ep1.led.set_led(led.COMP_TOP_ALL, 0, 0, 0, led.EFFECT_OFF)

    ep2.led.set_led(led.COMP_ALL, 0, 255, 55, led.EFFECT_FLASH,5)#第二组开始
    ep3.led.set_led(led.COMP_ALL, 0, 255, 55, led.EFFECT_FLASH,5)
    time.sleep(0.5)
    ep2.led.set_led(led.COMP_ALL, 255, 0, 0, led.EFFECT_ON)
    ep3.led.set_led(led.COMP_ALL, 0, 0, 255, led.EFFECT_ON)
    ep2.led.set_led(led.COMP_TOP_ALL, 255, 0, 0, led.EFFECT_BREATH)
    ep3.led.set_led(led.COMP_TOP_ALL, 0, 0, 255, led.EFFECT_BREATH)

    ep2.gimbal.resume()
    ep3.gimbal.resume()
    ep2.gimbal.moveto(0, 0, 180, 180)
    ep3.gimbal.moveto(0, 0, 180, 180)
    time.sleep(0.2)

    ep0.led.set_led(led.COMP_TOP_ALL, 255, 0, 0, led.EFFECT_SCROLLING)
    ep1.led.set_led(led.COMP_TOP_ALL, 0, 0, 255, led.EFFECT_SCROLLING)   

    for i in range(0,3):#第二组机器人的动作
        ep2.set_group_robots_mode(mode="gimbal_lead")
        ep3.set_group_robots_mode(mode="gimbal_lead")
        ep2.blaster.set_led(brightness=255, effect='on')
        ep3.blaster.set_led(brightness=255, effect='on')
        ep2.gimbal.moveto(20, -45, 90, 90)
        ep3.gimbal.moveto(20, 45, 90, 90).wait_for_completed()
        time.sleep(0.5)
        ep2.gimbal.moveto(-20, 0, 90, 90)
        ep3.gimbal.moveto(-20, 0, 90, 90).wait_for_completed()
        time.sleep(0.5)
        ep2.gimbal.moveto(20, 45, 90, 90)
        ep3.gimbal.moveto(20, -45, 90, 90).wait_for_completed()
        time.sleep(0.5)
        ep2.gimbal.moveto(0, 0, 90, 90)
        ep3.gimbal.moveto(0, 0, 90, 90).wait_for_completed()
        time.sleep(0.5)

    ep2.blaster.set_led(brightness=0, effect='off')
    ep3.blaster.set_led(brightness=0, effect='off')
    ep2.set_group_robots_mode(mode="free")
    ep3.set_group_robots_mode(mode="free")

    robot_group.led.set_led(led.COMP_ALL, 0, 255, 55, led.EFFECT_FLASH,5)
    time.sleep(0.5)
    robot_group.led.set_led(led.COMP_ALL, 0, 255, 55, led.EFFECT_OFF)

    ep4.led.set_led(led.COMP_ALL, 255, 0, 0, led.EFFECT_BREATH)
    ep5.led.set_led(led.COMP_ALL, 0, 0, 255, led.EFFECT_BREATH)   
    ep2.gimbal.moveto(0, 90, 180, 180)
    ep3.gimbal.moveto(0, -90, 180, 180).wait_for_completed()

    ep2.chassis.move(1,0,0,0.5,90)
    ep3.chassis.move(-1,0,0,0.5,90).wait_for_completed()

    ep2.gimbal.moveto(0, 180, 180, 180)
    ep3.gimbal.moveto(0, -180, 180, 180).wait_for_completed()

    ep2.chassis.move(0,-1,0,0.5,90)#调整余下机器人位置
    ep3.chassis.move(0,-1,0,0.5,90).wait_for_completed(0.5)
    ep4.chassis.move(0,0.5,0,0.5,90)
    ep5.chassis.move(0,0.5,0,0.5,90)
    ep0.chassis.move(0,0.5,0,0.5,90)
    ep1.chassis.move(0,0.5,0,0.5,90).wait_for_completed()

    ep2.chassis.move(-0.5,0,0,0.5,90)#调整23机器人
    ep3.chassis.move(0.5,0,0,0.5,90)
    ep2.gimbal.suspend()
    ep3.gimbal.suspend()
    ep2.led.set_led(led.COMP_TOP_ALL, 0, 0, 0, led.EFFECT_OFF)
    ep3.led.set_led(led.COMP_TOP_ALL, 0, 0, 0, led.EFFECT_OFF)

    ep4.led.set_led(led.COMP_ALL, 0, 255, 55, led.EFFECT_FLASH,5)#第三组开始
    ep5.led.set_led(led.COMP_ALL, 0, 255, 55, led.EFFECT_FLASH,5)
    time.sleep(0.5)
    ep4.led.set_led(led.COMP_ALL, 255, 0, 0, led.EFFECT_ON)
    ep5.led.set_led(led.COMP_ALL, 0, 0, 255, led.EFFECT_ON)
    ep4.led.set_led(led.COMP_TOP_ALL, 255, 0, 0, led.EFFECT_BREATH)
    ep5.led.set_led(led.COMP_TOP_ALL, 0, 0, 255, led.EFFECT_BREATH)

    ep4.gimbal.resume()
    ep5.gimbal.resume()
    ep4.gimbal.moveto(0, 0, 180, 180)
    ep5.gimbal.moveto(0, 0, 180, 180)
    time.sleep(0.2)

    ep4.led.set_led(led.COMP_TOP_ALL, 255, 0, 0, led.EFFECT_SCROLLING)
    ep5.led.set_led(led.COMP_TOP_ALL, 0, 0, 255, led.EFFECT_SCROLLING)   

    for i in range(0,3):#第三组机器人的动作
        ep4.set_group_robots_mode(mode="chassis_lead")
        ep5.set_group_robots_mode(mode="chassis_lead")
        ep4.chassis.move(0,0,180,0.5,90)
        ep5.chassis.move(0,0,-180,0.5,90).wait_for_completed(1.5)
        ep4.blaster.set_led(brightness=255, effect='on')
        ep5.blaster.set_led(brightness=255, effect='on')
        ep4.gimbal.moveto(20, 0, 90, 90)
        ep5.gimbal.moveto(20, 0, 90, 90).wait_for_completed()
        
        time.sleep(0.5)
        ep4.chassis.move(0,0,-180,0.5,90)
        ep5.chassis.move(0,0,180,0.5,90).wait_for_completed(1.5)
        ep4.gimbal.moveto(-20, 0, 90, 90)
        ep5.gimbal.moveto(-20, 0, 90, 90).wait_for_completed()
        time.sleep(0.5)
        ep4.chassis.move(0,0,180,0.5,90)
        ep5.chassis.move(0,0,-180,0.5,90).wait_for_completed(1.5)
        ep4.gimbal.moveto(20, 0, 90, 90)
        ep5.gimbal.moveto(20, 0, 90, 90).wait_for_completed()
        time.sleep(0.5)
        ep4.chassis.move(0,0,-180,0.5,90)
        ep5.chassis.move(0,0,180,0.5,90).wait_for_completed(1.5)
        ep4.gimbal.moveto(0, 0, 90, 90)
        ep5.gimbal.moveto(0, 0, 90, 90).wait_for_completed()
        time.sleep(0.5)

    ep4.blaster.set_led(brightness=0, effect='off')
    ep5.blaster.set_led(brightness=0, effect='off')
    ep4.set_group_robots_mode(mode="free")
    ep5.set_group_robots_mode(mode="free")

    robot_group.led.set_led(led.COMP_ALL, 0, 255, 55, led.EFFECT_FLASH,5)
    time.sleep(0.5)
    robot_group.led.set_led(led.COMP_ALL, 0, 255, 55, led.EFFECT_OFF)

    ep0.led.set_led(led.COMP_ALL, 255, 0, 0, led.EFFECT_BREATH)
    ep1.led.set_led(led.COMP_ALL, 0, 0, 255, led.EFFECT_BREATH)   
    ep4.gimbal.moveto(0, 90, 180, 180)
    ep5.gimbal.moveto(0, -90, 180, 180).wait_for_completed()

    ep4.chassis.move(1,0,0,0.5,90)
    ep5.chassis.move(-1,0,0,0.5,90).wait_for_completed()

    ep4.gimbal.moveto(0, 180, 180, 180)
    ep5.gimbal.moveto(0, -180, 180, 180).wait_for_completed()

    ep4.chassis.move(0,-1,0,0.5,90)#调整余下机器人位置
    ep5.chassis.move(0,-1,0,0.5,90).wait_for_completed(0.5)
    ep0.chassis.move(0,0.5,0,0.5,90)
    ep1.chassis.move(0,0.5,0,0.5,90)
    ep2.chassis.move(0,0.5,0,0.5,90)
    ep3.chassis.move(0,0.5,0,0.5,90).wait_for_completed()

    ep4.chassis.move(-0.5,0,0,0.5,90)#调整45机器人
    ep5.chassis.move(0.5,0,0,0.5,90)
    ep4.gimbal.suspend()
    ep5.gimbal.suspend()
    ep4.led.set_led(led.COMP_TOP_ALL, 0, 0, 0, led.EFFECT_OFF)
    ep5.led.set_led(led.COMP_TOP_ALL, 0, 0, 0, led.EFFECT_OFF)

    robot_group.gimbal.resume()
    robot_group.gimbal.moveto(0, 0, 180, 180)
    robot_group.blaster.set_led(brightness=0, effect='off')
    robot_group.led.set_led(led.COMP_ALL, 0, 0, 0, led.EFFECT_OFF)