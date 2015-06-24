#!usr/local/bin/python3

def rating(completions, attempts, yards, touchdowns, interceptions):
    C = (completions/attempts - 0.30) * 5
    Y = (yards/attempts - 3) * 0.25
    T = touchdowns/ attempts * 20
    I = 2.375 - (interceptions/attempts * 25)
    rating = (C + Y + T + I) / 6 * 100
    return("%.2f" % rating)

def clean(split_file_list):
    cleaned = [[line.strip("\n") for line in stats] for stats in split_file_list]
    return(cleaned)

def readFile(file_name):
    split_file_list = [line.split(",") for line in open(file_name, "r")]
    cleaned = clean(split_file_list)
    #  actually calculate the rating
    total_passer_rating = 0
    output = []
    for player_stats in cleaned:
        name = player_stats[0]
        completions = int(player_stats[1])
        attempts = int(player_stats[2])
        yards = int(player_stats[3])
        touchdowns = int(player_stats[4])
        interceptions = int(player_stats[5])
        rating1 = rating(completions, attempts, yards, touchdowns, interceptions)
        total_passer_rating += float(rating1)
        
        output.append([name + ": " + rating(completions, attempts, yards, touchdowns, interceptions)])
    
    writeFile(total_passer_rating)
    return(output)
    



def writeFile(total_passer_rating):
	new_file = open("/Users/Andrea/Desktop/QBoutput.txt", "w")
	new_file.write("Total passer rating is " + str(total_passer_rating))
	new_file.close()



print(readFile("/Users/Andrea/Desktop/Statistics.csv"))
