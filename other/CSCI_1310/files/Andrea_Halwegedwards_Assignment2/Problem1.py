#List input requests.
PV = float(input("Please input your present value. "))
i = float(input("Please input your interest rate. "))
n = float(input
("Please input the number of years your money will be invested. "))

#Calculate future worth
FV = PV*pow((1+i), n)
print(FV)

#Print result
string = "The future value of your investment will be $%.2f" % FV
print(string)
