import json
import update
import parse
import time
import change

if __name__ == "__main__":
    print()
    print("Welcome to Watchr!")
    print()
    with open('config.json', 'r') as f:
        try:
            config = json.load(f)
            #update.start()
            print("Current configuration: ")
            print("Point difference - ", config["max_point_difference"])
            print("Favorite teams - ", config["fav_teams"])
            print()
            edit = input("If you would like to edit your configuration, please type 'edit'. Else, press enter: ")
            if edit == "edit" or edit == "Edit":
                print("Old data has been cleared. Re-configuration will begin.")
                change.configure()
            input("Today is " + time.strftime("%d/%m/%Y") + ". The time is " + time.strftime("%H:%M:%S") + ". Press enter to see a list of reccomended games: ")
            current_games = parse.organize()
            for game in current_games:
                if game.home in config["fav_teams"] or game.away in config["fav_teams"]:
                    print()
                    print(game)
                elif game.point_difference <= config["max_point_difference"]:
                    print()
                    print(game)
            print()
        except ValueError:
            input("No config file was found. Press enter to create one.")
            change.configure()
