import sys
import tty, termios
from pymorse import Morse
import time
from collections import defaultdict

def printer(data):
	print("Incoming data! " + str(data))
	file_obj = open ("test.txt", "w+")
	file_obj.write(data)
	file_obj.close

def getchar():


	fd = sys.stdin.fileno()
	old_settings = termios.tcgetattr(fd)
	try:
		tty.setraw(sys.stdin.fileno())
		ch = sys.stdin.read(1)
	finally:
		termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
	return ch
def main():
	position = defaultdict(list)
	parts = defaultdict()
	parts = {'BASE_1_IN_L_': 'base', 'LINK1_1_IN_L_': 'link_1','LINK2_1_IN_L_': 'link_2','ENDEFF_1_IN_L_': 'endeff','OPERATOR_1_ARM_AREA_IN_L_': 'arm', 'OPERATOR_1_HEAD_AREA_IN_L_': 'head'}
#dealing with time = 0
	for p in parts:
		position[parts[p]].append('0')
#

	with open('output.hist.txt', 'r') as f_orig:
		i = 0
		for line in f_orig:
			if (i > 1):
				for p in parts:
					if p in line:
						position[parts[p]].append(line[-2:])
			if "------ time" in line:
				i += 1

	A=[position['link_1'], position['link_2'], position['base'], position['arm'], position['head'], position['endeff']]

	k=0
	n=len(A)
	m=len(A[0])
	x=0
	y=0
	z=0
	t=0	
	print(A)

	with Morse("localhost", 4000)  as simu:
				
		esc= 0

		while not esc:
			c = getchar()
			tinitial = [0.0, 0.0, 1.0]
			t1_2 = [0.4, 0.0, 0.0]
			t1_3 = [0.3, -0.5, 0.05]
			t1_5 = [0.5, -0.2, 0.3]
			t2_1 = [-0.4, 0.0, 0.0]
			t2_3 = [-0.15, -0.5, 0.05]
			t2_5 = [0.1, -0.2, 0.3]
			t3_1 = [-0.3, 0.5, -0.05]
			t3_2 = [0.15, 0.5, -0.05]
			t3_4 = [-0.25, 1.0, 0.2]
			t3_5 = [0.25, 0.3, 0.25]
			t3_6 = [-0.25, 0.0, 1.15]
			t4_3_1 = [0.25, -1.0, 0.0]
			t4_3_2 = [0.0, 0.0, -0.2]
			t4_5 = [0.65, -0.55, 0.25]
			t4_6 = [0.0, -0.95, 0.95]
			t4_8 = [0.0, -0.2, 0.2]
			t5_1 = [-0.5, 0.2, -0.3]
			t5_2 = [-0.1, 0.2, -0.3]
			t5_3 = [-0.25, -0.3, -0.25]
			t5_4 = [-0.65, 0.55, -0.25]
			t5_6 = [-0.75, -0.45, 0.5]
			t6_3 = [0.25, 0.0, -1.15]
			t6_4 = [0.0, 0.95, -0.95]
			t6_5 = [0.75, 0.45, -0.5]
			t6_8 = [0.0, 0.85, -0.6]
			t8_4 = [0.0, 0.2, -0.2]
			t8_6 = [0.0, -0.85, 0.6]
			rinitial = [0.0, 0.0, 0.0]
			r1 = [3.14, 0.0, 0.0]
			r2 = [-3.14, 0.0, 0.0]
			o1_3_1 = [0.0, 1.25]
			o1_3_2 = [0.4, 0.0]
			o1_4_h5 = [-1.2, 0.0]
			o1_4_h4 = [-1.0, 0.0]
			o1_5 = [-2.0, 0.0]
			o2_1 = [1.5, 0.0]
			o2_3_1 = [0.0, 1.25]
			o2_3_2 = [0.4, 0.0]
			o2_4_h5 = [0.3, 0.0]
			o2_4_h4 = [0.5, 0.0]
			o2_5 = [-0.5, 0.0]
			o3_1_1 = [0.0, -1.25]
			o3_1_2 = [1.5, 0.0]
			o3_2 = [0.0, -1.25]
			o3_4_h5_1 = [0.0, -1.25]
			o3_4_h5_2 = [0.3, 0.0]
			o3_4_h4_1 = [0.0, -1.25]
			o3_4_h4_2 = [0.5, 0.0]
			o3_5_1 = [0.0, -1.25]
			o3_5_2 = [-0.5, 0.0]
			o3_6 = [-0.3, 0.0]
			o4_h5_1 = [1.2, 0.0]
			o4_h4_1 = [1.0, 0.0]
			o4_h4h5_3_1 = [0.0, 1.25]
			o4_h4h5_3_2 = [0.4, 0.0]
			o4_h5_5 = [-0.8, 0.0]
			o4_h4_5 = [-1.0, 0.0]
			o4_h4h5_6_1 = [0.0, 1.25]
			o4_h4h5_6_2 = [0.1, 0.0]
			o4_h4_7 = [-1.3, 0.0]
			o4_h5_7 = [-1.1, 0.0]
			o5_1 = [2.0, 0.0]
			o5_3_1 = [0.0, 1.25]
			o5_3_1 = [0.4, 0.0]
			o5_4_h4 = [1.0, 0.0]
			o5_4_h5 = [0.8, 0.0]
			o5_6_1 = [0.0, 1.25]
			o5_6_2 = [0.1, 0.0]
			o5_7 = [-0.3, 0.0]
			o6_3 = [0.3, 0.0]
			o6_4_h4_1 = [0.0, -1.25]
			o6_4_h4_2 = [0.1, 0.0]
			o6_4_h5_1 = [0.0, -1.25]
			o6_4_h5_2 = [0.3, 0.0]
			o6_5_1 = [0.0, -1.25]
			o6_5_2 = [-0.5, 0.0]
			o7_4_h4 = [1.3, 0.0]
			o7_4_h5 = [1.1, 0.0]
			o7_5 = [0.3, 0.0] 
			name= "ik_target.robot.arm.kuka_7"	
			time.sleep(2)
			simu.rpc('robot.arm', 'place_IK_target', name, tinitial, rinitial) #it initializes the robot at position 6	

			if (c == "7"):
				while (k>=0) and (k<=(m-2)):
					time.sleep(2) #in each time interval, it waits for 2 seconds to ensure the completion of movement
					if A[5][k]=='1\n':
						if A[5][k+1]=='2\n':
							print("Robot's end effector moves from 1 to 2")
							simu.rpc('robot.arm', 'place_IK_target', name, t1_2)
						elif A[5][k+1]=='3\n':
							print("Robot's end effector moves from 1 to 3")
							simu.rpc('robot.arm', 'place_IK_target', name, t1_3)
							y=y+1
						elif A[5][k+1]=='5\n':
							print("Robot's end effector moves from 1 to 5")
							simu.rpc('robot.arm', 'place_IK_target', name, t1_5)
						elif A[5][k+1]=='1\n':
							print("Stay at 1")
					elif A[5][k]=='2\n':
						if A[5][k+1]=='1\n':
							print("Robot's end effector moves from 2 to 1")
							simu.rpc('robot.arm', 'place_IK_target', name, t2_1)
						elif A[5][k+1]=='3\n':
							print("Robot's end effector moves from 2 to 3")
							simu.rpc('robot.arm', 'place_IK_target', name, t2_3)
							y=y+1
						elif A[5][k+1]=='5\n':
							print("Robot's end effector moves from 2 to 5")
							simu.rpc('robot.arm', 'place_IK_target', name, t2_5)
						elif A[5][k+1]=='2\n':
							print("Robot stays at 2")
					elif A[5][k]=='3\n':
						if A[5][k+1]=='1\n':
							print("Robot's end effector moves from 3 to 1")
							simu.rpc('robot.arm', 'place_IK_target', name, t3_1)
						elif A[5][k+1]=='2\n':
							print("Robot's end effector moves from 3 to 2")
							simu.rpc('robot.arm', 'place_IK_target', name, t3_2)
						elif A[5][k+1]=='4\n':
							print("Robot's end effector moves from 3 to 4")
							simu.rpc('robot.arm', 'place_IK_target', name, t3_4)
							x=x+1
						elif A[5][k+1]=='5\n':
							print("Robot's end effector moves from 3 to 5")
							simu.rpc('robot.arm', 'place_IK_target', name, t3_5)
						elif A[5][k+1]=='6\n':
							print("Robot's end effector moves from 3 to 6")
							simu.rpc('robot.arm', 'place_IK_target', name, t3_6, r2)
						elif A[5][k+1]=='3\n':
							print("Robot stays at 3")					
					elif A[5][k]=='4\n':
						if A[5][k+1]=='3\n':
							print("Robot's end effector moves from 4 to 3")
							simu.rpc('robot.arm', 'place_IK_target', name, t4_3_1)
							time.sleep(2)
							simu.rpc('robot.arm', 'place_IK_target', name, t4_3_2) #from 4 to 3, we need 2 different movements, otherwise the robot touches the material
							y=y+1
						elif A[5][k+1]=='5\n':
							print("Robot's end effector moves from 4 to 5")
							simu.rpc('robot.arm', 'place_IK_target', name, t4_5)
						elif A[5][k+1]=='6\n':
							print("Robot's end effector moves from 4 to 6")
							simu.rpc('robot.arm', 'place_IK_target', name, t4_6, r2)
						elif A[5][k+1]=='8\n':
							print("Robot's end effector moves from 4 to 8")
							simu.rpc('robot.arm', 'place_IK_target', name, t4_8)
						elif A[5][k+1]=='4\n':
							print("Robot stays at 4")
					elif A[5][k]=='5\n':
						if A[5][k+1]=='1\n':
							print("Robot's end effector moves from 5 to 1")
							simu.rpc('robot.arm', 'place_IK_target', name, t5_1)
						elif A[5][k+1]=='2\n':
							print("Robot's end effector moves from 5 to 2")
							simu.rpc('robot.arm', 'place_IK_target', name, t5_2)
						elif A[5][k+1]=='3\n':
							print("Robot's end effector moves from 5 to 3")
							simu.rpc('robot.arm', 'place_IK_target', name, t5_3)
							y=y+1
						elif A[5][k+1]=='4\n':
							print("Robot's end effector moves from 5 to 4")
							simu.rpc('robot.arm', 'place_IK_target', name, t5_4)
							x=x+1
						elif A[5][k+1]=='5\n':
							print("Robot stays at 5")
						elif A[5][k+1]=='6\n':
							print("Robot's end effector moves from 5 to 6")
							simu.rpc('robot.arm', 'place_IK_target', name, t5_6, r2)
					elif A[5][k]=='6\n' or A[5][k]=='0':
						if A[5][k+1]=='3\n':
							print("Robot's end effector moves from 6 to 3")
							simu.rpc('robot.arm', 'place_IK_target', name, t6_3, r1)
							y=y+1
						elif A[5][k+1]=='4\n':
							print("Robot's end effector moves from 6 to 4")
							simu.rpc('robot.arm', 'place_IK_target', name, t6_4, r1)
							x=x+1
						elif A[5][k+1]=='5\n':
							print("Robot's end effector moves from 6 to 5")
							simu.rpc('robot.arm', 'place_IK_target', name, t6_5, r1)
						elif A[5][k+1]=='8\n':
							print("Robot's end effector moves from 6 to 8")
							simu.rpc('robot.arm', 'place_IK_target', name, t6_8, r1)
						elif A[5][k+1]=='6\n':
							print("Robot stays at 6")
					elif A[5][k]=='8\n':
						if A[5][k+1]=='4\n':
							print("Robot's end effector moves from 8 to 4")
							simu.rpc('robot.arm', 'place_IK_target', name, t8_4)
							x=x+1
						elif A[5][k+1]=='6\n':
							print("Robot's end effector moves from 8 to 6")
							simu.rpc('robot.arm', 'place_IK_target', name, t8_6)
						elif A[5][k+1]=='8\n':
							print("Robot stays at 8")
					if y==1 and t!=1:
						time.sleep(2) #waits for 2 seconds to ensure that robot's movement has finished and then starts to grab
						print("Robot grabs the material")
						simu.rpc('robot.arm.gripper', 'grab')
						t=1 #it means that robot grabbed a material
					if x>=1 and t==1 and z!=1: 
