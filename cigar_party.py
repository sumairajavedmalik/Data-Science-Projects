def cigar_party(cigars, is_weekend):
	if cigars>=40 and cigars<=60:
		return True
	elif cigars>=40 and is_weekend==True:
		return True
	else:
		return False