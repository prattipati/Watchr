class Game:
    def __init__(self, data):
        self.home = data['home']
        self.home_score = int(data['home_score'])
        self.away = data['away']
        self.away_score = int(data['away_score'])
        self.link = data['url']
        self.point_difference = self.home_score-self.away_score