#it came to position 4 (x>=1), it grabbed something before coming to position 4 (t=1), it did not release anything before (z!=1)
						time.sleep(2) #waits for 2 seconds to ensure that robot's movement has finished and then starts to release the material
						print("Robot releases the material")
						simu.rpc('robot.arm.gripper', 'release')
						z=1 #it means that robot released a material
					
					if A[3][k]=='1\n':
						if A[3][k+1]=='2\n':
							print("Operator's arm moves from 1 to 2")
							simu.rpc('human', 'toggle_manipulation')
						elif A[3][k+1]=='3\n':
							print("Operator's arm moves from 1 to 3")
							simu.rpc('human', 'toggle_manipulation')
							time.sleep(2)
							simu.rpc('human', 'move', o1_3_1[0], o1_3_1[1])
							time.sleep(2)
							simu.rpc('human', 'toggle_manipulation')
							time.sleep(2)
							simu.rpc('human', 'move_hand', o1_3_2[0], o1_3_2[1])
						elif A[3][k+1]=='4\n' and A[4][k+1]=='5\n':
							print("Operator's arm moves from 1 to 4")
							simu.rpc('human', 'move_hand', o1_4_h5[0], o1_4_h5[1])
						elif A[3][k+1]=='4\n' and A[4][k+1]=='4\n':
							print("Operator's arm moves from 1 to 4 and Operator's head moves from 5 to 4")
							simu.rpc('human', 'move_hand', o1_4_h4[0], o1_4_h4[1])
						elif A[3][k+1]=='5\n':
							print("Operator's arm moves from 1 to 5")
							simu.rpc('human', 'move_hand', o1_5[0], o1_5[1])
						elif A[3][k+1]=='1\n':
							print("Operators arm stays at 1")
					elif A[3][k]=='2\n' or A[3][k]=='0':
						if A[3][k+1]=='1\n':
							print("Operator's arm moves from 2 to 1")
							simu.rpc('human', 'toggle_manipulation')
							time.sleep(2)
							simu.rpc('human', 'move_hand', o2_1[0], o2_1[1])
						elif A[3][k+1]=='3\n':
							print("Operator's arm moves from 2 to 3")
							simu.rpc('human', 'move', o2_3_1[0], o2_3_1[1])
							time.sleep(2)
							simu.rpc('human', 'toggle_manipulation')
							time.sleep(2)
							simu.rpc('human', 'move_hand', o2_3_2[0], o2_3_2[1])
						elif A[3][k+1]=='4\n' and A[4][k+1]=='5\n':
							print("Operator's arm moves from 2 to 4")
							simu.rpc('human', 'toggle_manipulation')
							time.sleep(2)
							simu.rpc('human', 'move_hand', o2_4_h5[0], o2_4_h5[1])
						elif A[3][k+1]=='4\n' and A[4][k+1]=='4\n':
							print("Operator's arm moves from 2 to 4 and Operator's head moves from 5 to 4")
							simu.rpc('human', 'toggle_manipulation')
							time.sleep(2)
							simu.rpc('human', 'move_hand', o2_4_h4[0], o2_4_h4[1])
						elif A[3][k+1]=='5\n':
							print("Operator's arm moves from 2 to 5")
							simu.rpc('human', 'toggle_manipulation')
							time.sleep(2)
							simu.rpc('human', 'move_hand', o2_5[0], o2_5[1])
						elif A[3][k+1]=='2\n':
							print("Operator's arm stays at 2")
					elif A[3][k]=='3\n':
						if A[3][k+1]=='1\n':
							print("Operator's arm moves from 3 to 1")
							simu.rpc('human', 'toggle_manipulation')
							time.sleep(2)
							simu.rpc('human', 'move', o3_1_1[0], o3_1_1[1])
							time.sleep(2)
							simu.rpc('human', 'toggle_manipulation')
							time.sleep(2)
							simu.rpc('human', 'move_hand', o3_1_2[0], o3_1_2[1])
						elif A[3][k+1]=='2\n':
							print("Operator's arm moves from 3 to 2")
							simu.rpc('human', 'toggle_manipulation')
							time.sleep(2)
							simu.rpc('human', 'move', o3_2[0], o3_2[1])
						elif A[3][k+1]=='4\n' and A[4][k+1]=='5\n':
							print("Operator's arm moves from 3 to 4")
							simu.rpc('human', 'toggle_manipulation')
							time.sleep(2)
							simu.rpc('human', 'move', o3_4_h5_1[0], o3_4_h5_1[1])
							time.sleep(2)
							simu.rpc('human', 'toggle_manipulation')
							time.sleep(2)
							simu.rpc('human', 'move_hand', o3_4_h5_2[0], o3_4_h5_2[1])
						elif A[3][k+1]=='4\n' and A[4][k+1]=='4\n':
							print("Operator's arm moves from 3 to 4 and Operator's head moves from 5 to 4")
							simu.rpc('human', 'toggle_manipulation')
							time.sleep(2)
							simu.rpc('human', 'move', o3_4_h4_1[0], o3_4_h4_1[1])
							time.sleep(2)
							simu.rpc('human', 'toggle_manipulation')
							time.sleep(2)
							simu.rpc('human', 'move_hand', o3_4_h4_2[0], o3_4_h4_2[1])
						elif A[3][k+1]=='5\n':
							print("Operator's arm moves from 3 to 5")
							simu.rpc('human', 'toggle_manipulation')
							time.sleep(2)
							simu.rpc('human', 'move', o3_5_1[0], o3_5_1[1])
							time.sleep(2)
							simu.rpc('human', 'toggle_manipulation')
							time.sleep(2)
							simu.rpc('human', 'move_hand', o3_5_2[0], o3_5_2[1])
						elif A[3][k+1]=='6\n':
							print("Operator's arm moves from 3 to 6")
							simu.rpc('human', 'move_hand', o3_6[0], o3_6[1])
						elif A[3][k+1]=='3\n':
							print("Operator's arm stays at 3")
					elif A[3][k]=='4\n' and A[4][k]=='5\n':
						if A[3][k+1]=='1\n':
							print("Operator's arm moves from 4 to 1")
							simu.rpc('human', 'move_hand', o4_h5_1[0], o4_h5_1[1])
						elif A[3][k+1]=='3\n':
							print("Operator's arm moves from 4 to 3")
							simu.rpc('human', 'toggle_manipulation')
							time.sleep(2)
							simu.rpc('human', 'move', o4_h4h5_3_1[0], o4_h4h5_3_1[1])
							time.sleep(2)
							simu.rpc('human', 'toggle_manipulation')
							time.sleep(2)
							simu.rpc('human', 'move_hand', o4_h4h5_3_2[0], o4_h4h5_3_2[1])
						elif A[3][k+1]=='5\n':
							print("Operator's arm moves from 4 to 5")
							simu.rpc('human', 'move_hand', o4_h5_5[0], o4_h5_5[1])
						elif A[3][k+1]=='6\n':
							print("Operator's arm moves from 4 to 6")
							simu.rpc('human', 'toggle_manipulation')
							time.sleep(2)
							simu.rpc('human', 'move', o4_h4h5_6_1[0], o4_h4h5_6_1[1])
							time.sleep(2)
							simu.rpc('human', 'toggle_manipulation')
							time.sleep(2)
							simu.rpc('human', 'move_hand', o4_h4h5_6_2[0], o4_h4h5_6_2[1])
						elif A[3][k+1]=='7\n':
							print("Operator's arm moves from 4 to 7")
							simu.rpc('human', 'move_hand', o4_h5_7[0], o4_h5_7[1])
						elif A[3][k+1]=='4\n':
							print("Operator's arm stays at 4")
					elif A[3][k]=='4\n' and A[4][k]=='4\n':
						if A[3][k+1]=='1\n':
							print("Operator's arm moves from 4 to 1")
							simu.rpc('human', 'move_hand', o4_h4_1[0], o4_h4_1[1])
						elif A[3][k+1]=='3\n':
							print("Operator's arm moves from 4 to 3")
							simu.rpc('human', 'toggle_manipulation')
							time.sleep(2)
							simu.rpc('human', 'move', o4_h4h5_3_1[0], o4_h4h5_3_1[1])
							time.sleep(2)
							simu.rpc('human', 'toggle_manipulation')
							time.sleep(2)
							simu.rpc('human', 'move_hand', o4_h4h5_3_2[0], o4_h4h5_3_2[1])
						elif A[3][k+1]=='5\n':
							print("Operator's arm moves from 4 to 5")
							simu.rpc('human', 'move_hand', o4_h4_5[0], o4_h4_5[1])
						elif A[3][k+1]=='6\n':
							print("Operator's arm moves from 4 to 6")
							simu.rpc('human', 'toggle_manipulation')
							time.sleep(2)
							simu.rpc('human', 'move', o4_h4h5_6_1[0], o4_h4h5_6_1[1])
							time.sleep(2)
							simu.rpc('human', 'toggle_manipulation')
							time.sleep(2)
							simu.rpc('human', 'move_hand', o4_h4h5_6_2[0], o4_h4h5_6_2[1])
						elif A[3][k+1]=='7\n':
							print("Operator's arm moves from 4 to 7")
							simu.rpc('human', 'move_hand', o4_h4_7[0], o4_h4_7[1])
						elif A[3][k+1]=='4\n':
							print("Operator's arm stays at 4")	
					elif A[3][k]=='5\n':
						if A[3][k+1]=='1\n':
							print("Operator's arm moves from 5 to 1")
							simu.rpc('human', 'move_hand', o5_1[0], o5_1[1])
						elif A[3][k+1]=='2\n':
							print("Operator's arm moves from 5 to 2")
							simu.rpc('human', 'toggle_manipulation')
						elif A[3][k+1]=='3\n':
							print("Operator's arm moves from 5 to 3")
							simu.rpc('human', 'toggle_manipulation')
							time.sleep(2)
							simu.rpc('human', 'move', o5_3_1[0], o5_3_1[1])
							time.sleep(2)
							simu.rpc('human', 'toggle_manipulation')
							time.sleep(2)
							simu.rpc('human', 'move_hand', o5_3_2[0], o5_3_2[1])
						elif A[3][k+1]=='4\n' and A[4][k+1]=='5\n':
							print("Operator's arm moves from 5 to 4")
							simu.rpc('human', 'move_hand', o5_4_h5[0], o5_4_h5[1])
						elif A[3][k+1]=='4\n' and A[4][k+1]=='4\n':
							print("Operator's arm moves from 5 to 4 and Operator's head moves to 4")
							simu.rpc('human', 'move_hand', o5_4_h4[0], o5_4_h4[1])
						elif A[3][k+1]=='6\n':
							print("Operator's arm moves from 5 to 6")
							simu.rpc('human', 'toggle_manipulation')
							time.sleep(2)
							simu.rpc('human', 'move', o5_6_1[0], o5_6_1[1])
							time.sleep(2)
							simu.rpc('human', 'toggle_manipulation')
							time.sleep(2)
							simu.rpc('human', 'move_hand', o5_6_2[0], o5_6_2[1])
						elif A[3][k+1]=='7\n':
							print("Operator's arm moves from 5 to 7")
							simu.rpc('human', 'move_hand', o5_7[0], o5_7[1])
						elif A[3][k+1]=='5\n':
							print("Operator's arm stays at 5")
					elif A[3][k]=='6\n':
						if A[3][k+1]=='3\n':
							print("Operator's arm moves from 6 to 3")
							simu.rpc('human', 'move_hand', o6_3[0], o6_3[1])
						elif A[3][k+1]=='4\n' and A[4][k+1]=='5\n':
							print("Operator's arm moves from 6 to 4")
							simu.rpc('human', 'toggle_manipulation')
							time.sleep(2)
							simu.rpc('human', 'move', o6_4_h5_1[0], o6_4_h5_1[1])
							time.sleep(2)
							simu.rpc('human', 'toggle_manipulation')
							time.sleep(2)
							simu.rpc('human', 'move_hand', o6_4_h5_2[0], o6_4_h5_2[1])
						elif A[3][k+1]=='4\n' and A[4][k+1]=='4\n':
							print("Operator's arm moves from 6 to 4")
							simu.rpc('human', 'toggle_manipulation')
							time.sleep(2)
							simu.rpc('human', 'move', o6_4_h4_1[0], o6_4_h4_1[1])
							time.sleep(2)
							simu.rpc('human', 'toggle_manipulation')
							time.sleep(2)
							simu.rpc('human', 'move_hand', o6_4_h4_2[0], o6_4_h4_2[1])
						elif A[3][k+1]=='5\n':
							print("Operator's arm moves from 6 to 5")
							simu.rpc('human', 'toggle_manipulation')
							time.sleep(2)
							simu.rpc('human', 'move', o6_5_1[0], o6_5_1[1])
							time.sleep(2)
							simu.rpc('human', 'toggle_manipulation')
							time.sleep(2)
							simu.rpc('human', 'move_hand', o6_5_2[0], o6_5_2[1])
						elif A[3][k+1]=='6\n':
							print("Operator's arm stays at 6")
					elif A[3][k]=='7\n':
						if A[3][k+1]=='4\n' and A[4][k+1]=='5\n':
							print("Operator's arm moves from 7 to 4")
							simu.rpc('human', 'move_hand', o7_4_h5[0], o7_4_h5[1])
						elif A[3][k+1]=='4\n' and A[4][k+1]=='4\n':
							print("Operator's arm moves from 7 to 4")
							simu.rpc('human', 'move_hand', o7_4_h4[0], o7_4_h4[1])
						elif A[3][k+1]=='5\n':
							print("Operator's arm moves from 7 to 5")
							simu.rpc('human', 'move_hand', o7_5[0], o7_5[1])
						elif A[3][k+1]=='7\n':
							print("Operator's arm stays at 7")
					k=k+1
			elif (c == "0"):
				pose = simu.robot.arm.armpose
				print(pose.get_state())
				pose.subscribe(printer)
				simu.sleep(2)
		

			if c == "q":
				esc = 1
main()
