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
	parts = {'OPERATOR_1_LEG_AREA_IN_L_': 'leg', 'LINK1_1_IN_L_': 'link_1','LINK2_1_IN_L_': 'link_2','ENDEFF_1_IN_L_': 'endeff','OPERATOR_1_ARM_AREA_IN_L_': 'arm', 'OPERATOR_1_HEAD_AREA_IN_L_': 'head'}
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
	K=defaultdict(list)
	
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
	memo_list=False
	for p in parts:
		position[parts[p]].append('0')
	for h in haz:
		hazard[haz[h]].append(['0'])
	with open('output3.hist.txt', 'r') as f_orig:
		i = 0
		for line in f_orig:
			if (i > 1):
				for p in parts:
					if p in line:
						position[parts[p]].append(line[-3:])			
				for h in haz:
					if h in line:
						if memo_list == False:
							hazard[haz[h]].append([])
							memo_list = True
						if memo_list == True:
							hazard[haz[h]][i-1].append(line[-3:])
						#pdb.set_trace()
						z=True
					if h not in line and ("------ time" in line or "------ end" in line) and z == False:
						hazard[haz[h]].append(['0'])
				for j in hazris:
					if j in line :
						hazardrisk[hazris[j]].append(line[-2:])
			if "------ time" in line:
				i += 1
				z=False
				memo_list = False

	with open('Hazards.lisp', 'r') as f_haz:
		for line in f_haz:
			for ha in hazar_hit:
				if ha in line :
					hazard_explanation[hazar_hit[ha]].append(line.split("`")[1].split("_area")[0])
					hazard_explanation[hazar_hit[ha]].append(line.split("`")[2].split(" ")[0])
				

	A=[position['link_1'], position['link_2'], position['leg'], position['arm'], position['head'], position['endeff']]
	B=hazard['hazard_type']
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
	print(A)
	print(B)
	print(K)
	#print(D)
	#print(E)
	with Morse("localhost", 4000)  as simu:

		esc= 0

		while not esc:
			tab_pos=False #the memory of the position where the material will be released. if it is true, it means the material there.
			mat_pos=False #the memory of the position of the material.
			mat_grab=False #the memory of the grab. if it is true, it means the material is already grabbed.
			c = getchar()
			tinitial = [0.0, 0.0, 1.0]
			robot_moves = {
			"0":{"30\n" : [0.2, 0.1, -1.0], "_9\n" : [0.25, 0.1, -1.25], "23\n": [-0.6, 1.3, -0.5]},
			"_1\n":{"30\n" : [0.2, 0.1, -1.0], "_9\n" : [0.25, 0.1, -1.25], "23\n": [-0.6, 1.3, -0.5]},
			"22\n":{"30\n" : [0.2, 0.1, -1.0], "_9\n" : [0.25, 0.1, -1.25], "23\n": [-0.6, 1.3, -0.5]},
			"_5\n" : {"_9\n":[-0.09, -0.075, 0.05] , "13\n":[0.265, -0.72, -0.01], "14\n": [0.25, -0.02, 0.0], "26\n": [0.0, 0.0, 0.25], "30\n": [-0.2, -0.1, 0.25], "34\n": [0.22, -0.62, 0.12], "35\n": [0.22, -0.03, 0.22]},
			"_9\n" : {"0":[-0.25, -0.1, 1.25] , "_1\n":[-0.25, -0.1, 1.25], "_5\n": [0.09, 0.075, -0.05], "22\n": [-0.25, -0.1, 1.25], "26\n": [0.09, 0.08, 0.2], "30\n": [-0.05, 0.0, 0.25]},
			"13\n" : {"_5\n":[-0.265, 0.72, 0.01] , "14\n":[0.08, 0.7, 0.05], "26\n": [-0.22, 0.69, 0.27], "34\n": [-0.5, 0.5, 0.1], "35\n": [-0.005, 0.77, 0.25]},
			"14\n" : {"_5\n":[-0.25, 0.02, 0.0] , "13\n":[-0.08, -0.7, -0.05], "26\n": [-0.25, 0.025, 0.25], "34\n": [-0.08, -0.63, 0.09], "35\n": [-0.005, -0.01, 0.22]},
			"26\n" : {"_5\n":[0.0, 0.0, -0.25] , "_9\n":[-0.09, -0.08, -0.2], "13\n": [0.22, -0.69, -0.27], "14\n": [0.25, -0.025, -0.25], "30\n": [-0.2, -0.1, 0.0], "34\n": [0.5, -0.8, 0.0], "35\n": [0.3, 0.0, 0.0]},
			"2\n":{"1\n" : [-0.4, 0.0, 0.0],"3\n" : [-0.15, -0.5, 0.05],"5\n" : [0.1, -0.2, 0.3]},
			"30\n" : {"0":[-0.2, -0.1, 1.0] , "_1\n":[-0.2, -0.1, 1.0], "_5\n": [0.2, 0.1, -0.25], "22\n": [-0.2, -0.1, 1.0], "_9\n": [0.05, 0.0, -0.25], "26\n": [0.2, 0.1, 0.0]},
			"34\n" : {"_5\n":[-0.22, 0.62, -0.12] , "13\n":[0.5, -0.5, -0.1], "14\n": [0.08, 0.63, -0.09], "26\n": [-0.5, 0.8, 0.0], "35\n": [0.07, 0.63, 0.12]},
			"35\n" : {"_5\n":[-0.22, 0.03, -0.22] , "13\n":[0.005, -0.77, -0.25], "14\n": [0.005, 0.01, -0.22], "26\n": [-0.3, 0.0, 0.0], "34\n": [-0.07, -0.63, -0.12]},
			"23\n":{"32\n" : [-0.6, 0.0, 0.0]},
			"32\n":{"23\n" : [0.6, 0.0, 0.0]}
			}
			robot_init =["0", "_1\n", "22\n"] #initial position of the robot
			lay_pos = ["15\n", "36\n"] #positions of the layout side
			hum_pos = ["0", "14\n", "35\n"] #positions of the human side
			hum_hand_init = ["0", "14\n"] 
			hum_leg_init = ["0", "_5\n", "_9\n", "13\n", "14\n"] #human stays at 2_3 at the beginning, so these are all 2_ values
			hum_reachability_from_init = ["0", "_5\n", "_6\n", "_9\n", "10\n", "13\n", "14\n", "15\n", "26\n", "27\n", "30\n", "31\n", "34\n", "35\n", "36\n"] #human's hand can reach at these positions from the initial position
			hum_not_reach_outer = ["18\n"] #position where human's hand cannot reach (outer circle)
			hum_not_reach_inner = ["11\n"] #position where human's hand cannot reach (inner circle)
			rotate_needs = ["27\n","_6\n"] #rotation (human move command) is needed. positions are in a different symmetry
			rotate_needs2 = ["10\n", "31\n"]
			rotate_needs3 = ["_9\n", "30\n", "_5\n", "26\n"]
			rotate_needs4 = ["13\n", "34\n"]
			no_move = ["_5\n", "26\n"]
			hum_init = ["0", "14\n"] #initial position of the human arm
			material_pos = [] #position of the material which will be taken
			table_pos = [] #position where the material will be released
			head_pos = [] #default position of the head
			head_changes = [] #position of the head after movement
			head_move_needed = [] #the position movement of the arm where the head movement needed
			arm_moves = {
			"0" : {"_5\n":[[0.0, 0.785], [0.1, 0.0]], "_6\n": [[0.0, 0.26166667], [0.6, 0.0]], "_9\n": [[0.0, 0.785], [0.7, 0.0]], "10\n": [[0.0, 0.52333333], [0.6, 0.0]], "13\n": [[0.0, 2.355], [0.6, 0.0]], "15\n": [0.6, 0.0], "26\n": [[0.0, 0.785], [0.1, 0.0]], "27\n": [[0.0, 0.26166667], [0.6, 0.0]], "30\n": [[0.0, 0.785], [0.3, 0.0]], "31\n": [[0.0, 0.52333333], [0.6, 0.0]], "34\n": [[0.0, 2.355], [0.6, 0.0]], "36\n": [0.2, 0.0], "35\n": [-0.5, 0.0]},
			"14\n" : {"_5\n":[[0.0, 0.785], [0.1, 0.0]], "_6\n": [[0.0, 0.26166667], [0.6, 0.0]], "_9\n": [[0.0, 0.785], [0.7, 0.0]], "10\n": [[0.0, 0.52333333], [0.6, 0.0]], "13\n": [[0.0, 2.355], [0.6, 0.0]], "15\n": [0.6, 0.0], "26\n": [[0.0, 0.785], [0.1, 0.0]], "27\n": [[0.0, 0.26166667], [0.6, 0.0]], "30\n": [[0.0, 0.785], [0.3, 0.0]], "31\n": [[0.0, 0.52333333], [0.6, 0.0]], "34\n": [[0.0, 2.355], [0.6, 0.0]], "36\n": [0.2, 0.0], "35\n": [-0.5, 0.0]},
			"_5\n" : {"14\n":[0.0, -0.785], "_6\n": [[0.0, -0.52333333], [0.6, 0.0]], "_9\n": [0.6, 0.0], "10\n": [[0.0, -0.26166667], [0.6, 0.0]], "13\n": [[0.0, 1.57], [0.6, 0.0]], "15\n": [0.6, 0.0], "27\n": [[0.0, -0.52333333], [0.2, 0.0]], "30\n": [0.2, 0.0], "31\n": [[0.0, -0.26166667], [0.2, 0.0]], "34\n": [[0.0, 1.57], [0.2, 0.0]], "36\n": [0.0, -0.785], "35\n" :[[0.0, -0.785], [-0.5, 0.0]]},
			"26\n" : {"14\n":[0.0, -0.785], "_6\n": [[0.0, -0.52333333], [0.6, 0.0]], "_9\n": [0.6, 0.0], "10\n": [[0.0, -0.26166667], [0.6, 0.0]], "13\n": [[0.0, 1.57], [0.6, 0.0]], "15\n": [0.6, 0.0], "27\n": [[0.0, -0.52333333], [0.2, 0.0]], "30\n": [0.2, 0.0], "31\n": [[0.0, -0.26166667], [0.2, 0.0]], "34\n": [[0.0, 1.57], [0.2, 0.0]], "36\n": [0.0, -0.785], "35\n" :[[0.0, -0.785], [-0.5, 0.0]]},
			"_6\n" : {"_5\n":[[0.0, 0.52333333], [0.1, 0.0]], "14\n": [0.0, -0.26166667], "_9\n": [[0.0, 0.52333333], [0.7, 0.0]], "10\n": [[0.0, 0.26166667], [0.6, 0.0]], "13\n": [[0.0, -2.0932], [0.6, 0.0]], "15\n": [[0.0, -0.26166667], [0.6, 0.0]], "26\n": [[0.0, 0.52333333], [0.1, 0.0]], "27\n": [-0.4, 0.0], "30\n": [[0.0, 0.52333333], [0.3, 0.0]], "31\n": [[0.0, 0.26166667], [0.2, 0.0]], "34\n": [[0.0, 2.0932], [0.2, 0.0]], "36\n": [[0.0, -0.26166667], [0.2, 0.0]], "35\n": [[0.0, -0.26166667], [-0.5, 0.0]]},
			"_9\n" : {"_5\n":[-0.6, 0.0], "_6\n": [[0.0, -0.52333333], [0.6, 0.0]], "14\n": [0.0, -0.785], "10\n": [[0.0, -0.26166667], [0.6, 0.0]], "13\n": [[0.0, 1.57], [0.6, 0.0]], "15\n": [[0.0, -0.785], [0.6, 0.0]], "26\n": [-0.6, 0.0], "27\n": [[0.0, -0.52333333], [0.2, 0.0]], "30\n": [-0.4, 0.0], "31\n": [[0.0, -0.26166667], [0.2, 0.0]], "34\n": [[0.0, 1.57], [0.2, 0.0]], "36\n": [[0.0, -0.785], [0.2, 0.0]], "35\n": [[0.0, -0.785], [-0.5, 0.0]]},
			"10\n" : {"_5\n":[[0.0, 0.26166667], [0.1, 0.0]], "_6\n": [[0.0, -0.26166667], [0.6, 0.0]], "_9\n": [[0.0, 0.26166667], [0.7, 0.0]], "14\n": [0.0, -0.52333333], "13\n": [[0.0, 1.8317], [0.6, 0.0]], "15\n": [[0.0, -0.52333333], [0.6, 0.0]], "26\n": [[0.0, 0.26166667], [0.1, 0.0]], "27\n": [[0.0, -0.26166667], [0.2, 0.0]], "30\n": [[0.0, 0.26166667], [0.3, 0.0]], "31\n": [-0.4, 0.0], "34\n": [[0.0, 1.8317], [0.2, 0.0]], "36\n": [[0.0, -0.52333333], [0.2, 0.0]], "35\n": [[0.0, -0.52333333], [-0.5, 0.0]]}, 
			"13\n" : {"_5\n":[[0.0, -1.57], [0.1, 0.0]], "_6\n": [[0.0, -2.0932], [0.6, 0.0]], "_9\n": [[0.0, -1.57], [0.7, 0.0]], "10\n": [[0.0, -1.8317], [0.6, 0.0]], "14\n": [0.0, -2.355], "15\n": [[0.0, -2.355], [0.6, 0.0]], "26\n": [[0.0, -1.57], [0.1, 0.0]], "27\n": [[0.0, -2.0932], [0.2, 0.0]], "30\n": [[0.0, -1.57], [0.3, 0.0]], "31\n": [[0.0, -1.8317], [0.2, 0.0]], "34\n": [-0.4, 0.0], "36\n": [[0.0, -2.355], [0.2, 0.0]], "35\n": [[0.0, -2.355], [-0.5, 0.0]]},
			"15\n" : {"_5\n":[[0.0, 0.785], [0.3, 0.0]], "_6\n": [[0.0, 0.26166667], [0.6, 0.0]], "_9\n": [[0.0, 0.785], [0.7, 0.0]], "10\n": [[0.0, 0.52333333], [0.6, 0.0]], "13\n": [[0.0, 2.355], [0.6, 0.0]], "26\n": [[0.0, 0.785], [0.3, 0.0]], "27\n": [[0.0, 0.26166667], [0.2, 0.0]], "30\n": [[0.0, 0.785], [0.3, 0.0]], "31\n": [[0.0, 0.52333333], [0.2, 0.0]], "34\n": [[0.0, 2.355], [0.2, 0.0]], "36\n": [-0.4, 0.0], "35\n": [-0.5, 0.0]},
			"27\n" : {"_5\n":[[0.0, 0.52333333], [0.1, 0.0]], "_6\n": [0.4, 0.0], "_9\n": [[0.0, 0.52333333], [0.7, 0.0]], "10\n": [[0.0, 0.26166667], [0.6, 0.0]], "13\n": [[0.0, 2.0932], [0.6, 0.0]], "15\n": [[0.0, -0.26166667], [0.6, 0.0]], "26\n": [[0.0, 0.52333333], [0.1, 0.0]], "14\n": [0.0, -0.26166667], "30\n": [[0.0, 0.52333333], [0.3, 0.0]], "31\n": [[0.0, 0.26166667], [0.2, 0.0]], "34\n": [[0.0, 2.0932], [0.2, 0.0]], "36\n": [[0.0, -0.26166667], [0.2, 0.0]], "35\n": [[0.0, -0.26166667], [-0.5, 0.0]]},
			"30\n" : {"_5\n":[-0.2, 0.0], "_6\n": [[0.0, -0.52333333], [0.6, 0.0]], "_9\n": [0.4, 0.0], "10\n": [[0.0, -0.26166667], [0.2, 0.0]], "13\n": [[0.0, 1.57], [0.6, 0.0]], "15\n": [[0.0, -0.785], [0.6, 0.0]], "26\n": [-0.2, 0.0], "27\n": [[0.0, -0.52333333], [0.2, 0.0]], "14\n": [0.0, -0.785], "31\n": [[0.0, -0.26166667], [0.2, 0.0]], "34\n": [[0.0, 1.57], [0.2, 0.0]], "36\n": [[0.0, -0.785], [0.2, 0.0]], "35\n": [[0.0, -0.785], [-0.5, 0.0]]},
			"31\n" : {"_5\n":[[0.0, 0.26166667], [0.1, 0.0]], "_6\n": [[0.0, -0.26166667], [0.6, 0.0]], "_9\n": [[0.0, 0.26166667], [0.7, 0.0]], "10\n": [0.4, 0.0], "13\n": [[0.0, 1.8317], [0.6, 0.0]], "15\n": [[0.0, -0.52333333], [0.6, 0.0]], "26\n": [[0.0, 0.26166667], [0.1, 0.0]], "27\n": [[0.0, -0.26166667], [0.2, 0.0]], "30\n": [[0.0, 0.26166667], [0.3, 0.0]], "14\n": [0.0, -0.52333333], "34\n": [[0.0, 1.8317], [0.2, 0.0]], "36\n": [[0.0, -0.52333333], [0.2, 0.0]], "35\n": [[0.0, -0.52333333], [-0.5, 0.0]]},
			"34\n" : {"_5\n":[[0.0, -1.57], [0.1, 0.0]], "_6\n": [[0.0, -2.0932], [0.6, 0.0]], "_9\n": [[0.0, -1.57], [0.7, 0.0]], "10\n": [[0.0, -1.8317], [0.6, 0.0]], "13\n": [0.4, 0.0], "15\n": [[0.0, -2.355], [0.6, 0.0]], "26\n": [[0.0, -1.57], [0.1, 0.0]], "27\n": [[0.0, -2.0932], [0.2, 0.0]], "30\n": [[0.0, -1.57], [0.3, 0.0]], "31\n": [[0.0, -1.8317], [0.2, 0.0]], "14\n": [0.0, -2.355], "36\n": [[0.0, -2.355], [0.2, 0.0]], "35\n": [[0.0, -2.355], [-0.5, 0.0]]},
			"36\n" : {"_5\n":[[0.0, 0.785], [0.1, 0.0]], "_6\n": [[0.0, 0.26166667], [0.6, 0.0]], "_9\n": [[0.0, 0.785], [0.7, 0.0]], "10\n": [[0.0, 0.52333333], [0.6, 0.0]], "13\n": [[0.0, 2.355], [0.6, 0.0]], "15\n": [0.4, 0.0], "26\n": [[0.0, 0.785], [0.1, 0.0]], "27\n": [[0.0, 0.26166667], [0.2, 0.0]], "30\n": [[0.0, 0.785], [0.3, 0.0]], "31\n": [[0.0, 0.52333333], [0.2, 0.0]], "34\n": [[0.0, 2.355], [0.2, 0.0]], "35\n": [-0.5, 0.0]},
			"35\n" : {"_5\n":[[0.0, 0.785], [0.1, 0.0]], "_6\n": [[0.0, 0.26166667], [0.6, 0.0]], "_9\n": [[0.0, 0.785], [0.7, 0.0]], "10\n": [[0.0, 0.52333333], [0.6, 0.0]], "13\n": [[0.0, 2.355], [0.6, 0.0]], "15\n": [0.6, 0.0], "26\n": [[0.0, 0.785], [0.1, 0.0]], "27\n": [[0.0, 0.26166667], [0.6, 0.0]], "30\n": [[0.0, 0.785], [0.3, 0.0]], "31\n": [[0.0, 0.52333333], [0.6, 0.0]], "34\n": [[0.0, 2.355], [0.6, 0.0]], "36\n": [0.2, 0.0]},
			"18\n" : {"11\n": [1.0, 0.0], "32\n": [0.4, 0.0], "39\n": [0.2, 0.0]}
			}
			head_moves = { 
			}
			leg_moves = {
			"0": {"11\n":[[0.0, -0.785], [1.3, 0.0], [0.0, 1.57], [1.3, 0.0], [0.0, 1.57], [0.5, 0.0]], "18\n":[[0.0, -0.785], [1.3, 0.0], [0.0, 1.57], [1.3, 0.0], [0.0, 1.57]]},
			"_5\n": {"11\n":[[0.0, -0.785], [1.3, 0.0], [0.0, 1.57], [1.3, 0.0], [0.0, 1.57], [0.5, 0.0]], "18\n":[[0.0, -0.785], [1.3, 0.0], [0.0, 1.57], [1.3, 0.0], [0.0, 1.57]]},
			"_6\n": {"11\n":[[0.0, -1.0467], [1.3, 0.0], [0.0, 1.57], [1.3, 0.0], [0.0, 1.57], [0.5, 0.0]], "18\n":[[0.0, -1.0467], [1.3, 0.0], [0.0, 1.57], [1.3, 0.0], [0.0, 1.57]]}
			}
			arm_moves_diff = {"18\n": {"39\n":[0.2, 0.0]},
			"11\n": {"39\n":[0.7, 0.0]}
			}
			rinitial = [0.0, 0.0, 0.0]
			r1 = [3.14, 0.0, 0.0]
			r2 = [-3.14, 0.0, 0.0] 
			name= "ik_target.robot.arm.kuka_7"
			time.sleep(2)
			simu.rpc('robot.arm', 'place_IK_target', name, tinitial, rinitial) #it initializes the robot at position 6

			if (c == "7"):
				while (k>=0) and (k<=(m-2)):
					time.sleep(3) #in each time interval, it waits for 3 seconds to ensure the completion of movement
					print("----- From time %s to time %s -----"%(k, k+1))
					if (A[5][k] == A[5][k+1]) or (A[5][k] in robot_init and A[5][k+1] in robot_init):
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
					if A[3][k] == A[3][k+1] or (A[3][k] in no_move and A[3][k+1] in no_move):
						print("Operators arm stays at %s" % (A[3][k]))
					if (A[3][k+1] in hum_reachability_from_init and A[3][k] != A[3][k+1]):
						if (((A[3][k] in rotate_needs and A[3][k+1] not in rotate_needs) or (A[3][k] in rotate_needs2 and A[3][k+1] not in rotate_needs2) or (A[3][k] in rotate_needs3 and A[3][k+1] not in rotate_needs3) or (A[3][k] in rotate_needs4 and A[3][k+1] not in rotate_needs4)) and A[3][k+1] not in hum_init) or (((A[3][k] not in rotate_needs and A[3][k+1] in rotate_needs) or (A[3][k] not in rotate_needs2 and A[3][k+1] in rotate_needs2) or (A[3][k] not in rotate_needs3 and A[3][k+1] in rotate_needs3) or (A[3][k] not in rotate_needs4 and A[3][k+1] in rotate_needs4)) and A[3][k] not in hum_init):
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
						elif (A[3][k] in rotate_needs or A[3][k] in rotate_needs2 or A[3][k] in rotate_needs3 or A[3][k] in rotate_needs4) and A[3][k+1] in hum_init:
							print("Operator's arm moves from %s to %s" % (A[3][k], A[3][k+1]))
							simu.rpc('human', 'toggle_manipulation')
							time.sleep(2)
							simu.rpc('human', 'move', arm_moves[A[3][k]][A[3][k+1]][0], arm_moves[A[3][k]][A[3][k+1]][1])
						elif A[3][k] in hum_init and (A[3][k+1] in rotate_needs or A[3][k+1] in rotate_needs2 or A[3][k+1] in rotate_needs3 or A[3][k+1] in rotate_needs4):
							print("Operator's arm moves from %s to %s" % (A[3][k], A[3][k+1]))
							simu.rpc('human', 'move', arm_moves[A[3][k]][A[3][k+1]][0][0], arm_moves[A[3][k]][A[3][k+1]][0][1])
							time.sleep(2)
							simu.rpc('human', 'toggle_manipulation')
							time.sleep(2)
							simu.rpc('human', 'move_hand', arm_moves[A[3][k]][A[3][k+1]][1][0], arm_moves[A[3][k]][A[3][k+1]][1][1])
						elif ((A[3][k] in rotate_needs and A[3][k+1] in rotate_needs) or (A[3][k] in rotate_needs2 and A[3][k+1] in rotate_needs2) or (A[3][k] in rotate_needs3 and A[3][k+1] in rotate_needs3) or (A[3][k] in rotate_needs4 and A[3][k+1] in rotate_needs4)) or ((A[3][k] not in rotate_needs or A[3][k] not in rotate_needs2 or A[3][k] not in rotate_needs3 or A[3][k] not in rotate_needs4) and A[3][k] not in hum_init and (A[3][k+1] not in rotate_needs or A[3][k+1] not in rotate_needs2 or A[3][k+1] not in rotate_needs3 or A[3][k+1] not in rotate_needs4) and A[3][k+1] not in hum_init):
							print("Operator's arm moves from %s to %s" % (A[3][k], A[3][k+1]))
							if (A[4][k+1] in head_pos and A[3][k+1] in head_move_needed) or (A[4][k] in head_pos and A[3][k] in head_move_needed):
								simu.rpc('human', 'move_hand', head_moves[A[3][k]][A[3][k+1]][0][0], head_moves[A[3][k]][A[3][k+1]][0][1])
							elif (A[4][k+1] in head_changes and A[3][k+1] in head_move_needed) or (A[4][k] == "4\n" and A[3][k] =="4\n"):
								simu.rpc('human', 'move_hand', head_moves[A[3][k]][A[3][k+1]][1][0], head_moves[A[3][k]][A[3][k+1]][1][1])
							else:
								simu.rpc('human', 'move_hand', arm_moves[A[3][k]][A[3][k+1]][0], arm_moves[A[3][k]][A[3][k+1]][1])
						elif (A[3][k] not in rotate_needs or A[3][k] not in rotate_needs2 or A[3][k] not in rotate_needs3 or A[3][k] not in rotate_needs4) and A[3][k] not in hum_init and A[3][k+1] in hum_init:
							print("Operator's arm moves from %s to %s" % (A[3][k], A[3][k+1]))
							simu.rpc('human', 'toggle_manipulation')
						elif A[3][k] in hum_init and (A[3][k+1] not in rotate_needs or [3][k+1] not in rotate_needs2 or [3][k+1] not in rotate_needs3 or [3][k+1] not in rotate_needs4):
							print("Operator's arm moves from %s to %s" % (A[3][k], A[3][k+1]))
							simu.rpc('human', 'toggle_manipulation')
							time.sleep(2)
							if (A[4][k+1] in head_pos and A[3][k+1] in head_move_needed) or (A[4][k] in head_pos and A[3][k] in head_move_needed):
								simu.rpc('human', 'move_hand', head_moves[A[3][k]][A[3][k+1]][0][0], head_moves[A[3][k]][A[3][k+1]][0][1])
							elif (A[4][k+1] in head_changes and A[3][k+1] in head_move_needed) or (A[4][k] in head_changes and A[3][k] in head_move_needed):
								simu.rpc('human', 'move_hand', head_moves[A[3][k]][A[3][k+1]][1][0], head_moves[A[3][k]][A[3][k+1]][1][1])
							else:
								simu.rpc('human', 'move_hand', arm_moves[A[3][k]][A[3][k+1]][0], arm_moves[A[3][k]][A[3][k+1]][1])
					elif A[2][k] in hum_reachability_from_init and A[3][k+1] not in hum_reachability_from_init and A[2][k+1] not in hum_reachability_from_init:
						print("Operator walks from the initial position to %s" %(A[2][k+1]))
						if A[3][k] not in hum_hand_init:
							simu.rpc('human', 'toggle_manipulation')
						simu.rpc('human', 'move', leg_moves[A[2][k]][A[2][k+1]][0][0], leg_moves[A[2][k]][A[2][k+1]][0][1])
						time.sleep(2)
						simu.rpc('human', 'move', leg_moves[A[2][k]][A[2][k+1]][1][0], leg_moves[A[2][k]][A[2][k+1]][1][1])
						time.sleep(2)
						simu.rpc('human', 'move', leg_moves[A[2][k]][A[2][k+1]][2][0], leg_moves[A[2][k]][A[2][k+1]][2][1])
						time.sleep(2)
						simu.rpc('human', 'move', leg_moves[A[2][k]][A[2][k+1]][3][0], leg_moves[A[2][k]][A[2][k+1]][3][1])
						time.sleep(2)
						simu.rpc('human', 'move', leg_moves[A[2][k]][A[2][k+1]][4][0], leg_moves[A[2][k]][A[2][k+1]][4][1])
						time.sleep(2)
						if A[2][k+1] in hum_not_reach_inner:
							simu.rpc('human', 'move', leg_moves[A[2][k]][A[2][k+1]][5][0], leg_moves[A[2][k]][A[2][k+1]][5][1])
						if A[3][k+1] not in hum_not_reach_outer or A[3][k+1] not in hum_not_reach_inner:
							print("Operator's arm moves from %s to %s" %(A[2][k+1], A[3][k+1])) #when human comes to the new position, leg and arm at the same position, so I took A[2][k+1]
							simu.rpc('human', 'toggle_manipulation')
							time.sleep(2)
							simu.rpc('human', 'move_hand', arm_moves_diff[A[2][k+1]][A[3][k+1]][0], arm_moves_diff[A[2][k+1]][A[3][k+1]][1])
					elif (A[2][k] not in hum_reachability_from_init and A[2][k+1] not in hum_reachability_from_init):
						if A[3][k]==A[3][k+1]:
							print("Operator's arm stays at %s" %(A[3][k]))
						else:
							print("Operator's arm moves from %s to %s" %(A[3][k], A[3][k+1]))
							if A[3][k+1] not in human_not_reach_outer:
								if A[3][k] in human_not_reach_inner or A[3][k] in human_not_reach_outer:
									simu.rpc('human', 'toggle_manipulation')
									time.sleep(2)
								simu.rpc('human', 'move_hand', arm_moves[A[3][k]][A[3][k+1]][0], arm_moves[A[3][k]][A[3][k+1]][1])
							if A[3][k+1] in human_not_reach_outer:
								simu.rpc('human', 'toggle_manipulation')
						
					if len(B[k+1])== 1:
						if B[k+1][0]== '0':
							print("There is no hazard occured.")
						else:
							for i in D:
								if B[k+1][0] == i:
									o=D.index(i)
									print("Hazard number %s occured."%(o+1))
									if (o>=0) and (o<=15):
										print("Tr on %s by %s"%(E[o][0], E[o][1]))
									elif (o<=16) and (o>=28):
										print("Qs on %s by %s"%(E[o][0], E[o][1]))
									print("Hazard number %s has a risk value %s" %((o+1), C[o][k+1]))
					else:
						for i in D:
							if B[k+1][-1] == i:
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
