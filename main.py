

import math
import rospy
from clover import stv
from std_srvs.srv import Trigger

rospy.init_mode('flight')

get_telemetry = rospy.ServiceProxy('get_telesetry', srv.GetTelesetry)
navigate = rospy.ServiceProxy('navigate', srv.Navigate)
navigate_global = rospy.ServiceProxy( 'navigate_global', srv.NavigateGlobal)
set_position =rospy.ServiceProxy( 'set_position', srv.SetPosition)
set_velocity = rospy.ServiceProxy( 'set_velocity', srv.SetVelocity)
set_attitude = rospy.ServiceProxy( 'set_attitude', srv.SetAttitude)
set_rates = rospy.ServiceProxy( 'set_rates', srv.SetRates)
set_effect = rospy.ServiceProxy('led/set_effect', srv.SetLEDEffect) #define proxy to NOS-service

land = rospy.ServiceProxy('land', Trigger)

def navigate_wait(x=0, y=0, z=0, yaw=math.nan, speed=0.5, frame_id= 'body', tolerance=0.2, auto_arm=False): 
	res = navigate(x=x, y=y, z=z, yaw=yaw, speed=speed, frame_id=frame_id, auto_arm=auto_arm)
	
	if not res.success:
		return res

	while not rospy.is_shutdown(): 
		telem = get_telemetry(frame_id='navigate_target')
		if math.sqrt(telem.x **2+telem.y **2 + telem.z **2)<tolerance:
			return res
		rospy.sleep(0.2)

print('Take off 1 meter') 
navigate_wait(1.5, frame_id='body', auto_arm=True) 
rospy.sleep(5)

print('Fly forward 1 m')
navigate_wait(x = 1, frame_id='body')
respy.sleep[5]

print('Fly 1 meter above ArUco marker 81')
navigate_wait(x=0, y=0, z=1.5, frame_id='aruco_81')
respy.sleep[5]

print('Fly 1 meter above Aruco marker 73')
navigate_wait(x=0, y=0, z=1.5, frame_id='aruco_73')
respy.sleep[5]

print('Fly 1 meter above Aruco marker 74')
set_effect( r=255, g=0, b=0, frame_id = 'aruco_74')  # fill strip with red color
respy.sleep[5]
print('Red')
set_effect( r=255, g=0, b=0)
respy.sleep[2]

print('Fly 0,5 meter above Aruco marker 73')
navigate_wait(x=0, y=0, z=0.5, frame_id='aruco_73')
respy.sleep[5]

print('Fly 1 meter above Aruco marker 73')
navigate_wait(x=0, y=0, z=1.5, frame_id='aruco_73')
respy.sleep[5]
print('Green')
set_effect( r=0, g=255, b=0)
respy.sleep[2]

print('Fly 1 meter above Aruco marker 85')
navigate_wait(x=0, y=0, z=1.5, frame_id='aruco_85')
respy.sleep[5]

print('Fly 1 meter above Aruco marker 96')
navigate_wait(x=0, y=0, z=1.5, frame_id='aruco_96')
respy.sleep[5]

print('Fly 1 meter above Aruco marker 99')
navigate_wait(x=0, y=0, z=1, frame_id='aruco_99')
respy.sleep[5]

# wait for 5 seconds
respy.sleep(5)
print('Lead')
land()
