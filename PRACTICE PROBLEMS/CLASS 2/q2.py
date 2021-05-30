#PROGRAM TO CHECK WHETHER A NUMBER IS POSITIVE OR NEGATIVE
def posneg() :
	x = int(input("ENTER A NUMBER TO PERFORM CHECK : "))
	if x > 0 :
		print("POSITIVE NUMBER")
	elif x < 0 :
		print("NEGATIVE NUMBER")
	else :
		print("ZERO")
