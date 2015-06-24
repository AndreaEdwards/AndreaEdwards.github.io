#List variables
days_per_year = 365
hours_per_day = 24
minutes_per_hour = 60
seconds_per_minute = 60
seconds_per_day = hours_per_day * minutes_per_hour * seconds_per_minute

births_per_second = float(1 / 7)
deaths_per_second = float(1 / 13)
immigrants_per_second = float(1 / 35)

#Calculate additional people per year
births_per_year = births_per_second * seconds_per_day * days_per_year
deaths_per_year = deaths_per_second * seconds_per_day * days_per_year
immigrants_per_year = immigrants_per_second * seconds_per_day * days_per_year
census = 330357870

#Print current census and census after one year
print(census)
print(int(census + births_per_year - deaths_per_year + immigrants_per_year))
