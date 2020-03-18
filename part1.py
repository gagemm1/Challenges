'''
public interface ICalculateOhmValues
{
    /// <summary>
    /// Calculates the Ohm value of a resistor based on the band colors.
    /// </summary>
    /// <param name="bandAColor">The color of the first figure of component value band.</param>
    /// <param name="bandBColor">The color of the second significant figure band.</param>
    /// <param name="bandCColor">The color of the decimal muliplier band.</param>
    /// <param name="bandDColor">The color of the tolerance value band.</param>
    int CalculateOhmValue(string bandAColor, string bandBColor, string bandCColor, string bandDColor)
}
'''

'''
Based on the above function and the problem description, I interpret you want
a made up function to take in those parameters and spit out a resistance
'''

#import pandas and read band color entries from csv to calculate resistance for each and put into dataframe
#5 possible colors for each band

#import pandas for dataframe use
import pandas as pd

#read color codes, colors correspond to a color 1 to 5
dataset = pd.read_csv('colorCodes.csv')

#initialize variables and call calculateohmvalue for each row in the dataframe
def ICalculateOhmValues():
	i = 0
	while i < len(dataset):
		bandA = dataset.iloc[i,0]
		bandB = dataset.iloc[i,1]
		bandC = dataset.iloc[i,2]
		bandD = dataset.iloc[i,3]
		i += 1
		CalculateOhmValue(bandA,bandB,bandC,bandD)
	

def CalculateOhmValue(bandA,bandB,bandC,bandD):
	#average for determining if a wire is out of spec
	averageRatings = (bandA + bandB + bandC + bandD) / 4
	#initial values of specs
	cats = "No"
	tempRating = "Less than 200"
	shockRated = "not"
	#hot is none because the wires are always hot
	hot = None
	if averageRatings < 1 or averageRatings > 5:
		#alternative is print
		#print("This wire is out of spec, replace wires")
		return "This wire is out of spec, replace wires"
	else:
		if 2 < bandA > 1:
			tempRating = "In between 200 and 500"
		if bandB > 2:
			cats = "yes"
		if bandC == 5:
			shockRated = ""
		if bandD:
			hot = "always"
		#alternative is print
		print("This wire's temperature rating is",tempRating, "cats are a",cats,",shocks are",shockRated,"ok and after shock the resistor is",hot,"hot")
		return "This wire's temperature rating is",tempRating, "cats are a",cats,",shocks are",shockRated,"ok and after shock the resistor is",hot,"hot"
ICalculateOhmValues()
