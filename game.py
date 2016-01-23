class Game:
    def __init__(self, data):
        self.home = str(data['home']['text'])
        self.away = str(data['away']['text'])
        try:
            self.home_score = int(data['home_score'])
            self.away_score = int(data['away_score'])
            self.link = str(data['url'])
        except KeyError:
            self.home_score = 0
            self.away_score = 0
            self.link = "Game has not started yet"
        self.point_difference = self.home_score-self.away_score

    def __str__(self):
        res = self.away + " at " + self.home + "\n" + str(self.away_score) + " - " + str(self.home_score) + "\n" + self.link
        return res
