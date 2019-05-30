from collections import defaultdict

position = defaultdict(list)



with open('output.hist.txt', 'r') as f_orig, open('values.txt', 'w') as f_new, open('den.txt', 'w') as f_den:
	for line in f_orig:
		i=1
		while (i < 16):
			if "------ time %d" % (i) in line:
				f_new.write(line)
				i=i+1
				for line in f_orig:
					if "BASE_1_IN_L_" in line:
						position['base'].append(line[-2:])
						print(position['base'])
					if "LINK1_1_IN_L_" in line:
						position['link_1'].append(line[-2:])
						print(position['link_1'])
					if "LINK2_1_IN_L_" in line:
						position['link_2'].append(line[-2:])
						print(position['link_2'])
					if "ENDEFF_1_IN_L_" in line:
						position['endeff'].append(line[-2:])
						print(position['endeff'])
					if "OPERATOR_1_ARM_AREA_IN_L_" in line:
						position['arm'].append(line[-2:])
						print(position['arm'])
					if "OPERATOR_1_HEAD_AREA_IN_L_" in line:
						position['head'].append(line[-2:])
						print(position['head'])
					if "------ time %d" % (i) in line:
						break

