#!usr/local/bin/python3

# step 1: see the common formula and capture it in a function
# step 2: 

def rating(completions, attempts, yards, touchnowns, interceptions):
    C = (completions/attempts - 0.30) * 5
    Y = (yards/attempts - 3) * 0.25
    T = touchdowns/ attempts * 20
    I = 2.375 - (interceptions/attempts * 25)
    rating = (C + Y + T + I) / 6 * 100
    print("%.2f" % rating)

for record in open("ratings.csv", "r"):
    fields = record.split(",")  # parsing the line
    cleaned = []
    for field in fields:
        cleaned.append(field.strip())  # strip() takes out anything that is white space
    print(cleaned)

    #  actually calculate the rating
    name = cleaned[0]
    completions = int(cleaned[1])
    attempts = int(cleaned[2])
    yards = int(cleaned[3])
    touchdowns = int(cleaned[4])
    interceptions = int(cleaned[5])

    rating(completions, attempts, yards, touchdowns, interceptions)


def clean(values):
    cleaned = []
    for field in values:
        cleaned.append(field.strip())  # strip() takes out anything that is white space
    return(cleaned)


for record in open("ratings.csv", "r"):
    fields = record.split(",")  # parsing the line
    cleaned = clean(fields)    


    
    #  actually calculate the rating
    name = cleaned[0]
    completions = int(cleaned[1])
    attempts = int(cleaned[2])
    yards = int(cleaned[3])
    touchdowns = int(cleaned[4])
    interceptions = int(cleaned[5])

    rating(completions, attempts, yards, touchdowns, interceptions)
