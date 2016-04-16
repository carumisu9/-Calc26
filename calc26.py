
def convert_26_to_10(x):
	
	length = len(x)
	x = ",".join(x)
	x = x.split(",")
	x.reverse()
	sum = 0

	for i in range(length):
		sum += alpha_2_num(x[i]) * 26**i

	return sum

def convert_10_to_26(x):

	ret = []
	q = x
	end_flag = False

	if 26 > x:
		return num_2_alpha(x)

	while not end_flag:
		tmp = q / 26
		r = q % 26
		q = tmp
		ret.append(num_2_alpha(r))
		if 26 > q:
			end_flag = True
			ret.append(num_2_alpha(q))

	ret.reverse()
	ret = "".join(ret)

	return ret


def alpha_2_num(c):
	if c == 'A':
		return 0
	elif c == 'B':
		return 1
	elif c == 'C':
		return 2
	elif c == 'D':
		return 3
	elif c == 'E':
		return 4
	elif c == 'F':
		return 5
	elif c == 'G':
		return 6
	elif c == 'H':
		return 7
	elif c == 'I':
		return 8
	elif c == 'J':
		return 9
	elif c == 'K':
		return 10
	elif c == 'L':
		return 11
	elif c == 'M':
		return 12
	elif c == 'N':
		return 13
	elif c == 'O':
		return 14
	elif c == 'P':
		return 15
	elif c == 'Q':
		return 16
	elif c == 'R':
		return 17
	elif c == 'S':
		return 18
	elif c == 'T':
		return 19
	elif c == 'U':
		return 20
	elif c == 'V':
		return 21
	elif c == 'W':
		return 22
	elif c == 'X':
		return 23
	elif c == 'Y':
		return 24
	elif c == 'Z':
		return 25

def num_2_alpha(x):
	if x == 0:
		return 'A'
	elif x == 1:
		return 'B'
	elif x == 2:
		return 'C'
	elif x == 3:
		return 'D'
	elif x == 4:
		return 'E'
	elif x == 5:
		return 'F'
	elif x == 6:
		return 'G'
	elif x == 7:
		return 'H'
	elif x == 8:
		return 'I'
	elif x == 9:
		return 'J'
	elif x == 10:
		return 'K'
	elif x == 11:
		return 'L'
	elif x == 12:
		return 'M'
	elif x == 13:
		return 'N'
	elif x == 14:
		return 'O'
	elif x == 15:
		return 'P'
	elif x == 16:
		return 'Q'
	elif x == 17:
		return 'R'
	elif x == 18:
		return 'S'
	elif x == 19:
		return 'T'
	elif x == 20:
		return 'U'
	elif x == 21:
		return 'V'
	elif x == 22:
		return 'W'
	elif x == 23:
		return 'X'
	elif x == 24:
		return 'Y'
	elif x == 25:
		return 'Z'


