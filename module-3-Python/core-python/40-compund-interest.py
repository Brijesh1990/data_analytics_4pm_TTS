# w.a.p to calculate compound  interest 
import math
p=int(input("Enter principle amount :"))
n=int(input("Enter Number of years  :"))
r=int(input("Enter ROI  :"))
# compound interest is 
ci=p*math.pow((1+r/100),n)
print("paid a compound interest is   :",ci)
