import numpy as np
import scipy as sp

#some sample data to work with
a  = [65,66,67,66,67,70,67,70,71,68]

#it helps to use numpy arrays
a = np.array(a)

#really basic stuff
print(a)
print 'mean: ' + str(np.mean(a))
print 'median: ' + str(np.median(a))
print 'standard deviation: ' + str(np.std(a))

# sample variance 
# note if you need to get a sample variance you need to set the N-1 parameter, otherwise it will default to zero (population variance)
print 'Sample variance: ' + str(a.var(ddof=1))

#Determine the Z-score
x = 6
mu = 16
sigma = 1.9 

#defines the z-score for an observed value (x) when given the mean and std deviation
def zscore(x,mu,sigma):
	return ((x-mu)/sigma)	

print 'z-score:' + str(zscore(x,mu,sigma))

# determining an r value using the Pearson Linear Correlation Coefficient
# to determine the relationship between two values
from scipy.stats import pearsonr

x = [1,3,3,6,7]
y = [18,13,9,6,4]

lcc = pearsonr(x,y)
print 'Pearson coefficient: ' + str(lcc[0])

#computing the slope of a regression line y = mx + b
#the equation to determine slope of a line is y-y1 = m(x-x1)

x = [3,6]
y = [5.7,1.9]

#solve for m
m = (y[0] - y[1]) / (x[0] - x[1])

#just printing out the equation
print 'y = ' + str(m) + 'x' + ' + ' + str((m * -x[1]) + y[1])

# example of computing a least-squares regression analysis
# the equation of a line that represents the sum of the squares of least residual errors
# for reference the equation of a line is y-y1 = m(x-x1)
# y hat = b1x + b0

x = [35,50,75,95,120,130,145,155,160,175,185,190]
y = [5.88,5.99,6.74,6.1,7.47,6.93,6.42,7.97,7.92,7.62,6.89,7.9]

print 'std of x: ' + str(np.std(x))
print 'std of y: ' + str(np.std(y))
print 'lcc of x: ' + str(pearsonr(x,y)[0])

# first compute the slope of the least squares regression b1 given x,y
b1 = pearsonr(x,y)[0] * (np.std(y)/np.std(x	))

#now solve for the y-intercept given x,y
b0 = np.mean(y) - (b1 * np.mean(x))

#Solve for y hat using 130 as the explanatory variable
yhat = (b1 * 130) + b0

print 'y hat: ' + str(yhat) 

#computing the sum of squared residuals
sumres = 0

for i, v in enumerate(x):
	yhat = (b1 * v) + b0 #compute y hat
	res = y[i] - yhat #difference between the actual (y) and predicted score (y hat)
	sumres = sumres + (res*res) 

print 'sum of squared residuals: ' + str(sumres)

#determine r squared - coefficient of determination
r = pearsonr(x,y)[0]
print 'r squared: ' + str(int(r*r * 100)) + '%'





