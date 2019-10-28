#name = "asd"
#searchfile = open("den.txt", "r")
with open('output.hist.txt', 'r') as f_orig, open('values.txt', 'w') as f_new, open('den.txt', 'w') as f_den:
	for line in f_orig:
		i=0
		while (i < 16):
			if "------ time %d" % (i) in line:
				f_new.write(line)
				i=i+1
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
						f = line[-2:]
						f_den.write(f)
					if "OPERATOR_1_HEAD_AREA_IN_L_" in line:
						f_new.write(line)
						e = line[-2:]
						f_den.write(e)
					if "------ time %d" % (i) in line:
						break

