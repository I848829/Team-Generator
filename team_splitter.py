import csv
import sys
import itertools
from player import Player

playerList = []
ifile = open('resource/ICSVTeamOuting.csv', "rb")
reader = csv.reader(ifile)
num_teams = 6


def extractActivities(activitiesColumn):
    return activitiesColumn.split(';')


def subtract(list_a):
    list_b = []
    for player in playerList:
        if player not in list_a:
            list_b.append(player)

    return list_b


def checkValidityActivity(teams, activity):
    maximum = -sys.maxint - 1
    minimum = sys.maxint
    for team in teams:
        maximum = max(maximum, getNumOfPlayerForActivity(team, activity))
        minimum = min(minimum, getNumOfPlayerForActivity(team, activity))

    return maximum-minimum < 2


def getNumOfPlayerForActivity(team, activity):
    number = 0
    for player in team:
        if player.likesActivity(activity):
            number += 1

    return number


def getFemaleNumber(team):
    number = 0
    for player in team:
        if player.gender == 'Female':
            number += 1
    return number


def checkValidityGender(teams):
    maximum = -sys.maxint - 1
    minimum = sys.maxint
    for team in teams:
        maximum = max(maximum, getFemaleNumber(team))
        minimum = min(minimum, getFemaleNumber(team))

    return maximum-minimum < 2


def checkValidity(teams, activities):
    if not checkValidityGender(teams):
        return False
    for activity in activities:
        if not checkValidityActivity(teams, activity):
            return False
    return True


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
            if colnum == 1:
                name = col
            elif colnum == 3:
                activities = extractActivities(col)
            elif colnum == 2:
                gender = col

            colnum += 1

        player = Player(name, gender, activities)
        playerList.append(player)

    rownum += 1


ifile.close()

count = 0
activities = ['Soccer', 'Basketball', 'Ultimate Frisbee']
permutations = itertools.permutations(playerList)
for permutation in permutations:
    teams = [permutation[i::num_teams] for i in range(num_teams)]
    if checkValidity(teams, activities):
        for j in range(len(teams)):
            print "----- Team ", j, " -----"
            for activity in activities:
                print activity, ": ", getNumOfPlayerForActivity(teams[j], activity)
            print "Female: ", getFemaleNumber(teams[j])
            for member in teams[j]:
                print member.name
        break
    count += 1
    if count % 1000 == 0:
        print count
