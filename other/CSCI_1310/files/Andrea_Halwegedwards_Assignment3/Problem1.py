#Input parameters
pass_comp = int(input("Enter quaterback pass completions. "))
pass_attmps = int(input("Enter quaterback pass attempts. "))
tot_pass_yrds = float(input("Enter total passing yards. "))
touchdowns = int(input("Enter number of touchdowns. "))
interceptions = int(input("Enter number of interceptions. "))

#Calculated variables
completions_per_attempt = float(pass_comp / pass_attmps)
yards_per_attempt = tot_pass_yrds / pass_attmps
tcdwns_per_attempt = float(touchdowns / pass_attmps)
interceptions_per_attempt = float(interceptions / pass_attmps)

C = (completions_per_attempt - 0.30) * 5
Y = (yards_per_attempt - 3) * 0.25
T = tcdwns_per_attempt * 20
I = 2.375 - (interceptions_per_attempt * 25)
PasserRating = (C + Y + T + I) / 6 * 100

#Print result
print("The passer rating is %.2f" % PasserRating)
