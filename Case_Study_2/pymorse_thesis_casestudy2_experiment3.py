import sys
import tty, termios
from pymorse import Morse
import time
from collections import defaultdict
import pdb


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
	hazard = defaultdict(list)
	haz = defaultdict()
	haz = {'HAZARD_OCCURED_': 'hazard_type'}

	hazardrisk = defaultdict(list)
	hazris = defaultdict()
	hazris = {'HAZARD_RISK_1 ': 'hazard_risk 1', 'HAZARD_RISK_2 ': 'hazard_risk 2'}

	hazard_explanation = defaultdict(list)
	hazar_hit = defaultdict()
	hazar_entg = defaultdict()
	hazar_hit = {'hazard_hit 1 ': 'hazard 1', 'hazard_hit 2 ': 'hazard 2'}
	hazar_entg= {'hazard_entg 17': 'hazard 17'}
	
	Haz=[]
	H=[]
	T=[]
	TT=[]
	for hh in range(1,29):
		H.append('HAZARD_RISK_%s'%hh)
	for tt in range(1,29):
		T.append('hazard_risk %s'%tt)
	for kk in range(1,17):
		Haz.append('hazard_hit %s'%kk)
	for kk in range(17,29):
		Haz.append('hazard_entg %s'%kk)
	for aa in range(1,29):
		TT.append('hazard %s'%aa)
	t=2	
	while (t>=2) and (t<=27):
		hazris.update({H[t]: 'hazard_risk %s'%(t+1)})
		hazar_hit.update({Haz[t]: 'hazard %s'%(t+1)})
		t=t+1
	#print(hazar_hit)
	z=False

	for p in parts:
		position[parts[p]].append('0')

	with open('output.hist.txt', 'r') as f_orig:
		i = 0
		for line in f_orig:
			if (i > 1):
				for p in parts:
					if p in line:
						position[parts[p]].append(line[-2:])
			if (i > 0):
				for h in haz:
					if h in line :
						hazard[haz[h]].append(line[-3:])
						#pdb.set_trace()
						z=True
					elif h not in line and ("------ time" in line or "------ end" in line) and z == False:
						hazard[haz[h]].append('0')
				for j in hazris:
					if j in line :
						hazardrisk[hazris[j]].append(line[-2:])
			if "------ time" in line:
				i += 1
				z=False

	with open('Hazards.lisp', 'r') as f_haz:
		for line in f_haz:
			for ha in hazar_hit:
				if ha in line :
					hazard_explanation[hazar_hit[ha]].append(line.split("`")[1].split("_area")[0])
					hazard_explanation[hazar_hit[ha]].append(line.split("`")[2].split(" ")[0])
				

	A=[position['link_1'], position['link_2'], position['base'], position['arm'], position['head'], position['endeff']]
	B=[hazard['hazard_type']]
	C=[]
	D=[]
	E=[]

	for cc in range(0,28):
		C.append(hazardrisk[T[cc]])
	for aa in range(0,28):
		E.append(hazard_explanation[TT[aa]])
	for i in range(1,10):
		D.append("_%s\n"%i)
	for i in range(10,29):
		D.append("%s\n"%i)

	k=0
	n=len(A)
	m=len(A[0])
	#print(A)
	#print(B)
	#print(C)
	#print(D)
	#print(E)
	with Morse("localhost", 4000)  as simu:

		esc= 0

		while not esc:
			tab_pos=False #the memory of the position where the material will be released. if it is true, it means the material there.
			mat_pos=True #the memory of the position of the material.
			mat_grab=False #the memory of the grab. if it is true, it means the material is already grabbed.
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
			robot_init =["0", "6\n"] #initial position of the robot
			lay_pos = ["1\n", "4\n"] #positions of the layout side
			hum_pos = ["0", "2\n", "5\n", "7\n"] #positions of the human side
			rotate_needs =["3\n","6\n"] #rotation (human move command) is needed. position are in a different symmetry
			hum_init = ["0", "2\n"] #initial position of the human arm
			material_pos = ["3\n"] #position of the material which will be taken
			table_pos = ["4\n"] #position where the material will be released
			head_pos = ["5\n"] #default position of the head
			head_changes = ["4\n"] #position of the head after movement
			head_move_needed = ["4\n"] #the position movement of the arm where the head movement needed
			arm_moves = {
			"0" : {"1\n":[1.5, 0.0], "3\n": [[0.0, 1.25], [0.4, 0.0]], "5\n": [-0.5, 0.0]},
			"1\n" : {"3\n":[[0.0, 1.25], [0.4, 0.0]], "5\n": [-2.0, 0.0] },
			"2\n" : {"1\n":[1.5, 0.0], "3\n": [[0.0, 1.25], [0.4, 0.0]], "5\n": [-0.5, 0.0]},
			"3\n" : {"1\n":[[0.0, -1.25], [1.5, 0.0]], "2\n": [0.0, -1.25], "5\n": [[0.0, -1.25], [-0.5, 0.0]], "6\n": [-0.3, 0.0]},
			"5\n" : {"1\n":[2.0, 0.0], "3\n": [[0.0, 1.25], [0.4, 0.0]], "6\n":[[0.0, 1.25], [0.1, 0.0]], "7\n":[-0.4, 0.0]},
			"6\n" : {"3\n":[0.3, 0.0], "5\n":[[0.0, -1.25], [-0.5, 0.0]]},
			"7\n" : {"5\n":[0.4, 0.0]}
			}
			head_moves = {
			"0" : {"4\n": [[0.3, 0.0], [0.5, 0.0]]},
			"1\n" : {"4\n": [[-1.2, 0.0], [-1.0, 0.0]]},
			"2\n" : {"4\n": [[0.3, 0.0], [0.5, 0.0]]},
			"3\n" : {"4\n": [[0.0, -1.25], [0.3, 0.0], [0.0, -1.25], [0.5, 0.0]]},
			"4\n" : {"1\n": [[1.2, 0.0], [1.0, 0.0]], "3\n": [[0.0, 1.25], [0.4, 0.0], [0.0, 1.25], [0.4, 0.0]], "5\n": [[-0.8, 0.0], [-1.0, 0.0]], "6\n": [[0.0, 1.25], [0.1, 0.0], [0.0, 1.25], [0.1, 0.0]], "7\n": [[-1.2, 0.0], [-1.4, 0.0]]},
			"5\n" : {"4\n": [[0.8, 0.0], [1.0, 0.0]]},
			"6\n" : {"4\n": [[0.0, -1.25], [0.3, 0.0], [0.0, -1.25], [0.1, 0.0]]},
			"7\n" : {"4\n": [[1.2, 0.0], [1.4, 0.0]]}
			}
			rinitial = [0.0, 0.0, 0.0]
			r1 = [3.14, 0.0, 0.0]
			r2 = [-3.14, 0.0, 0.0] 
			name= "ik_target.robot.arm.kuka_7"
			time.sleep(2)
			simu.rpc('robot.arm', 'place_IK_target', name, tinitial, rinitial) #it initializes the robot at position 6

			if (c == "7"):
				while (k>=0) and (k<=(m-2)):
					time.sleep(5) #in each time interval, it waits for 2 seconds to ensure the completion of movement
					print("----- Time %s -----"%(k+1))
					if A[5][k] == A[5][k+1]:
						print("Robot stays at %s" % (A[5][k]))
					else:
						if A[5][k] in table_pos and mat_grab==False and tab_pos==True:
							time.sleep(2)
							mat_grab=True
							tab_pos=False
							print("Robot grabs the material")
							simu.rpc('robot.arm.gripper', 'grab')	
						elif A[5][k] in material_pos and mat_grab==False and mat_pos==True:
							time.sleep(2)
							mat_grab=True
							mat_pos=False
							print("Robot grabs the material")
							simu.rpc('robot.arm.gripper', 'grab')					
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
						if A[5][k+1] in material_pos and mat_grab==True and mat_pos==False:
							time.sleep(2)
							mat_grab=False
							mat_pos=True
							print("Robot releases the material")
							simu.rpc('robot.arm.gripper', 'release') 
						elif A[5][k+1] in table_pos and mat_grab==True and tab_pos==False:
							time.sleep(2)
							mat_grab=False
							tab_pos=True
							print("Robot releases the material")
							simu.rpc('robot.arm.gripper', 'release')
					if A[3][k] == A[3][k+1]:
						print("Operators arm stays at %s" % (A[3][k]))
					elif (A[3][k] in rotate_needs and A[3][k+1] not in rotate_needs and A[3][k+1] not in hum_init) or (A[3][k] not in rotate_needs and A[3][k] not in hum_init and A[3][k+1] in rotate_needs):
						print("Operator's arm moves from %s to %s" % (A[3][k], A[3][k+1]))
						simu.rpc('human', 'toggle_manipulation')
						time.sleep(2)
						if (A[4][k+1] in head_pos and A[3][k+1] in head_move_needed) or (A[4][k] in head_pos and A[3][k] in head_move_needed):
							simu.rpc('human', 'move', head_moves[A[3][k]][A[3][k+1]][0][0], head_moves[A[3][k]][A[3][k+1]][0][1])
							time.sleep(2)
							simu.rpc('human', 'toggle_manipulation')
							time.sleep(2)
							simu.rpc('human', 'move_hand', head_moves[A[3][k]][A[3][k+1]][1][0], head_moves[A[3][k]][A[3][k+1]][1][1])
							
						elif (A[4][k+1] in head_changes and A[3][k+1] in head_move_needed) or (A[4][k] in head_changes and A[3][k] in head_move_needed):
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
						if (A[4][k+1] in head_pos and A[3][k+1] in head_move_needed) or (A[4][k] in head_pos and A[3][k] in head_move_needed):
							simu.rpc('human', 'move_hand', head_moves[A[3][k]][A[3][k+1]][0][0], head_moves[A[3][k]][A[3][k+1]][0][1])
						elif (A[4][k+1] in head_changes and A[3][k+1] in head_move_needed) or (A[4][k] in head_pos and A[3][k] in head_move_needed):
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
						if (A[4][k+1] in head_pos and A[3][k+1] in head_move_needed) or (A[4][k] in head_pos and A[3][k] in head_move_needed):
							simu.rpc('human', 'move_hand', head_moves[A[3][k]][A[3][k+1]][0][0], head_moves[A[3][k]][A[3][k+1]][0][1])
						elif (A[4][k+1] in head_changes and A[3][k+1] in head_move_needed) or (A[4][k] == "4\n" and A[3][k] in head_move_needed):
							simu.rpc('human', 'move_hand', head_moves[A[3][k]][A[3][k+1]][1][0], head_moves[A[3][k]][A[3][k+1]][1][1])
						else:
							simu.rpc('human', 'move_hand', arm_moves[A[3][k]][A[3][k+1]][0], arm_moves[A[3][k]][A[3][k+1]][1])
					if B[0][k+1]== '0':
						print("There is no hazard occured.")
					else:
						for i in D:
							if B[0][k+1] == i:
								o=D.index(i)
								print("Hazard number %s occured."%(o+1))
								if (o>=0) and (o<=15):
									print("Tr on %s by %s"%(E[o][0], E[o][1]))
								elif (o<=16) and (o>=28):
									print("Qs on %s by %s"%(E[o][0], E[o][1]))
								print("Hazard number %s has a risk value %s" %((o+1), C[o][k+1]))
						
						
					k=k+1
			elif (c == "0"):
				pose = simu.robot.arm.armpose
				print(pose.get_state())
				pose.subscribe(printer)
				simu.sleep(2)


			if c == "q":
				esc = 1
main()
