import csv 
from pathlib import Path 

csv_file = Path("Premier 16-17.csv")

def check_file_exists(csv_file): 
    return csv_file.is_file()
        
def read_csv(csv_file):
    csv_contents = []
    if check_file_exists(csv_file):
        with open(csv_file) as csvfile:
            reader = csv.reader(csvfile, delimiter=",")
            next(reader)                  ###   skip first row (header)
            for row in reader:
                csv_contents.append(row)
    return csv_contents

def process_results(rows):
    dictionary = {}
    for row in rows:
        home = row[1]
        away = row[2]
        goals_by_home = row[3]
        goals_by_away = row[4]
        winner = row[5]
        home,away,homegoals,awaygoals,winner=row[1],row[2],row[3],row[4],row[5]
        if home not in dictionary:
            dictionary[home] = [0,0,0,0,0,0,0] #winner, draw, loss, goal dif, points, shots, target shots
        if away not in dictionary:
            dictionary[away] = [0,0,0,0,0,0,0]
        dictionary[home][5] += goals_by_home
        dictionary[away][5] += goals_by_away
        if winner == "D":
            dictionary[home][4] += 1
            dictionary[away][4] += 1
            dictionary[home][1] += 1
            dictionary[home][1] += 1
        if winner == "A":
            dictionary[away][4] += 3
            dictionary[home][2] += 1
            dictionary[away][0] += 1
        if winner == "H":
            dictionary[home][0] += 1
            dictionary[home][4] += 3
            dictionary[away][2] += 1
        goal_difference = abs(dictionary[row][7] - dictionary[row][8])
        dictionary[home][3] += goal_difference
        dictionary[away][3] += goal_difference
        
        home_shots += row[7]
        dictionary[home][5] += home_shots
        home_shots_target += row[9]
        dictionary[home][6] += home_shots_target
        away_shots += row[8]
        away_shots_target += row[10]
        
        
        
if __name__ == "__main__":
    file_contents = read_csv(csv_file)
    print(process_results(file_contents))
