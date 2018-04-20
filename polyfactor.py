#should REALLY get this commented up
import math


ffac = 0
sfac = 0

a = int(input("Input the a of the polynomial: "))
b = int(input("Input the b of the polynomial: "))
c = int(input("Input the c of the polynomial: "))
ac = a * c
radical = 1


def findgcf(a, b): #returns the greatest common factor of a and b with the sign of b
    while b:
        a, b = b, a%b
    return int(a)

def radicalreduce(radical):#returns a reduced radical in the form x*sqrt(y)
	radreturn = ""
	gf = 1
	a = 1
	if(radical < 0): #divide out an i if applicable
		radreturn = "i"
		radical = abs(radical)
	for i in range (1, 100): #check if it is a perfect square and return the root if it is
		if (i**2 == radical):
			radreturn = str(math.sqrt(radical))

	for i in range (1, 100): #brute force check if radical is divisible by any perfect square

		a = i**2
		#print(str(i) + " was checked")
		if(radical % a == 0) and (a != radical): #record the largest perfect square that divides radical
			if(a > gf):
				gf = a

	if (gf == 1): #if there is no perfect square factor, return the input radical in a square root sign
		radreturn = radreturn + "(" + u'\u221a' + str(int(radical)) + ")"
		#print("We got here")
	else: #return a big ugly string that says the 
		#print("GF = " + str(gf))
		radreturn = str(int(math.sqrt(gf))) + radreturn + u'\u221a' + str(int(radical / gf))

	return(radreturn)



def quadsolve(x, y, z): #prints the result of the quadratic formula in radical form + decimal form if real
	radreturn = radicalreduce((y**2) - (4 * x * z))
	if (4 * x * z) > (y**2):
		print("(" + str(-y) + " " + u"\u00b1" + " " + str(radreturn) + ")/" + str(2 * x))
	else:
		quadpos = (-y + math.sqrt((y**2) - (4 * x * z))) / (2 * x)
		quadneg = (-y - math.sqrt((y**2) - (4 * x * z))) / (2 * x)
		print("(" + str(-y) + u" \u00b1 " + str(radreturn) + ")/" + str(2 * x))
		print(str(quadpos) + " or " + str(quadneg)) #this only outputs raw values, should adjust to output stuff w/sqrts as well

def polyfactor(a, b, c): #take the three given inputs
	for i in range (-100, 100): #brute force check
		if (i == 0):
			continue
		ffac = (ac / i) #divide the ac by i for the check
		sfac = (ac / ffac) #take the co-factor of ac
		if (ffac + sfac) == b and (ac % ffac) == 0: #if the two factors also add up to the b, continue. simulates factoring by grouping

#ffac and a become the two terms of the first grouping, sfac and c become the two terms of second grouping

			firstgcf = int(findgcf(int(ffac), a)) #simulate factoring by grouping by finding gcf of two grouped terms and recording it
			secgcf = int(findgcf(c, int(sfac)))

			fpodfterm = a / firstgcf
			fpodsterm = ffac / firstgcf

			spodfterm = firstgcf
			spodsterm = secgcf

			fpodgcf = abs(findgcf(fpodfterm, fpodsterm)) #find the gcf of each pod, only positive ints
			spodgcf = abs(findgcf(spodfterm, spodsterm))
			
			fpodfterm = int(fpodfterm / fpodgcf) #divide through by gcf of the respective pod
			fpodsterm = int(fpodsterm / fpodgcf)
			spodfterm = int(spodfterm / spodgcf)
			spodsterm = int(spodsterm / spodgcf)

			if(fpodgcf == 1) or (fpodgcf == -1): #if the gcf is 1, null the variable so it doesn't show up
				fpodgcf = ""
			if(spodgcf == 1) or (spodgcf == -1):
				spodgcf = ""

			print(str(fpodgcf) + str(spodgcf) + "(" + str(int(fpodfterm)) + "x + " + str(int(fpodsterm)) + ")(" + str(spodfterm) + "x + " + str(spodsterm) + ")")
			#print("firstgcf = " + str(firstgcf))
			#print("secgcf = " + str(secgcf))
			#print("ffac = " + str(ffac))
			#print("sfac = " + str(sfac))
			break
		if (i == 99): #if no soln is found, send the data to the quadsolve function
			quadsolve(a, b, c)

polyfactor(a, b, c)