 def eligibility_check() :
	x = int(input("ENTER AGE TO PERFORM CHECK : "))
	if x >= 18 :
		status = "ELIGIBLE"
	else :
		status = "NOT ELIGIBLE"
	print("THE PERSON IS ",status," FOR VOTING")
