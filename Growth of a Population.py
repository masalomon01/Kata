# 7kyu
def nb_year(p0, percent, aug, p):
	percent, years, pn = (percent * .01) + 1, 0, p0
	while pn < p:
		pn = pn * percent + aug
		years+=1
	
	return years



print(nb_year(1500, 5, 100, 5000)) #, 15)
print(nb_year(1500000, 2.5, 10000, 2000000)) #, 10)
print(nb_year(1500000, 0.25, 1000, 2000000)) #, 94)