import csv
import itertools
from player import Player

playerList = []
ifile = open('resource/questionnaire.csv', "rb")
reader = csv.reader(ifile)


def extractActivities(activitiesColumn):
    return activitiesColumn.split(';')


def subtract(list_a):
    list_b = []
    for player in playerList:
        if player not in list_a:
            list_b.append(player)

    return list_b


def checkValidityActivity(team_a, team_b, activity):
    team_a_activity_num = getNumOfPlayerForActivity(team_a, activity)
    team_b_activity_num = getNumOfPlayerForActivity(team_b, activity)

    return abs(team_a_activity_num-team_b_activity_num) < 2


def getNumOfPlayerForActivity(team, activity):
    number = 0
    for player in team:
        if player.likesActivity(activity):
            number += 1

    return number


def getFemaleNumber(team):
    number = 0
    for plyaer in team:
        if player.gender == 'f':
            number += 1
    return number


def checkValidityGender(team_a, team_b):
    team_a_female_num = getFemaleNumber(team_a)
    team_b_female_num = getFemaleNumber(team_b)

    return abs(team_a_female_num-team_b_female_num) < 2


def checkValidity(team_a, team_b):
    return checkValidityActivity(team_a, team_b, 'Basketball') and checkValidityActivity(team_a, team_b, 'Volleyball') and checkValidityActivity(team_a, team_b, 'Soccer') and checkValidityGender(team_a, team_b)


rownum = 0
for row in reader:
    if rownum == 0:
        header = row
    else:
        colnum = 0

        name = ''
        gender = ''
        activities = []

        for col in row:
            if colnum == 2:
                name = col
            elif colnum == 3:
                activities = extractActivities(col)
            elif colnum == 7:
                gender = col

            colnum += 1

        player = Player(name, gender, activities)
        playerList.append(player)

    rownum += 1


ifile.close()

combinationList = list(itertools.combinations(playerList, len(playerList)/2))

for combination in combinationList:
    team_b = subtract(combination)
    if checkValidity(combination, team_b):
        print "----- Team A -----"
        print "Volleyball: ", getNumOfPlayerForActivity(combination, 'Volleyball')
        print "Basketball: ", getNumOfPlayerForActivity(combination, 'Basketball')
        print "Soccer: ", getNumOfPlayerForActivity(combination, 'Soccer')
        print "#####"
        for player in combination:
            print player.name
        print "----- Team B -----"
        print "Volleyball: ", getNumOfPlayerForActivity(team_b, 'Volleyball')
        print "Basketball: ", getNumOfPlayerForActivity(team_b, 'Basketball')
        print "Soccer: ", getNumOfPlayerForActivity(team_b, 'Soccer')
        print "#####"
        for player in team_b:
            print player.name
        break
