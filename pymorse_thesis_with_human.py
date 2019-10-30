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
	z=0
	t=0
	print(A)

	with Morse("localhost", 4000)  as simu:

		esc= 0

		while not esc:
			c = getchar()
			tinitial = [0.0, 0.0, 1.0]
			robot_moves = {
			"0":{"3\n" : [0.25, 0.0, -1.15], "4\n" : [0.0, 0.95, -0.95], "5\n" :[0.75, 0.45, -0.5] ,"8\n" : [0.0, 0.85, -0.6]},
			"1\n" : {"2\n":[0.4, 0.0, 0.0] , "3\n":[0.3, -0.5, 0.05], "5\n": [0.5, -0.2, 0.3]},
			"2\n":{"1\n" : [-0.4, 0.0, 0.0],"3\n" : [-0.15, -0.5, 0.05],"5\n" : [0.1, -0.2, 0.3]},
			"3\n":{"1\n" : [-0.3, 0.5, -0.05],"2\n" : [0.15, 0.5, -0.05],"4\n" : [-0.25, 1.0, 0.2] ,"5\n" : [0.25, 0.3, 0.25],  "6\n": [-0.25, 0.0, 1.15], },
			"4\n":{"3\n" : [[0.25, -1.0, 0.0],[0.0, 0.0, -0.2]], "5\n" :[0.65, -0.55, 0.25], "6\n" :[0.0, -0.95, 0.95], "8\n": [0.0, -0.2, 0.2] },
			"5\n":{"1\n" : [-0.5, 0.2, -0.3], "2\n" :[-0.1, 0.2, -0.3], "3\n" :[-0.25, -0.3, -0.25], "4\n" :[-0.65, 0.55, -0.25], "6\n" :  [-0.75, -0.45, 0.5] },
			"6\n":{"3\n" : [0.25, 0.0, -1.15], "4\n" : [0.0, 0.95, -0.95], "5\n" :[0.75, 0.45, -0.5] ,"8\n" : [0.0, 0.85, -0.6]},
			"8\n":{"4\n" : [0.0, 0.2, -0.2], "6\n" : [0.0, -0.85, 0.6]}
			}
			robot_init =["0", "6\n"]
			lay_pos = ["1\n", "4\n"]
			hum_pos = ["0", "2\n", "5\n", "7\n"]
			rotate_needs =["3\n","6\n"]
			hum_init = ["0", "2\n"]
			arm_moves = {
			"0" : {"1\n":[1.5, 0.0], "3\n": [[0.0, 1.25], [0.4, 0.0]], "5\n": [-0.5, 0.0]},
			"1\n" : {"3\n":[[0.0, 1.25], [0.4, 0.0]], "5\n": [-2.0, 0.0] },
			"2\n" : {"1\n":[1.5, 0.0], "3\n": [[0.0, 1.25], [0.4, 0.0]], "5\n": [-0.5, 0.0]},
			"3\n" : {"1\n":[[0.0, -1.25], [1.5, 0.0]], "2\n": [0.0, -1.25], "5\n": [[0.0, -1.25], [-0.5, 0.0]], "6\n": [-0.3, 0.0]},
			"5\n" : {"1\n":[2.0, 0.0], "3\n": [[0.0, 1.25], [0.4, 0.0]], "6\n":[[0.0, 1.25], [0.1, 0.0]], "7\n":[-0.3, 0.0]},
			"6\n" : {"3\n":[0.3, 0.0], "5\n":[[0.0, -1.25], [-0.5, 0.0]]},
			"7\n" : {"5\n":[0.3, 0.0]}
			}
			head_moves = {
			"0" : {"4\n": [[0.3, 0.0], [0.5, 0.0]]},
			"1\n" : {"4\n": [[-1.2, 0.0], [-1.0, 0.0]]},
			"2\n" : {"4\n": [[0.3, 0.0], [0.5, 0.0]]},
			"3\n" : {"4\n": [[0.0, -1.25], [0.3, 0.0], [0.0, -1.25], [0.5, 0.0]]},
			"4\n" : {"1\n": [[1.2, 0.0], [1.0, 0.0]], "3\n": [[0.0, 1.25], [0.4, 0.0], [0.0, 1.25], [0.4, 0.0]], "5\n": [[-0.8, 0.0], [-1.0, 0.0]], "6\n": [[0.0, 1.25], [0.1, 0.0], [0.0, 1.25], [0.1, 0.0]], "7\n": [[-1.1, 0.0], [-1.3, 0.0]]},
			"5\n" : {"4\n": [[0.8, 0.0], [1.0, 0.0]]},
			"6\n" : {"4\n": [[0.0, -1.25], [0.3, 0.0], [0.0, -1.25], [0.1, 0.0]]},
			"7\n" : {"4\n": [[1.1, 0.0], [1.3, 0.0]]}
			}
			rinitial = [0.0, 0.0, 0.0]
			r1 = [3.14, 0.0, 0.0]
			r2 = [-3.14, 0.0, 0.0] 
			name= "ik_target.robot.arm.kuka_7"
			time.sleep(2)
			simu.rpc('robot.arm', 'place_IK_target', name, tinitial, rinitial) #it initializes the robot at position 6

			if (c == "7"):
				while (k>=0) and (k<=(m-2)):
					time.sleep(2) #in each time interval, it waits for 2 seconds to ensure the completion of movement
					if A[5][k] == A[5][k+1]:
						print("Robot stays at %s" % (A[5][k]))
					else:
						print("Robot's end effector moves from %s to %s"% (A[5][k], A[5][k+1]))
						coordinate_value = robot_moves[A[5][k]][A[5][k+1]]
						if (len(coordinate_value) ==3) and A[5][k] not in robot_init and A[5][k+1] not in robot_init:
							simu.rpc('robot.arm', 'place_IK_target', name, coordinate_value)
						elif (len(coordinate_value) !=3) and A[5][k] not in robot_init and A[5][k+1] not in robot_init:
							for x in coordinate_value:
								simu.rpc('robot.arm', 'place_IK_target', name, x)
						elif (len(coordinate_value) ==3) and (A[5][k] in robot_init or A[5][k+1] in robot_init):
							if A[5][k] in robot_init:
								simu.rpc('robot.arm', 'place_IK_target', name, coordinate_value, r1)
							else:
								simu.rpc('robot.arm', 'place_IK_target', name, coordinate_value, r2)

					if A[3][k] == A[3][k+1]:
						print("Operators arm stays at %s" % (A[5][k]))
					elif (A[3][k] in rotate_needs and A[3][k+1] not in rotate_needs and A[3][k+1] not in hum_init) or (A[3][k] not in rotate_needs and A[3][k] not in hum_init and A[3][k+1] in rotate_needs):
						print("Operator's arm moves from %s to %s" % (A[3][k], A[3][k+1]))
						simu.rpc('human', 'toggle_manipulation')
						time.sleep(2)
						if (A[4][k+1] == "5\n" and A[3][k+1] =="4\n") or (A[4][k] == "5\n" and A[3][k] =="4\n"):
							simu.rpc('human', 'move', head_moves[A[3][k]][A[3][k+1]][0][0], head_moves[A[3][k]][A[3][k+1]][0][1])
							time.sleep(2)
							simu.rpc('human', 'toggle_manipulation')
							time.sleep(2)
							simu.rpc('human', 'move_hand', head_moves[A[3][k]][A[3][k+1]][1][0], head_moves[A[3][k]][A[3][k+1]][1][1])
							
						elif (A[4][k+1] == "4\n" and A[3][k+1] =="4\n") or (A[4][k] == "4\n" and A[4][k] =="4\n"):
							simu.rpc('human', 'move', head_moves[A[3][k]][A[3][k+1]][2][0], head_moves[A[3][k]][A[3][k+1]][2][1])
							time.sleep(2)
							simu.rpc('human', 'toggle_manipulation')
							time.sleep(2)
							simu.rpc('human', 'move_hand', head_moves[A[3][k]][A[3][k+1]][3][0], head_moves[A[3][k]][A[3][k+1]][3][1])
						else:
							simu.rpc('human', 'move', arm_moves[A[3][k]][A[3][k+1]][0][0], arm_moves[A[3][k]][A[3][k+1]][0][1])
							time.sleep(2)
							simu.rpc('human', 'toggle_manipulation')
							time.sleep(2)
							simu.rpc('human', 'move_hand', arm_moves[A[3][k]][A[3][k+1]][1][0], arm_moves[A[3][k]][A[3][k+1]][1][1])
					elif A[3][k] in rotate_needs and A[3][k+1] in hum_init:
						print("Operator's arm moves from %s to %s" % (A[3][k], A[3][k+1]))
						simu.rpc('human', 'toggle_manipulation')
						time.sleep(2)
						simu.rpc('human', 'move', arm_moves[A[3][k]][A[3][k+1]][0], arm_moves[A[3][k]][A[3][k+1]][1])
					elif A[3][k] in hum_init and A[3][k+1] in rotate_needs:
						print("Operator's arm moves from %s to %s" % (A[3][k], A[3][k+1]))
						simu.rpc('human', 'move', arm_moves[A[3][k]][A[3][k+1]][0][0], arm_moves[A[3][k]][A[3][k+1]][0][1])
						time.sleep(2)
						simu.rpc('human', 'toggle_manipulation')
						time.sleep(2)
						simu.rpc('human', 'move_hand', arm_moves[A[3][k]][A[3][k+1]][1][0], arm_moves[A[3][k]][A[3][k+1]][1][1])
					elif (A[3][k] in rotate_needs and A[3][k+1] in rotate_needs) or (A[3][k] not in rotate_needs and A[3][k] not in hum_init and A[3][k+1] not in rotate_needs and A[3][k+1] not in hum_init):
						print("Operator's arm moves from %s to %s" % (A[3][k], A[3][k+1]))
						if (A[4][k+1] == "5\n" and A[3][k+1] =="4\n") or (A[4][k] == "5\n" and A[3][k] =="4\n"):
							simu.rpc('human', 'move_hand', head_moves[A[3][k]][A[3][k+1]][0][0], head_moves[A[3][k]][A[3][k+1]][0][1])
						elif (A[4][k+1] == "4\n" and A[3][k+1] =="4\n") or (A[4][k] == "4\n" and A[4][k] =="4\n"):
							simu.rpc('human', 'move_hand', head_moves[A[3][k]][A[3][k+1]][1][0], head_moves[A[3][k]][A[3][k+1]][1][1])
						else:
							simu.rpc('human', 'move_hand', arm_moves[A[3][k]][A[3][k+1]][0], arm_moves[A[3][k]][A[3][k+1]][1])
					elif A[3][k] not in rotate_needs and A[3][k] not in hum_init and A[3][k+1] in hum_init:
						print("Operator's arm moves from %s to %s" % (A[3][k], A[3][k+1]))
						simu.rpc('human', 'toggle_manipulation')
					elif A[3][k] in hum_init and A[3][k+1] not in rotate_needs:
						print("Operator's arm moves from %s to %s" % (A[3][k], A[3][k+1]))
						simu.rpc('human', 'toggle_manipulation')
						time.sleep(2)
						if (A[4][k+1] == "5\n" and A[3][k+1] =="4\n") or (A[4][k] == "5\n" and A[3][k] =="4\n"):
							simu.rpc('human', 'move_hand', head_moves[A[3][k]][A[3][k+1]][0][0], head_moves[A[3][k]][A[3][k+1]][0][1])
						elif (A[4][k+1] == "4\n" and A[3][k+1] =="4\n") or (A[4][k] == "4\n" and A[4][k] =="4\n"):
							simu.rpc('human', 'move_hand', head_moves[A[3][k]][A[3][k+1]][1][0], head_moves[A[3][k]][A[3][k+1]][1][1])
						else:
							simu.rpc('human', 'move_hand', arm_moves[A[3][k]][A[3][k+1]][0], arm_moves[A[3][k]][A[3][k+1]][1])
					k=k+1
			elif (c == "0"):
				pose = simu.robot.arm.armpose
				print(pose.get_state())
				pose.subscribe(printer)
				simu.sleep(2)


			if c == "q":
				esc = 1
main()
