




def normal_range(r):
	# Just a simple replacement for the x's.
	starting = r.replace("x", "0")
	ending = r.replace("x", "255")
	return starting, ending



def lined_range(r):
	r = str(r).split(".")

	# Copies from the original IP address.
	copy1 = r.copy()
	copy2 = r.copy()


	for d in r:
		if "-" in d:

			# Splitting and finding the lined range.
			pos = r.index(d)
			u = d.split("-")

			# Set the first range to the right starting position.
			u1 = u[0]
			copy1[pos] = u1


			# Set the second range to the right starting position.
			u2 = u[1]
			copy2[pos] = u2
	
	starting = ".".join(copy1).replace("x", "0")
	ending = ".".join(copy2).replace("x", "255")


	return starting, ending




if __name__ == "__main__":
	lined_range()
	normal_range()