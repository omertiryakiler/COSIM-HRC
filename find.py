#name = "asd"
#searchfile = open("den.txt", "r")
with open('output.hist.txt', 'r') as f_orig, open('values.txt', 'w') as f_new, open('den.txt', 'w') as f_den:
	for line in f_orig:
		if "------ time 0" in line:
			f_new.write(line)
			for line in f_orig:
				if "BASE_1_IN_L_" in line:
					f_new.write(line)
				if "LINK1_1_IN_L_" in line:
					f_new.write(line)
				if "LINK2_1_IN_L_" in line:
					f_new.write(line)
				if "ENDEFF_1_IN_L_" in line:
					f_new.write(line)
				if "OPERATOR_1_ARM_AREA_IN_L_" in line:
					f_new.write(line)
				if "OPERATOR_1_HEAD_AREA_IN_L_" in line:
					f_new.write(line)
				if "------ time 1" in line:
					break
		if "------ time 1 -" in line:
			f_new.write(line)
			for line in f_orig:
				if "BASE_1_IN_L_" in line:
					f_new.write(line)
					a = line[-2:]
					f_den.write(a)
				if "LINK1_1_IN_L_" in line:
					f_new.write(line)
					b = line[-2:]
					f_den.write(b)
				if "LINK2_1_IN_L_" in line:
					f_new.write(line)
					c = line[-2:]
					f_den.write(c)
				if "ENDEFF_1_IN_L_" in line:
					f_new.write(line)
					d = line[-2:]
					f_den.write(d)
				if "OPERATOR_1_ARM_AREA_IN_L_" in line:
					f_new.write(line)
					e = line [-2:]
					f_den.write(e)
				if "OPERATOR_1_HEAD_AREA_IN_L_" in line:
					f_new.write(line)
					f = line [-2:]
					f_den.write(f)
				if "------ time 2" in line:
					break
		if "------ time 2 -" in line:
			f_new.write(line)
			for line in f_orig:
				if "BASE_1_IN_L_" in line:
					f_new.write(line)
					a2 = line[-2:]
					f_den.write(a2)
				if "LINK1_1_IN_L_" in line:
					f_new.write(line)
					b2 = line[-2:]
					f_den.write(b2)
				if "LINK2_1_IN_L_" in line:
					f_new.write(line)
					c2 = line[-2:]
					f_den.write(c2)
				if "ENDEFF_1_IN_L_" in line:
					f_new.write(line)
					d2 = line[-2:]
					f_den.write(d2)
				if "OPERATOR_1_ARM_AREA_IN_L_" in line:
					f_new.write(line)
					e2 = line [-2:]
					f_den.write(e2)
				if "OPERATOR_1_HEAD_AREA_IN_L_" in line:
					f_new.write(line)
					f2 = line [-2:]
					f_den.write(f2)
				if "------ time 3" in line:
					break
		if "------ time 3 -" in line:
			f_new.write(line)
			for line in f_orig:
				if "BASE_1_IN_L_" in line:
					f_new.write(line)
					a3 = line[-2:]
					f_den.write(a3)
				if "LINK1_1_IN_L_" in line:
					f_new.write(line)
					b3 = line[-2:]
					f_den.write(b3)
				if "LINK2_1_IN_L_" in line:
					f_new.write(line)
					c3 = line[-2:]
					f_den.write(c3)
				if "ENDEFF_1_IN_L_" in line:
					f_new.write(line)
					d3 = line[-2:]
					f_den.write(d3)
				if "OPERATOR_1_ARM_AREA_IN_L_" in line:
					f_new.write(line)
					e3 = line [-2:]
					f_den.write(e3)
				if "OPERATOR_1_HEAD_AREA_IN_L_" in line:
					f_new.write(line)
					f3 = line [-2:]
					f_den.write(f3)
				if "------ time 4 -" in line:
					break
		if "------ time 4 -" in line:
			f_new.write(line)
			for line in f_orig:
				if "BASE_1_IN_L_" in line:
					f_new.write(line)
					a4 = line[-2:]
					f_den.write(a4)
				if "LINK1_1_IN_L_" in line:
					f_new.write(line)
					b4 = line[-2:]
					f_den.write(b4)
				if "LINK2_1_IN_L_" in line:
					f_new.write(line)
					c4 = line[-2:]
					f_den.write(c4)
				if "ENDEFF_1_IN_L_" in line:
					f_new.write(line)
					d4 = line[-2:]
					f_den.write(d4)
				if "OPERATOR_1_ARM_AREA_IN_L_" in line:
					f_new.write(line)
					e4 = line [-2:]
					f_den.write(e4)
				if "OPERATOR_1_HEAD_AREA_IN_L_" in line:
					f_new.write(line)
					f4 = line [-2:]
					f_den.write(f4)
				if "------ time 5 -" in line:
					break
		if "------ time 5 -" in line:
			f_new.write(line)
			for line in f_orig:
				if "BASE_1_IN_L_" in line:
					f_new.write(line)
					a5 = line[-2:]
					f_den.write(a5)
				if "LINK1_1_IN_L_" in line:
					f_new.write(line)
					b5 = line[-2:]
					f_den.write(b5)
				if "LINK2_1_IN_L_" in line:
					f_new.write(line)
					c5 = line[-2:]
					f_den.write(c5)
				if "ENDEFF_1_IN_L_" in line:
					f_new.write(line)
					d5 = line[-2:]
					f_den.write(d5)
				if "OPERATOR_1_ARM_AREA_IN_L_" in line:
					f_new.write(line)
					e5 = line [-2:]
					f_den.write(e5)
				if "OPERATOR_1_HEAD_AREA_IN_L_" in line:
					f_new.write(line)
					f5 = line [-2:]
					f_den.write(f5)
				if "------ time 6 -" in line:
					break
		if "------ time 6 -" in line:
			f_new.write(line)
			for line in f_orig:
				if "BASE_1_IN_L_" in line:
					f_new.write(line)
					a6 = line[-2:]
					f_den.write(a6)
				if "LINK1_1_IN_L_" in line:
					f_new.write(line)
					b6 = line[-2:]
					f_den.write(b6)
				if "LINK2_1_IN_L_" in line:
					f_new.write(line)
					c6 = line[-2:]
					f_den.write(c6)
				if "ENDEFF_1_IN_L_" in line:
					f_new.write(line)
					d6 = line[-2:]
					f_den.write(d6)
				if "OPERATOR_1_ARM_AREA_IN_L_" in line:
					f_new.write(line)
					e6 = line [-2:]
					f_den.write(e6)
				if "OPERATOR_1_HEAD_AREA_IN_L_" in line:
					f_new.write(line)
					f6 = line [-2:]
					f_den.write(f6)
				if "------ time 7 -" in line:
					break
	A = (a, a2, a3)	
	print(A)
