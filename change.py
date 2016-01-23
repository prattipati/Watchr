import json

fav_teams = []
def configure():
    while(True):
        config = {}
        max_diff = input("Enter the maximium point difference in games to be found: ")
        try:
            config["max_point_difference"] = int(max_diff)
            break
        except ValueError:
            print("Please enter a number.")

    while(True):
        team_to_add = input("Enter the name of a favorite team to add to config: ")
        fav_teams.append(team_to_add)
        config["fav_teams"] = fav_teams
        more = input("If finished adding teams, type 'save' to save config and quit. If not, press enter: ")
        if more == "save" or  more == "Save":
            print("Team(s) added: ", fav_teams)
            with open('config.json', 'w') as f:
                json.dump(config, f)
                break
