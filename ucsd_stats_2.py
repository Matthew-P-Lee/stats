#calulating confidence intervals of the estimated mean 
import math
import numpy as np
import scipy as sp
import scipy.stats as ss

#calculating it when you have mean, std, and n
x = 1123.00
n = 1783.00
alpha = .10

#point estimate for a parameter of a normal distribution
#determine p_hat as the sample mean
p_hat = x/n

#compute the sample standard deviation
std = math.sqrt((p_hat*(1-p_hat))/n)

#standard error E
E = std / math.sqrt(n)

#create a normal distribution and get the z score of z sub alpha /2
pd = ss.norm(loc = 0, scale = 1)
z = abs(pd.ppf((alpha/2)))

#get the cofidence intervals about the mean
lbound = p_hat - (z * std)
ubound = p_hat + (z * std)

print "p hat: " + "{0:.3f}".format(p_hat)
print "std: " + "{0:.3f}".format(std)
print("E: " + "{0:.3f}".format(E))
print("z score: " + "{0:.3f}".format(z))
print("lbound: " + "{0:3f}".format(lbound))
print("ubound: " + "{0:3f}".format(ubound))

