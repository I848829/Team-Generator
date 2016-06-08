class Player:

    def __init__(self, name, gender, activities):
        self.name = name
        self.gender = gender
        self.activities = activities

    def likesActivity(self, activity):
        return activity in self.activities
